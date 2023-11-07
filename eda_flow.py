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
import re



os.system('rm design_space_exploration.txt')
os.system('rm design_space.txt')
with open('design_space.txt','w') as space:
    space.write('design, area, power, delay\n')


###################################################################
#Obtain number of adders

number_of_adders = 0
with open('dut_base.py') as dut_file:
    for line in dut_file:
        area=re.search('[aA][dD][dD][eE][rR].*\s+=',line)
        if(area):
            number_of_adders += 1
    print(number_of_adders)




##################################################################
# Problem definition
#x selects the type of adder and y the number of approximation bits############
# Results are area,power,delay and MAE , no constraints for now#################
# 
#
###################################################################################

#********************************************************************!!!!!!!!!!!!!!!!!!!!!!
#nota# ver si la codificacion se puede mejorar sin que sea muy dificil
#***********************************************************************!!!!!!!!!!!!!!!!!!!!!!!
#Nota: Crear el bound de y1 de forma automatica con number_of_adders

def exhaustive_run():
    for x1 in range(512):
        for x0 in range(1,512):
            out = []
            ys = []
            yindex = []
            qty = 0
            y1 = 0
            orx = x0|x1
            for i in range(8):
                tor  = (orx>>i)&1
                if tor == 1:
                    qty = qty + 1
                    yindex.append(str(i))
                    ys.append(str(tor))
            if qty == 1:
                for i in range(10):
                    ind = int(yindex[0])
                    y1 = i*10**ind
                    out = objective_func(x0,x1,y1)
                    with open('design_space_exploration.txt','a') as dse:
                        dse.write(str(out)+'\n')
                    print(out)
                    y1 = 0
            elif qty == 2:
                for i in range(10):
                    for j in range(10):
                        ind1 = int(yindex[0])
                        ind2 = int(yindex[1])
                        y1 = i*10**ind1 + j*10**ind2
                        out = objective_func(x0,x1,y1)
                        with open('design_space_exploration.txt','a') as dse:
                            dse.write(str(out)+'\n')
                        print(out)
                        y1 = 0
            elif qty == 3:
                for i in range(10):
                    for j in range(10):
                        for k in range(10):
                            ind1 = int(yindex[0])
                            ind2 = int(yindex[1])
                            ind3 = int(yindex[2])
                            y1 = i*10**ind1 + j*10**ind2 + k*10**ind3
                            out = objective_func(x0,x1,y1)
                            with open('design_space_exploration.txt','a') as dse:
                                dse.write(str(out)+'\n')
                            print(out)
                            y1 = 0
            elif qty == 4:
                for i in range(10):
                    for j in range(10):
                        for k in range(10):
                            for p in range(10):
                                ind1 = int(yindex[0])
                                ind2 = int(yindex[1])
                                ind3 = int(yindex[2])
                                ind4 = int(yindex[3])
                                y1 = i*10**ind1 + j*10**ind2 + k*10**ind3 +  p*10**ind4
                                out = objective_func(x0,x1,y1)
                                with open('design_space_exploration.txt','a') as dse:
                                    dse.write(str(out)+'\n')
                                print(out)
                                y1 = 0
            elif qty == 5:
                for i in range(10):
                    for j in range(10):
                        for k in range(10):
                            for p in range(10):
                                for q in range(10):
                                    ind1 = int(yindex[0])
                                    ind2 = int(yindex[1])
                                    ind3 = int(yindex[2])
                                    ind4 = int(yindex[3])
                                    ind5 = int(yindex[4])
                                    y1 = i*10**ind1 + j*10**ind2 + k*10**ind3 + p*10**ind4 + q*10**ind5
                                    out = objective_func(x0,x1,y1)
                                    with open('design_space_exploration.txt','a') as dse:
                                        dse.write(str(out)+'\n')
                                    print(out)
                                    y1 = 0
            elif qty == 6:
                for i in range(10):
                    for j in range(10):
                        for k in range(10):
                            for p in range(10):
                                for q in range(10):
                                    for t in range(10):
                                        ind1 = int(yindex[0])
                                        ind2 = int(yindex[1])
                                        ind3 = int(yindex[2])
                                        ind4 = int(yindex[3])
                                        ind5 = int(yindex[4])
                                        ind6 = int(yindex[5])
                                        y1 = i*10**ind1 + j*10**ind2 + k*10**ind3 + p*10**ind4 + q*10**ind5 + t*10**ind6
                                        out = objective_func(x0,x1,y1)
                                        with open('design_space_exploration.txt','a') as dse:
                                            dse.write(str(out)+'\n')
                                        print(out)
                                        y1 = 0
            elif qty == 7:
                for i in range(10):
                    for j in range(10):
                        for k in range(10):
                            for p in range(10):
                                for q in range(10):
                                    for t in range(10):
                                        for m in range(10):
                                            ind1 = int(yindex[0])
                                            ind2 = int(yindex[1])
                                            ind3 = int(yindex[2])
                                            ind4 = int(yindex[3])
                                            ind5 = int(yindex[4])
                                            ind6 = int(yindex[5])
                                            ind7 = int(yindex[6])
                                            y1 = i*10**ind1 + j*10**ind2 + k*10**ind3 + p*10**ind4 + q*10**ind5 + t*10**ind6 + m*10**ind7
                                            out = objective_func(x0,x1,y1)
                                            with open('design_space_exploration.txt','a') as dse:
                                                dse.write(str(out)+'\n')
                                            print(out)
                                            y1 = 0
            elif qty == 8:
                for i in range(10):
                    for j in range(10):
                        for k in range(10):
                            for p in range(10):
                                for q in range(10):
                                    for t in range(10):
                                        for m in range(10):
                                            for n in range(10):
                                                ind1 = int(yindex[0])
                                                ind2 = int(yindex[1])
                                                ind3 = int(yindex[2])
                                                ind4 = int(yindex[3])
                                                ind5 = int(yindex[4])
                                                ind6 = int(yindex[5])
                                                ind7 = int(yindex[6])
                                                ind8 = int(yindex[7])
                                                y1 = i*10**ind1 + j*10**ind2 + k*10**ind3 + p*10**ind4 + q*10**ind5 + t*10**ind6 + m*10**ind7 + n*10**ind8
                                                out = objective_func(x0,x1,y1)
                                                with open('design_space_exploration.txt','a') as dse:
                                                    dse.write(str(out)+'\n')
                                                print(out)
                                                y1 = 0


