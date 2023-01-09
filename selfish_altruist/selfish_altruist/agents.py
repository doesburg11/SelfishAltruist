import mesa
from mesa.space import SingleGrid


class Patch(mesa.Agent):

    def __init__(self, unique_id, pos, model):
        """
        Creates a new patch of grass

        Args:
            fully_grown: (boolean) Whether the patch of grass is fully grown or not
        """
        super().__init__(unique_id, model)
        self.name = str()
        self.pcolor = str()
        self.pos = pos
        self.fitness: float = 0

        self.n_neighboring_altruists = 0  # N_A in paper
        self.sum_fitness_selfish_in_neighborhood = 0
        self.sum_fitness_altruists_in_neighborhood = 0
        self.sum_fitness_harshness_in_neighborhood = 0
        self.sum_total_fitness_in_neighborhood = 0
        self.weight_fitness_selfish_in_neighborhood = 0
        self.weight_fitness_altruists_in_neighborhood = 0
        self.weight_fitness_harshness_in_neighborhood = 0

    def n_neighboring_agents(self):
        # print("position " + str(self.pos))
        n_neighbor_selfish = 0
        n_neighbor_altruists = 0
        n_neighbor_voids = 0
        neighbor_iterator = self.model.grid.iter_neighbors(self.pos, moore=False, include_center=True, radius=1)
        for neighbor in neighbor_iterator:
            # print(str(neighbor.pos) + ":  " + str(neighbor.name))
            if neighbor.name == "selfish":
                n_neighbor_selfish += 1
            elif neighbor.name == "altruist":
                n_neighbor_altruists += 1
            if neighbor.name == "void":
                n_neighbor_voids += 1
        n_neigborhood_cells = n_neighbor_selfish + n_neighbor_altruists + n_neighbor_voids
        # print("n_neigborhood_cells")
        # print(n_neigborhood_cells)

        return n_neighbor_selfish, n_neighbor_altruists, n_neighbor_voids, n_neigborhood_cells

    def calculate_fitness(self):
        self.n_neighboring_altruists = self.n_neighboring_agents()[1]  # N_A in paper
        n_neighbor_cells = self.n_neighboring_agents()[3]
        c = self.model.cost_of_altruism
        b = self.model.benefit_of_altruism
        fitness_void = self.model.harshness

        if self.name is "altruist":
            return 1 - c + b * self.n_neighboring_altruists / n_neighbor_cells
        elif self.name is "selfish":
            return 1 + b * (self.n_neighboring_altruists / n_neighbor_cells)
        elif self.name is "void":
            return fitness_void

    def step(self):
        n_selfish, n_altruists, n_voids, n_cells = self.n_neighboring_agents()
        self.fitness = self.calculate_fitness()
        self.model.datacollector.add_table_row(
            "Fitness", {
                "position": self.pos,
                "agent": self.name,
                "fitness": self.calculate_fitness(),
            }
        )

    # print("position " + str(self.pos) + " fitness " + str(self.name) + " = " + str(self.fitness()) + " N_A = " + str(
    #    n_altruists))
    # print("n_altruists")
    # print(n_altruists)
    # print("n_altruists/5")
    # print(float(n_altruists / n_cells))
