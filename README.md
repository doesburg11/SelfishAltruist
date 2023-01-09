## WHAT IS IT?

This is an evolutionary biology model.  It models population genetics with respect to the fitness of traits that are affected by social and environmental conditions.  The model has two types of patch agents: altruistic agents and selfish agents.

The basic premise of the model is that the selfish agents and the altruistic agents are competing for each spot in the world by entering into a genetic lottery.  You can imagine these agents as plants who "seed" for a spot, and the dominant seed generally wins.  The details of the lottery are explained below in HOW IT WORKS.

Under normal (non-interfering) environmental conditions, the selfish agents win, and the altruistic population is driven to extinction.  However, as outlined in HOW TO USE IT, when the environmental conditions are made more harsh, the altruistic population is able to survive, and even dominate the selfish population.

This model (and Cooperation and Divide the Cake) are part of the EACH unit ("Evolution of Altruistic and Cooperative Habits: Learning About Complexity in Evolution").  See http://ccl.northwestern.edu/rp/each/index.shtml for more information on the EACH unit. The EACH unit is embedded within the BEAGLE (Biological Experiments in Adaptation, Genetics, Learning and Evolution) evolution curriculum. See http://ccl.northwestern.edu/rp/beagle/index.shtml.

## HOW IT WORKS

1. Patches live in five-cell, plus-sign-shaped neighborhoods.  Whenever a patch is calculating something about its fitness, it is the center of the neighborhood.  For another patch, when that patch is calculating, it becomes merely one of the neighbors.

2. Each patch is an agent that has a fitness.  Each patch is also the location of a lottery for its space.  The patch and the four surrounding patches put in "seeds" to try to get the patch turned to their type of patch, altruist or selfish. Being successful in the lottery is getting patches to turn to your type.  We're assuming here that the type (altruistic or selfish) is the important genetic trait.

3.  Each patch calculates its own fitness using equation:
    if it is A (altruist): 1 - cost + (Number Altruists in Neighborhood / 5 * benefit from Altruists)
    if it is S (selfish):  1 + (Number Altruists in Neighborhood / 5 * benefit from Altruists)
    Thus, the fitness of the S patch will be higher than the fitness of the A's.  If the cost is 0.2 and benefit is 0.5, for an A surrounded by two S's and two A's, then the fitness of this spot is 1 - 0.2 + (3/5 * 0.5) = 1.1.

