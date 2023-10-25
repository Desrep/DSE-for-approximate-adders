import re
import os

output_var = "o"
os.system("rm output_values.txt")
catch = 0
interval = 0
prev_value = ""
with open ("dut.vcd","r") as vcd:
    for line in vcd:
        found = line.find(output_var+' $end')
        if(found != -1):
            mark = line.split()[-3]
            catch = 1
        if(catch): #si se encuentra la variable extraer los datos
            if(list(line.split()[0])[0]=='#' ):# si el valor se repite volver a copiarlo
                if(interval == 1):
                    interval = 0
                    with open ("output_values.txt","a") as val_rep:
                        val_rep.write(prev_value+"\n")
                else: 
                    interval = 1

            if(line.split()[-1] == mark):#extraer
                interval = 0
                with open ("output_values.txt","a") as val_rep:
                    prev_value = line.split()[0].strip("b")
                    val_rep.write(line.split()[0].strip("b")+"\n")