#################################################################################################
# Procedure for getting output values
# includes synthesis                                                     #########################
#
#
#################################################################################################
def objective_func(x0,x1,y1):
    
    bits_list = str(y1)
    add_count = 1
    padding = ''

    if(len(bits_list)<number_of_adders): #number needs to have at least number_of_adder digits
        for i in range(number_of_adders - len(bits_list)):
            padding = padding+'0'

    bits_list = padding+bits_list
    print(bits_list)
    with open('adder_selection.txt','w') as select:
        for i in range(number_of_adders):
            t1 = (x1>>i&1)
            t0 = (x0>>i&1)
            print(str(t1)+str(t0)) #binary code for adder type
            if((t1 == 0) and (t0 == 0)):
                atype = 'STD'
            elif((t1 == 0) and (t0 == 1)):
                atype = 'COPY'
            elif((t1 == 1) and (t0 == 0)):
                atype = 'TRUN'
            elif((t1 == 1) and (t0 == 1)):
                atype = 'LOA'

            print(atype)
            y = bits_list[i]
            y = int(y) + 1 #prevents 0 as approximation bits
            y = str(y)
            # approx number of bits go from 1 to 10 then

            if(atype == 'STD'):
                select.write(atype+" 0 "+str(add_count)+"\n")
            else:
                select.write(atype+" "+y+" "+str(add_count)+"\n")
                print(y)
            add_count += 1
    with open('design_space_exploration.txt','a') as dse:
        dse.write(bin(x1)+' '+bin(x0)+' '+y+' adder type and number of approximate bits'+'\n')
    os.system("python3 adder_builder.py") #first create adder
    os.system("python3 dut_builder.py") # build the new dut file
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
    for counter in range(number_of_adders):
        select.write("STD 0 1\n")
os.system("python3 adder_builder.py") #first create adder
os.system("python3 dut_builder.py") # build the new dut file
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
exhaustive_run()


#############################Plot the results##################################################
plot = Scatter()
with open('design_space_exploration.txt') as dsp:
    for data in dsp:
        if(len(data.split()) < 4):
            #design_space = [float((data.split()[0].strip(',')).strip('[')), float(data.split()[1].strip(',')), float(data.split()[2].strip(',')), float((data.split()[3].strip(',')).strip(']'))]
            design_space = [float((data.split()[0].strip(',')).strip('[')), float(data.split()[1].strip(',')), float((data.split()[2].strip(',')).strip(']'))]
                
            plot.add(np.array(design_space), facecolor = "none", edgecolor = "black")
plot.show()


