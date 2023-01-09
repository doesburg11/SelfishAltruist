import mesa

from selfish_altruist.model import SelfishAltruist


def static_string(model):
    """
    Display a text count of how many happy agents there are.
    """
    return "Fitness values"  # f"Happy agents: {model.disease}"


def selfish_altruist_portrayal(agent):
    portrayal = {}

    if agent.name is "selfish":
        # agent layout
        portrayal["Shape"] = "rect"
        portrayal["w"] = 1
        portrayal["h"] = 1
        portrayal["Filled"] = "true"
        portrayal["Color"] = ["#FF0000"]  # ["#FF0000", "#FF9999"]
        portrayal["stroke_color"] = "#00FF00"

        if agent.model.verbose_1:
            portrayal["text"] = str(round(agent.fitness, 1))
            portrayal["text_color"] = "white"

            # tooltip content
            portrayal["type"] = "selfish"
            portrayal["id"] = agent.unique_id
            portrayal["N_A"] = agent.n_neighboring_altruists
            portrayal["fitness"] = str(round(agent.fitness, 1))
            portrayal["area fitness + disease"] = str(round(agent.sum_total_fitness_in_neighborhood, 2))
            portrayal["disease"] = str(round(agent.model.disease, 1))
            portrayal["lottery weight selfish"] = str(round(agent.weight_fitness_selfish_in_neighborhood, 2))
            portrayal["lottery weight altruist"] = str(round(agent.weight_fitness_altruists_in_neighborhood, 2))
            portrayal["lottery weight void"] = str(round(agent.weight_fitness_harshness_in_neighborhood, 2))
            portrayal["pos"] = str(agent.pos)
        portrayal["Layer"] = 1

    elif agent.name is "altruist":
        # agent layout
        portrayal["Shape"] = "rect"
        portrayal["w"] = 1
        portrayal["h"] = 1
        portrayal["Filled"] = "true"
        portrayal["Color"] = ["#0000FF"]
        if agent.model.verbose_1:
            portrayal["text"] = str(round(agent.fitness, 1))
            portrayal["text_color"] = "white"

            # tooltip content
            portrayal["type"] = "altruist"
            portrayal["id"] = agent.unique_id
            portrayal["N_A"] = agent.n_neighboring_altruists
            portrayal["fitness"] = str(round(agent.fitness, 1))
            portrayal["area fitness + disease"] = str(round(agent.sum_total_fitness_in_neighborhood, 2))
            portrayal["disease"] = str(round(agent.model.disease, 1))
            portrayal["lottery weight selfish"] = str(round(agent.weight_fitness_selfish_in_neighborhood, 2))
            portrayal["lottery weight altruist"] = str(round(agent.weight_fitness_altruists_in_neighborhood, 2))
            portrayal["lottery weight void"] = str(round(agent.weight_fitness_harshness_in_neighborhood, 2))
            portrayal["pos"] = str(agent.pos)
        portrayal["Layer"] = 1

    elif agent.name is "void":
        portrayal["Color"] = ["black"]
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["w"] = 1
        portrayal["h"] = 1
        if agent.model.verbose_1:
            portrayal["text"] = str(round(agent.fitness, 1))
            portrayal["text_color"] = "white"

            # tooltip content void
            portrayal["type"] = "Void"
            portrayal["id"] = agent.unique_id
            portrayal["N_A"] = agent.n_neighboring_altruists
            portrayal["fitness"] = str(round(agent.fitness, 1))
            portrayal["area fitness + disease"] = str(round(agent.sum_total_fitness_in_neighborhood, 2))
            portrayal["disease"] = str(round(agent.model.disease, 1))
            portrayal["lottery weight selfish"] = str(round(agent.weight_fitness_selfish_in_neighborhood, 2))
            portrayal["lottery weight altruist"] = str(round(agent.weight_fitness_altruists_in_neighborhood, 2))
            portrayal["lottery weight void"] = str(round(agent.weight_fitness_harshness_in_neighborhood, 2))
            portrayal["pos"] = str(agent.pos)
        portrayal["Layer"] = 1

    return portrayal


canvas_element = mesa.visualization.CanvasGrid(
    selfish_altruist_portrayal,
    SelfishAltruist.n_grid_cells_width,
    SelfishAltruist.n_grid_cells_height,
    SelfishAltruist.canvas_width,
    SelfishAltruist.canvas_height)

text_element = mesa.visualization.TextElement()

chart_element = mesa.visualization.ChartModule(
    [
        {"Label": "Selfish", "Color": "#FF0000"},
        {"Label": "Altruist", "Color": "#9999FF"},
        {"Label": "Void", "Color": "black"},
    ]
)

model_params = {
    "title": mesa.visualization.StaticText(
        "Parameters:"
    ),
    "altruistic_probability": mesa.visualization.Slider(
        "altruistic-probability", 0.26, 0.0, 0.5, 0.01
    ),
    "selfish_probability": mesa.visualization.Slider(
        "selfish-probability", 0.26, 0.0, 0.5, 0.01
    ),
    "cost_of_altruism": mesa.visualization.Slider(
        "cost-of-altruism", 0.13, 0.0, 0.9, 0.01
    ),
    "benefit_of_altruism": mesa.visualization.Slider(
        "benefit-of-altruism", 0.48, 0.0, 0.9, 0.01
    ),
    "disease": mesa.visualization.Slider(
        "disease", 0.2, 0.0, 1.0, 0.01
    ),
    "harshness": mesa.visualization.Slider(
        "harshness", 0.96, 0.0, 1.0, 0.01
    ),

}

server = mesa.visualization.ModularServer(
    SelfishAltruist,

    [canvas_element, static_string, chart_element],
    "Selfish-Altruist Model",
    model_params
)
server.port = 8521
