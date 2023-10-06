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



os.system('rm design_space.txt')
with open('design_space.txt','w') as space:
    space.write('design, area, power, delay\n')




class ThisProblem(ElementwiseProblem):

    def __init__(self,**kwargs):
        vars = {
            "x": Integer(bounds=(0, 1)),
            "y":Integer(bounds=(0,3))
        }
        super().__init__(vars=vars, n_obj=3,n_ieq_constr=0,**kwargs)




    def _evaluate(self,x,out,*args,**kwargs):
        x,y = x["x"],x["y"]
        out["F"] = [objective_func(x,y)]
        print(out)
        #out["G"] = out["F"][0][0]+out["F"][0][1]*1e5+out["F"][0][2]-900 

def objective_func(x,y):
    if((x==0)and(y==0)):
        atype = 'STD'
    elif((x==0)and(y==1)):
        atype = 'LOA1'
    elif((x==0)and(y==2)):
        atype = 'LOA2'
    elif((x==0)and(y==3)):
        atype = 'LOA3'
    elif((x==1)and(y==1)):
        atype = 'LOWA1'
    elif((x==1)and(y==2)):
        atype = 'LOWA2'
    elif((x==1)and(y==3)):
        atype = 'LOWA3'
    else:
        atype = 'STD'
    print(atype)
    with open('adder_selection.txt','w') as select:
        select.write(atype)
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
               ('n_gen', 20),
               seed=1,
               verbose=False)

plot = Scatter()
plot.add(problem.pareto_front(), plot_type="line", color="black", alpha=0.7)
plot.add(res.F, facecolor="none", edgecolor="red")
plot.show()


print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))
