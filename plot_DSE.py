import numpy as np
from pymoo.core.problem import Problem
from pymoo.visualization.scatter import Scatter
from pymoo.algorithms.moo.nsga2 import RankAndCrowdingSurvival
from pymoo.core.mixed import MixedVariableGA
from pymoo.optimize import minimize
from pymoo.core.problem import ElementwiseProblem
from pymoo.core.variable import Real, Integer, Choice, Binary
import os

#############################Plot the results##################################################
plot = Scatter()
#plot.add(problem.pareto_front(), plot_type="surface", color="blue", alpha=0.7)
#plot.add(res.F, facecolor="none", edgecolor="red")
with open('design_space_exploration.txt') as dsp:
    for data in dsp:
        if(len(data.split()) < 4):
            #design_space = [float((data.split()[0].strip(',')).strip('[')), float(data.split()[1].strip(',')), float(data.split()[2].strip(',')), float((data.split()[3].strip(',')).strip(']'))]
            design_space = [float((data.split()[0].strip(',')).strip('[')), float((data.split()[1].strip(',')).strip(']'))]

            plot.add(np.array(design_space), facecolor = "none", edgecolor = "black")
plot.show()

