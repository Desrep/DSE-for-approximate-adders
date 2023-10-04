import re
import os

with open('adder_selection.txt') as next_adder:
    adder_type = next_adder.readline().strip()

record = 0
os.system("rm built_adder.py")

with open('built_adder.py','w') as out_file:
    out_file.write('from amaranth import *\nfrom amaranth.cli import main\n')
with open('adder.py') as adder_db:
    for line,data in enumerate(adder_db):
        if(record == 1):
            with open('built_adder.py','a') as out_file:
                out_file.write(data+"\n")

        if(data.find(adder_type) != -1):
            record = 1
            with open('built_adder.py','a') as out_file:
                out_file.write("class Adder(Elaboratable):\n")

        if((record == 1)and(data.find('return m')!=-1)):
            record = 0
            


