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


##################################################################
# Problem definition
#x selects the type of adder and y the number of approximation bits############
# Results are area,power,delay and MAE , no constraints for now#################
#
#
###################################################################################

class ThisProblem(ElementwiseProblem):

    def __init__(self,**kwargs):
        vars = {
            "x": Integer(bounds=(0, 2)),
            "y":Integer(bounds=(1,6))
        }
        super().__init__(vars=vars, n_obj=3,n_ieq_constr=0,**kwargs)


    def _evaluate(self,x,out,*args,**kwargs):
        x,y = x["x"],x["y"]
        out["F"] = objective_func(x,y)
        with open('design_space_exploration.txt','a') as dse:
            dse.write(str(out["F"])+'\n')
        print(out)

#################################################################################################
# Procedure for getting output values
# includes synthesis                                                     #########################
#
#
#################################################################################################
def objective_func(x,y):
    if(x==0):
        atype = 'COPY'
    elif(x==1):
        atype = 'TRUN'
    elif(x==2):
        atype = 'LOA'
    
    with open('adder_selection.txt','w') as select:
        select.write(atype+" "+str(y))
    with open('design_space_exploration.txt','a') as dse:
        dse.write(atype+str(y)+'\n')
    os.system("python3 adder_builder.py") #first create adder
    os.system('python3 dut_tb.py') #run test bench with this adder approximation
    os.system("python3 out_extract.py") #extract output values
   
#####calculate MAE############################################################################
    approx_value = [] 
    with open ("output_values.txt", "r") as outval:
        for line in outval:
            approx_value.append(int(line,2))
    golden_value = []
    with open ("golden_values.txt", "r") as outval:
        for line in outval:
            golden_value.append(int(line,2))
    mae_val = mae(golden_value,approx_value)
    print("mae is "+str(mae_val)+"\n")

    os.system("python3 py_to_verilog.py") # convert dut to verilog
    os.system("python3 synth_and_metrics.py") # synthesize and get metrics
    with open('metrics_output.csv') as metric:
        for line,data in enumerate(metric):
            if(line == 1):
                with open('design_space.txt','a') as space:
                    space.write(data+'\n')
                #f = [float(data.split()[1].strip(',')), float(data.split()[2].strip(','))*1e5, float(data.split()[3].strip(',')),float(mae_val)]
                f = [float(data.split()[1].strip(',')), float(data.split()[3].strip(',')),float(mae_val)]
    return f

################################################### golden run #################################################################

with open('adder_selection.txt','w') as select:
    select.write("STD 0")
os.system("python3 adder_builder.py") #first create adder
os.system('python3 dut_tb.py') #run DUT for reference
os.system("python3 out_extract.py") #extract output values
os.system("mv output_values.txt golden_values.txt") #rename output to golden


##############################################################################################################################

######################### MAE calculation definition############################################################################
def mae(golden, aprox):
    y_true, aprox = np.array(golden), np.array(aprox)
    return np.mean(np.abs(golden - aprox))
##########################################################################################################################


##################################Run exploration#################################################
problem = ThisProblem()

algorithm = MixedVariableGA(pop_size=10, survival=RankAndCrowdingSurvival())

res = minimize(problem,
               algorithm,
               ('n_gen', 20),
               seed=1,
               save_history = True,
               verbose=False)


#############################Plot the results##################################################
plot = Scatter()
plot.add(problem.pareto_front(), plot_type="surface", color="blue", alpha=0.7)
plot.add(res.F, facecolor="none", edgecolor="red")
with open('design_space_exploration.txt') as dsp:
    for data in dsp:
        if(len(data.split())!= 1):
            #design_space = [float((data.split()[0].strip(',')).strip('[')), float(data.split()[1].strip(',')), float(data.split()[2].strip(',')), float((data.split()[3].strip(',')).strip(']'))]
            design_space = [float((data.split()[0].strip(',')).strip('[')), float(data.split()[1].strip(',')), float((data.split()[2].strip(',')).strip(']'))]

            plot.add(np.array(design_space), facecolor = "none", edgecolor = "black")
plot.show()


print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))
