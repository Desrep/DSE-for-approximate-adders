import os
import re

os.system('rm dut.py')

adder_number = 0
with open('adder_selection.txt','r') as sel_adder:
    for line in sel_adder:
        adder_number += 1

adder_list = []
adder_type = []
with open('adder_selection.txt') as next_adder:
    for line in next_adder:
        adder_list.append(line.split()[2].strip())
        adder_type.append(line.split()[0].strip())


with open('dut_prev.py','w') as out_file:
    out_file.write('from amaranth import *\nfrom amaranth.cli import main\n')
    for adders in adder_list:
        out_file.write('from built_adder'+adders+' import Adder'+adders+'\n')


count = 0
sub_string = ''
count_lim = len(adder_list)
with open('dut_base.py','r') as dut_original:
    with open('dut_prev.py','a') as dut_final:
        for idx,line in enumerate(dut_original):
            area=re.search('[aA][dD][dD][eE][rR].*\s+=',line)
            if(area and (count < count_lim)):
                sub_string = re.sub(r'Adder\s*\(','Adder'+str(adder_list[count])+'(',line)
                dut_final.write(sub_string)
                count += 1
            else:
                dut_final.write(line)

#eliminar los import repetidos#
lines_seen = set()
with open("dut.py", 'w') as dut_file:
    with open("dut_prev.py", 'r') as prev_file:
        for line in prev_file:
            if line not in lines_seen:
                dut_file.write(line)
                lines_seen.add(line)

os.system("rm dut_prev.py")
