import os
import csv
import re

designs = ['adder.v','adder1.v','adder2.v','adder3.v']
this_tag = 'current_run'
os.system("rm metrics_output.csv")
with open ('metrics_output.csv','w') as metric_output:
    metric_output.write("tipo, area, power, delay\n")
os.system("rm -r /home/simuse/OpenLane/designs/adder/runs/"+this_tag)
for adder in designs:
    print(adder)
    os.system("cp "+adder+" /home/simuse/OpenLane/designs/adder/src/top.v")
    #os.system("cd /home/simuse/OpenLane/")
    os.system("docker exec  0c78d59bf5bd ./flow.tcl -design adder -overwrite -tag "+this_tag)
    os.system("cd /home/simuse/Desktop/Amaranth/test")
    with open ('/home/simuse/OpenLane/designs/adder/runs/'+this_tag+'/reports/signoff/24-rcx_sta.area.rpt') as area_file:
        for data in area_file:
            if(data.find('Design area')!=-1):
                area=re.sub(r'Design area (\S+).*',r'\1',data)
                area = area.strip()
    with open ('/home/simuse/OpenLane/designs/adder/runs/'+this_tag+'/reports/signoff/24-rcx_sta.power.rpt') as pow_file:
        for data in pow_file:
            if(data.find('Total')!=-1):
                power = data.split()[-2]
    with open ('/home/simuse/OpenLane/designs/adder/runs/'+this_tag+'/reports/signoff/24-rcx_sta.max.rpt') as delay_file:
        for data in delay_file:
            if(data.find('data arrival time')!=-1):
                delay = data.split()[0]
    with open ('metrics_output.csv','a') as metric_output:
        metric_output.write(adder.strip(".v")+", "+area+", "+power+", "+delay.strip("-")+"\n")

