####Dummy flow, tests every adder in database by replacing it in the dut#############

import numpy as np
from pymoo.core.problem import Problem
from pymoo.visualization.scatter import Scatter
from pymoo.algorithms.moo.nsga2 import RankAndCrowdingSurvival
from pymoo.core.mixed import MixedVariableGA
from pymoo.optimize import minimize
from pymoo.core.problem import ElementwiseProblem
from pymoo.core.variable import Real, Integer, Choice, Binary
import os


os.system('rm design_space_exploration.txt')
os.system('rm design_space.txt')
with open('design_space.txt','w') as space:
    space.write('design, area, power, delay\n')



class ThisProblem(ElementwiseProblem):

    def __init__(self,**kwargs):
        vars = {
            "x": Integer(bounds=(0, 1)),
            "y":Integer(bounds=(1,10))
        }
        super().__init__(vars=vars, n_obj=3,n_ieq_constr=0,**kwargs)




    def _evaluate(self,x,out,*args,**kwargs):
        x,y = x["x"],x["y"]
        out["F"] = objective_func(x,y)
        with open('design_space_exploration.txt','a') as dse:
            dse.write(str(out["F"])+'\n')
        print(out)

def objective_func(x,y):
    if(x==0):
        atype = 'LOA'
    else:
        atype = 'COPY'
    
    with open('adder_selection.txt','w') as select:
        select.write(atype+" "+str(y))
    os.system("python3 adder_builder.py") #first create adder
    os.system("python3 py_to_verilog.py") # convert dut to verilog
    os.system("python3 synth_and_metrics.py") # synthesize and get metrics
    with open('metrics_output.csv') as metric:
        for line,data in enumerate(metric):
            if(line == 1):
                with open('design_space.txt','a') as space:
                    space.write(data+'\n')
                f = [float(data.split()[1].strip(',')), float(data.split()[2].strip(','))*1e5, float(data.split()[3].strip(','))]
    return f

problem = ThisProblem()

algorithm = MixedVariableGA(pop_size=10, survival=RankAndCrowdingSurvival())

res = minimize(problem,
               algorithm,
               ('n_gen', 5),
               seed=1,
               save_history = True,
               verbose=False)


plot = Scatter()
plot.add(problem.pareto_front(), plot_type="surface", color="blue", alpha=0.7)
plot.add(res.F, facecolor="none", edgecolor="red")
with open('design_space_exploration.txt') as dsp:
    for data in dsp:
        design_space = [float((data.split()[0].strip(',')).strip('[')), float(data.split()[1].strip(',')), float((data.split()[2].strip(',')).strip(']'))]
        plot.add(np.array(design_space), facecolor = "none", edgecolor = "black")
plot.show()


print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))
