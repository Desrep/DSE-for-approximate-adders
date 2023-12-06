# eda_proyecto
To use this change the open_lane_path in synth_and_metrics.py
## adder.py
Contains the different approximate adders to use.
##dut_builder.py
This script grabs the original dut (dut_base.py) and replaces the adders by the configuration provided by the search algorithm (for example, it imports the adders created by adder_builder.py).
It outputs dut.py
## adder_builder.py
This script receives the adder configuration to use in the next run, provided by the search algorithm, and creates the necessary adders to be imported into the DUT.
For example if there are 4 adders in the DUT it will generate 4 files named built_adder1.py, built_adder2.py... built_adder4.py.
## py_to_verilog.py
Takes dut.py as input and produces the verilog implementation.
## synth_and_metrics.py
This script takes the dut.v file, copies it into the appropiate OpenLane directory and runs the synthesis, it also extracts the required metrics (delay, power, area).
It generates a file named metrics_output.csv
##dut_tb.py
This is the Amaranth testbench used to obtain the data for the calculation of the error (the MAE) between the approximation and the original dut.
##out_extract.py
This script takes the dut.vcd file after simulation and extracts the data. It generates a file called output_values.txt used by eda_flow.py.
## eda_flow.py 
This is the search flow, it runs all the scripts in order and performs the search algorithm, it generates the metrics for accuracy (the first run is the reference run without approximation) and calculates the MAE, it 
generates an output file named design_space_exploration.txt with all the results. It also generates a file called design_space.txt which is used by some of the other scripts (like adder_builder.py).
