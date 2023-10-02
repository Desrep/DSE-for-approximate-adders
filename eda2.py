import os
import csv

designs = ['adder.v','adder1.v','adder2.v','adder3.v']
this_tag = 'current_run'
os.system("rm metrics_output.csv")
os.system("rm -r /home/simuse/OpenLane/designs/adder/runs/"+this_tag)
for adder in designs:
    print(adder)
    os.system("cp "+adder+" /home/simuse/OpenLane/designs/adder/src/top.v")
    #os.system("cd /home/simuse/OpenLane/")
    os.system("docker exec  0c78d59bf5bd ./flow.tcl -design adder -overwrite -tag "+this_tag)
    os.system("cd /home/simuse/Desktop/Amaranth/test")
    with open ('/home/simuse/OpenLane/designs/adder/runs/'+this_tag+'/reports/metrics.csv') as metrics:
        metricreader = csv.DictReader(metrics)
        for row in metricreader:
            print(row['wns'],row['CoreArea_um^2'],row['wire_length'])
    with open ('metrics_output.csv','a') as metric_output:
        metric_output.write("wns, area, wire_length\n"+row['wns']+", "+row['CoreArea_um^2']+", "+row['wire_length']+"\n")

