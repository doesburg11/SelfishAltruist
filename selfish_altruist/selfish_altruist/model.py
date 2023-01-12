"""
Selfish-Altruist Model

Reproduction of:
 Wilensky, U. (1997). NetLogo Selfish-Altruist model
"""

import mesa
import random

from selfish_altruist.scheduler import BaseSchedulerByFilteredType

from selfish_altruist.agents import SelfishAltruistAgent


class SelfishAltruist(mesa.Model):
    n_grid_cells_height = 5
    n_grid_cells_width = 5
    canvas_width = 400
    canvas_height = canvas_width * (n_grid_cells_height / n_grid_cells_width)
    altruistic_probability = 0.26
    selfish_probability = 0.26
    cost_of_altruism = 0.13
    benefit_of_altruism = 0.5
    disease = 0.0
    harshness = 0.0

    verbose_1 = True  # Fitness values in grid and advanced tooltips

    description = (
        "A model for simulating Selfish-Altruist behavior."
    )

    def __init__(
            self,
            n_grid_cells_width=n_grid_cells_width,
            n_grid_cells_height=n_grid_cells_height,
            altruistic_probability=altruistic_probability,
            selfish_probability=selfish_probability,
            cost_of_altruism=cost_of_altruism,
            benefit_of_altruism=benefit_of_altruism,
            disease=disease,
            harshness=harshness

    ):
        """
        Create a new Predator-Prey model with the given parameters.

        Args:
        """
        super().__init__()
        # Set parameters
        self.n_grid_cells_width = n_grid_cells_width
        self.n_grid_cells_height = n_grid_cells_height
        self.n_cells = n_grid_cells_width * n_grid_cells_height

        self.n_altruist = 0
        self.n_selfish = 0
        self.n_population = 0
        self.n_void = 0
        self.percentage_of_altruist = 0.0

        # fitness parameters
        self.harshness = harshness  # =/= to fitnes of a Void patch
        self.disease = disease

        # selfish-altruistic
        self.altruistic_probability = altruistic_probability
        self.selfish_probability = selfish_probability
        self.cost_of_altruism = cost_of_altruism
        self.benefit_of_altruism = benefit_of_altruism

        self.schedule = BaseSchedulerByFilteredType(self)

        self.grid = mesa.space.SingleGrid(self.n_grid_cells_width, self.n_grid_cells_height, torus=True)
        self.datacollector = mesa.DataCollector(

            model_reporters={
                "Selfish": lambda m: m.n_selfish,
                "Altruist": lambda m: m.n_altruist,
                "Void": lambda m: m.n_void,
                "Population": lambda m: m.n_population,
                "%Altruist": lambda m: m.percentage_of_altruist,
            },
            tables={
                "Fitness": ["position", "agent", "fitness"],
                "Lottery": ["position", "current agent", "P[selfish]", "P[altruists]", "P[harshness]"],
            },
        )

        # initialize patches
        for _, x, y in self.grid.coord_iter():
            selfish_altruist_agent = SelfishAltruistAgent(self.next_id(), (x, y), self)
            self.grid.place_agent(selfish_altruist_agent, (x, y))
            self.schedule.add(selfish_altruist_agent)
            ptype = random.uniform(0, 1)
            if ptype < self.altruistic_probability:
                selfish_altruist_agent.benefit_out = 0
                selfish_altruist_agent.name = "altruist"
                selfish_altruist_agent.pcolor = "blue"
                self.n_altruist += 1
            elif ptype < self.altruistic_probability + self.selfish_probability:
                selfish_altruist_agent.benefit_out = 1
                selfish_altruist_agent.name = "selfish"
                selfish_altruist_agent.pcolor = "red"
                self.n_selfish += 1
            else:
                selfish_altruist_agent.benefit_out = 0
                selfish_altruist_agent.name = "void"
                selfish_altruist_agent.pcolor = "black"
                selfish_altruist_agent.altruism_benefit = 0

        self.running = True

        self.n_population = self.n_altruist + self.n_selfish
        self.n_void = self.n_cells - self.n_population
        self.percentage_of_altruist = self.n_altruist / self.n_cells
        self.datacollector.collect(self)

    def step(self):
        self.n_population = self.n_altruist + self.n_selfish
        self.n_void = self.n_cells - self.n_population
        self.percentage_of_altruist = self.n_altruist / self.n_cells

        self.schedule.step()  # Base schedule to find out fitness per cell/agent
        # collect fitness per cell/agent in Table
        # print(self.datacollector.get_model_vars_dataframe())
        self.datacollector.collect(self)

        # print("round 1: calculate fitness per cell:")

        # print(self.percentage_of_altruist)
        grid_iterator = self.grid.coord_iter()
        for agent, x, y in grid_iterator:
            position_agent = (x, y)
            agent.sum_fitness_selfish_in_neighborhood = 0
            agent.sum_fitness_altruists_in_neighborhood = 0
            agent.sum_fitness_harshness_in_neighborhood = 0
            agent.sum_total_fitness_in_neighborhood = 0
            agent.weight_fitness_selfish_in_neighborhood = 0
            agent.weight_fitness_altruists_in_neighborhood = 0
            agent.weight_fitness_harshness_in_neighborhood = 0
            neighbor_iterator = self.grid.iter_neighbors(position_agent, moore=False, include_center=True, radius=1)
            for neighbor in neighbor_iterator:
                if neighbor.name == "selfish":
                    agent.sum_fitness_selfish_in_neighborhood += neighbor.fitness
                elif neighbor.name == "altruist":
                    agent.sum_fitness_altruists_in_neighborhood += neighbor.fitness
                elif neighbor.name == "void":
                    agent.sum_fitness_harshness_in_neighborhood += neighbor.fitness
            agent.sum_total_fitness_in_neighborhood = agent.sum_fitness_selfish_in_neighborhood + \
                                                      agent.sum_fitness_altruists_in_neighborhood + \
                                                      agent.sum_fitness_harshness_in_neighborhood + self.disease
            if agent.sum_total_fitness_in_neighborhood > 0:
                # lottery weights
                agent.weight_fitness_selfish_in_neighborhood = agent.sum_fitness_selfish_in_neighborhood / \
                                                               agent.sum_total_fitness_in_neighborhood
                agent.weight_fitness_altruists_in_neighborhood = agent.sum_fitness_altruists_in_neighborhood / \
                                                                 agent.sum_total_fitness_in_neighborhood
                agent.weight_fitness_harshness_in_neighborhood = (
                                                                         agent.sum_fitness_harshness_in_neighborhood + self.disease) / \
                                                                 agent.sum_total_fitness_in_neighborhood
            else:
                agent.weight_fitness_selfish_in_neighborhood = 0
                agent.weight_fitness_altruists_in_neighborhood = 0
                agent.weight_fitness_harshness_in_neighborhood = 0

            self.datacollector.add_table_row(
                "Lottery", {
                    "position": position_agent,
                    "current agent": agent.name,
                    "P[selfish]": agent.weight_fitness_selfish_in_neighborhood,
                    "P[altruists]": agent.weight_fitness_altruists_in_neighborhood,
                    "P[harshness]": agent.weight_fitness_harshness_in_neighborhood,
                }
            )
        grid_iterator = self.grid.coord_iter()
        for agent, x, y in grid_iterator:
            breed_chance = random.uniform(0, 1)
            if breed_chance < agent.weight_fitness_altruists_in_neighborhood:
                old_type_name = agent.name
                agent.benefit_out = 0  # todo: set into fitness equation
                agent.name = "altruist"
                agent.pcolor = "blue"
                if old_type_name != "altruist":
                    self.n_altruist += 1
                    if old_type_name == "selfish":
                        self.n_selfish -= 1
            elif breed_chance < agent.weight_fitness_altruists_in_neighborhood + agent.weight_fitness_selfish_in_neighborhood:
                old_type_name = agent.name
                agent.benefit_out = 1
                agent.name = "selfish"
                agent.pcolor = "red"
                if old_type_name != "selfish":
                    self.n_selfish += 1
                    if old_type_name == "altruist":
                        self.n_altruist -= 1
            else:
                old_type_name = agent.name
                if old_type_name == "altruist":
                    self.n_altruist -= 1
                elif old_type_name == "selfish":
                    self.n_selfish -= 1
                agent.benefit_out = 0
                agent.name = "void"
                agent.pcolor = "black"
                agent.altruism_benefit = 0
                agent.fitness = self.harshness
                agent.weight_fitness_selfish_in_neighborhood = 0
                agent.weight_fitness_altruists_in_neighborhood = 0
                agent.weight_fitness_harshness_in_neighborhood = 0
                agent.sum_fitness_selfish_in_neighborhood = 0
                agent.sum_fitness_altruists_in_neighborhood = 0
                agent.sum_fitness_harshness_in_neighborhood = 0
        df_selfish = self.datacollector.get_model_vars_dataframe()["Selfish"]
        df_altruist = self.datacollector.get_model_vars_dataframe()["Altruist"]
        percentage_altruist = df_altruist / (df_altruist + df_selfish)
        # print(df_selfish)
        df = self.datacollector.get_model_vars_dataframe()
        # df.insert(2, "%Altruist",  percentage_altruist, True)
        df["Population"] = df_selfish + df_altruist
        df["%Altruist"] = df_altruist / self.n_cells
        # print(df)
        # if df_selfish.iloc[-1] == 0 or df_altruist.iloc[-1] == 0:
        if self.percentage_of_altruist > 0.7:
            # https://stackoverflow.com/questions/34166030/obtaining-last-value-of-dataframe-column-without-index

            self.running = False
