##############this script automatically builds a lower-k bits LOA##########################

import re
import os

############get next adder, from design exploration algo###########################
with open('adder_selection.txt') as next_adder:
    line = next_adder.readline()
    adder_type = line.split()[0].strip()
    lower_bits = line.split()[1].strip() 

record = 0
os.system("rm built_adder.py")


####################create the adder to use#########################################
with open('built_adder.py','w') as out_file:
    out_file.write('from amaranth import *\nfrom amaranth.cli import main\n')

##############from the database, get the selected adder and output the adder file(python)##########    
with open('adder.py') as adder_db:
    for line,data in enumerate(adder_db):
        if(record == 1):
            with open('built_adder.py','a') as out_file:
                if(data.strip()=="self.k = 8"):
                    out_file.write(data.replace("8",lower_bits)+"\n")
                else:
                    out_file.write(data+"\n")

        if((data.find(adder_type+lower_bits) != -1)|(data.find(adder_type+'K')!= -1)):
            record = 1
            with open('built_adder.py','a') as out_file:
                out_file.write("class Adder(Elaboratable):\n")

        if((record == 1)and(data.find('return m')!=-1)):
            record = 0
            


