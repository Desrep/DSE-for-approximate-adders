		##############this script automatically builds a lower-k bits LOA##########################
		
import re
import os
		
os.system("rm built_adder*")
		############get next adder, from design exploration algo###########################
with open('adder_selection.txt') as next_adder:
    for line in next_adder:
        adder_type = line.split()[0].strip()
        lower_bits = line.split()[1].strip() 
        adder_number = line.split()[2].strip()
        record = 0
		
		
		####################create the adder to use#########################################
        with open('built_adder'+adder_number+'.py','w') as out_file:
            out_file.write('from amaranth import *\nfrom amaranth.cli import main\n')
		
		##############from the database, get the selected adder and output the adder file(python)##########    
        with open('adder.py') as adder_db:
            for line,data in enumerate(adder_db):
                if(record == 1):
                    with open('built_adder'+adder_number+'.py','a') as out_file:
                        if(data.strip()=="self.k = 8"):
                            out_file.write(data.replace("8",lower_bits)+"\n")
                        else:
                            out_file.write(data)
		
                if((data.find(adder_type+lower_bits) != -1)or(data.find(adder_type+'K')!= -1)):
                    record = 1
                    with open('built_adder'+adder_number+'.py','a') as out_file:
                        out_file.write('class Adder'+adder_number+'(Elaboratable):\n')
		
                if((record == 1)and(data.find('return m')!=-1)):
                    record = 0
