####Dummy flow, tests every adder in database by replacing it in the dut#############

import numpy as np

from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.core.problem import Problem
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.repair.rounding import RoundingRepair
from pymoo.operators.sampling.rnd import IntegerRandomSampling
from pymoo.optimize import minimize



import os
from scipy.optimize import basinhopping

def step_routine(x):
    x[0] += -1 + np.random.randint(5,size = 1)
    print(int(x))
    return int(x)




os.system('rm design_space.txt')
with open('design_space.txt','w') as space:
    space.write('design, area, power, delay\n')


def print_fun(x,f,accepted):
    print("minimo local %f %d" % (f,int(accepted)))

minimizer_kwargs = {"method": "BFGS"}

class ThisProblem(Problem):

    def __init__(self):
        super().__init__(n_var=1, n_obj=1, n_ieq_constr = 1, xl = 0, xu = 3, vtype = int)

    def _evaluate(self,x,out,*args,**kwargs):
        out["F"] = [objective_func(x)]
        out["G"] = -x

def objective_func(x):
    if(x[0]==0):
        atype = 'STD'
    elif(x[0]==1):
        atype = 'LOA1'
    elif(x[0]==2):
        atype = 'LOA2'
    elif(x[0]==3):
        atype = 'LOA3'
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
                f = np.array([float(data.split()[1].strip(','))])
                print(f)
    return f

problem = ThisProblem()

method = GA(pop_size=1,
            sampling=IntegerRandomSampling(),
            crossover=SBX(prob=1.0, eta=3.0, vtype=float, repair=RoundingRepair()),
            mutation=PM(prob=1.0, eta=3.0, vtype=float, repair=RoundingRepair()),
            eliminate_duplicates=True,
            )

res = minimize(problem,
               method,
               termination=('n_gen', 5),
               seed=1,
               save_history=True
               )

print("Best solution found: %s" % res.X)
print("Function value: %s" % res.F)
print("Constraint violation: %s" % res.CV)




