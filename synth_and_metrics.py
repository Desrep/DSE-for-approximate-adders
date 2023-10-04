import os
import csv
import re
open_lane_path = '/home/simuse/OpenLane/'

########get the docker container id################
os.system("docker ps > containerid.txt")
docker_id = ''

with open('containerid.txt') as dockid:
    for line,data in enumerate(dockid):
        if(line == 1):
            docker_id = data.split()[0]
###########################################################


############################prepare directory and run###############
designs = ['dut.v']
this_tag = 'current_run'
os.system("rm metrics_output.csv")
with open ('metrics_output.csv','w') as metric_output:
    metric_output.write("type, area, power, delay\n")
os.system("rm -r "+open_lane_path+"designs/dut/runs/"+this_tag)
acc_count = 0

###############copy design to openlane dir and run synthesis#############################
for dut in designs:
    os.system("cp "+dut+" "+open_lane_path+"designs/dut/src/top.v")
    os.system("docker exec "+docker_id+" ./flow.tcl -design dut -overwrite -tag "+this_tag)
    
##################open reports and get the date#############################################################
   #area#
    with open (open_lane_path+'designs/dut/runs/'+this_tag+'/reports/signoff/24-rcx_sta.area.rpt') as area_file:
        for data in area_file:
            if(data.find('Design area')!=-1):
                area=re.sub(r'Design area (\S+).*',r'\1',data)
                area = area.strip()
   #power#
    with open (open_lane_path+'designs/dut/runs/'+this_tag+'/reports/signoff/24-rcx_sta.power.rpt') as pow_file:
        for data in pow_file:
            if(data.find('Total')!=-1):
                power = data.split()[-2]

   #delay, grabs the highest delay#
    with open (open_lane_path+'designs/dut/runs/'+this_tag+'/reports/signoff/24-rcx_sta.max.rpt') as delay_file:
        for data in delay_file:
            if(data.find('data arrival time')!=-1):
                if(acc_count == 0):    
                    delay = data.split()[0]
                    acc_count += 1
        acc_count = 0

##################output  metrics for current design as file###########################
    with open ('metrics_output.csv','a') as metric_output:
        metric_output.write(dut.strip(".v")+", "+area+", "+power+", "+delay.strip("-")+"\n")

