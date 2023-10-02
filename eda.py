import os
import csv
os.system("cd /home/simuse/OpenLane/")
os.system("docker exec  0c78d59bf5bd ./flow.tcl -design adder")
os.system("cd /home/simuse/Desktop/Amaranth/test")
with open ('/home/simuse/OpenLane/designs/adder/runs/RUN_2023.10.02_05.29.07/reports/metrics.csv') as metrics:
    metricreader = csv.DictReader(metrics)
    for row in metricreader:
        print(row['wns'],row['CoreArea_um^2'],row['wire_length'])
with open ('metrics_output.csv','w') as metric_output:
    metric_output.write("wns, area, wire_length\n"+row['wns']+", "+row['CoreArea_um^2']+", "+row['wire_length'])

