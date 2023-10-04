import os
import csv
import re
open_lane_path = '/home/simuse/OpenLane/'

os.system("docker ps > containerid.txt")
docker_id = ''

with open('containerid.txt') as dockid:
    for line,data in enumerate(dockid):
        if(line == 1):
            docker_id = data.split()[0]
print(docker_id)

designs = ['dut.v']
this_tag = 'current_run'
os.system("rm metrics_output.csv")
with open ('metrics_output.csv','w') as metric_output:
    metric_output.write("type, area, power, delay\n")
os.system("rm -r "+open_lane_path+"designs/dut/runs/"+this_tag)
acc_count = 0
for dut in designs:
    print(dut)
    os.system("cp "+dut+" "+open_lane_path+"designs/dut/src/top.v")
    #os.system("cd /home/simuse/OpenLane/")
    os.system("docker exec "+docker_id+" ./flow.tcl -design dut -overwrite -tag "+this_tag)
    os.system("cd /home/simuse/Desktop/Amaranth/test")
    with open (open_lane_path+'designs/dut/runs/'+this_tag+'/reports/signoff/24-rcx_sta.area.rpt') as area_file:
        for data in area_file:
            if(data.find('Design area')!=-1):
                area=re.sub(r'Design area (\S+).*',r'\1',data)
                area = area.strip()
    with open (open_lane_path+'designs/dut/runs/'+this_tag+'/reports/signoff/24-rcx_sta.power.rpt') as pow_file:
        for data in pow_file:
            if(data.find('Total')!=-1):
                power = data.split()[-2]
    with open (open_lane_path+'designs/dut/runs/'+this_tag+'/reports/signoff/24-rcx_sta.max.rpt') as delay_file:
        for data in delay_file:
            if(data.find('data arrival time')!=-1):
                if(acc_count == 0):    
                    delay = data.split()[0]
                    acc_count += 1
        acc_count = 0
    with open ('metrics_output.csv','a') as metric_output:
        metric_output.write(dut.strip(".v")+", "+area+", "+power+", "+delay.strip("-")+"\n")

