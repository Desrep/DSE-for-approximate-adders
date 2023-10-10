####Dummy flow, tests every adder in the database by replacing it in the dut#############


import os
import re

os.system('rm design_space.txt')
with open('design_space.txt','w') as space:
    space.write('design, area, power, delay\n')
    
adder_type = ['STD0','LOA1','LOA2','LOA3']

for atype in adder_type: #for every adder type
    to_write = re.split(r'(\d+)',atype)
    with open('adder_selection.txt','w') as select:
        select.write(to_write[0]+" "+to_write[1])
    os.system("python3 adder_builder.py") #first create adder
    os.system("python3 py_to_verilog.py") # convert dut to verilog
    os.system("python3 synth_and_metrics.py") # synthesize and get metrics
    with open('metrics_output.csv') as metric:
        for line,data in enumerate(metric):
            if(line == 1):
                with open('design_space.txt','a') as space:
                    space.write(data+'\n')