4.  After each patch has calculated its fitness, it looks to its four neighbors.  Each of the five patches, including itself, puts a weighted seed into a genetic lottery for this center spot.  So, for example, if the neighborhood is ASASA, each of the three A's register their fitness value, and each of the two S's put in their fitness.  The A's are added, and the S's are added.  Let us assume that the A's add up to 3.2 (this includes the A in the center spot), and the S's add up to 2.6.  These two numbers are the altruist weight and selfish weight respectively, in the lottery for the center spot.  Now, the larger number, whichever it is, is called the Major seed; it is divided by the sum of all the fitnesses.
    Thus, 3.2/(3.2 + 2.6) = .552.  This number is the Altruism seed in the lottery.  The minor seed is 2.6/(3.2 + 2.6) = .448. (Notice that the Altruism seed of the parent is 3/5 = .600, while the child's is .552.  Even though altruism is dominating, it is losing ground.)

5.  There are a number of ways of doing the lottery itself.  Currently, we choose a random number between 0 and 1.  Now, if the Number is below the Minor seed, the minor weight gets the spot, and if it is above the major seed, the major seed gets the spot.  So, in the example, if the random number is anywhere from .449 to 1, then the Major seed gets it. If it is between 0 and .448, the minor seed gets it.

## HOW TO USE IT

SETUP button --- sets up the model by creating the agents.

GO button --- runs the model

ALTRUISTIC-PROBABILITY slider --- lets you determine the initial proportion of altruists

SELFISH-PROBABILITY slider --- determines the initial proportion of selfish agents.

ALTRUISM-COST slider --- determines the value of cost in the above fitness equations.

BENEFIT-FROM-ALTRUISM slider --- determines the value of benefit in the above fitness equations.

There are two sliders for controlling environmental variables:

HARSHNESS slider --- sets the value for the resistance of empty patch spots to being populated by agents.  The value for this slider determines a corresponding value in the lottery for each empty (black) spot on the grid; the higher this value, the more difficult it is to populate.

DISEASE slider --- sets the value for the possibility that the agents in occupied spots will die.  The value for this slider is factored into the genetic lottery, and determines the percentage chance that each agent will die out from their spot.

## THINGS TO TRY

1.  At first, run the model with Harshness and Disease both at 0.  Notice that the selfish population quickly dominates the world, driving the altruistic population to extinction.  How do respective population sizes affect the outcome?

2.  Play with the values of cost and benefit.  What are realistic values for actual genetic competition?  How does initial population size effect the significance of these values?

3.  Increase the Harshness and Disease values, independently, and with respect to one another.  What are the effects of the Harshness Model?  of Disease?  How are the values dependent on one another?  At what values does the altruistic population begin to have greater success?

4.  Consider why the introduction of Harshness and Disease conditions affects the success of the altruistic population.  How does each population, run alone, respond to the Harshness and Disease conditions?  If you imagine the black spots as Voids (a third type of competing agent), what is the fitness relationship between Altruists and Voids?  Selfish agents and Voids?

5.  Can you find slider values that maximize the advantage of the altruistic agents?

6.  Try running BehaviorSpace on this model to explore the model's behavior under a range of initial conditions.

## EXTENDING THE MODEL

The model can be extended in a number of interesting directions, including adding new environmental variables, adding different types of agents, and changing the altruistic and selfish weighting under different environmental conditions.

This model does not address the behaviors of individuals, only the relative weights of genetic traits.  A next step in considering the evolution of altruism is to model altruistic behaviors.  (See the related model: Cooperation.)

## NETLOGO FEATURES

This model uses patches as its basic agents. Can you design an "equivalent" model using turtles?  How would the model dynamics be affected?

## RELATED MODELS

* Cooperation
* Divide the Cake

## CREDITS AND REFERENCES

This model, the Cooperation model and the Divide the Cake model are part of the curriculum unit "Evolution of Altruistic and Cooperative Habits: Learning About Complexity in Evolution".  See http://ccl.northwestern.edu/rp/each/index.shtml for more information. The EACH unit is embedded within the BEAGLE (Biological Experiments in Adaptation, Genetics, Learning and Evolution) evolution curriculum. See http://ccl.northwestern.edu/rp/beagle/index.shtml.

This model is based on a paper by Mitteldorf and Wilson, 2000, "Population Viscosity and the Evolution of Altruism", Journal of Theoretical Biology, v.204, pp.481-496.

Thanks also to Damon Centola and Scott Styles.

## HOW TO CITE

If you mention this model or the NetLogo software in a publication, we ask that you include the citations below.

For the model itself:

* Wilensky, U. (1998).  NetLogo Altruism model.  http://ccl.northwestern.edu/netlogo/models/Altruism.  Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

Please cite the NetLogo software as:

* Wilensky, U. (1999). NetLogo. http://ccl.northwestern.edu/netlogo/. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

## COPYRIGHT AND LICENSE

Copyright 1998 Uri Wilensky.

![CC BY-NC-SA 3.0](http://ccl.northwestern.edu/images/creativecommons/byncsa.png)

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License.  To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.

Commercial licenses are also available. To inquire about commercial licenses, please contact Uri Wilensky at uri@northwestern.edu.

This model was created as part of the project: CONNECTED MATHEMATICS: MAKING SENSE OF COMPLEX PHENOMENA THROUGH BUILDING OBJECT-BASED PARALLEL MODELS (OBPML).  The project gratefully acknowledges the support of the National Science Foundation (Applications of Advanced Technologies Program) -- grant numbers RED #9552950 and REC #9632612.

This model was converted to NetLogo as part of the projects: PARTICIPATORY SIMULATIONS: NETWORK-BASED DESIGN FOR SYSTEMS LEARNING IN CLASSROOMS and/or INTEGRATED SIMULATION AND MODELING ENVIRONMENT. The project gratefully acknowledges the support of the National Science Foundation (REPP & ROLE programs) -- grant numbers REC #9814682 and REC-0126227. Converted from StarLogoT to NetLogo, 2001.

<!-- 1998 2001 -->