# DSE for approximate adders
This is a small project to try to obtain a DSE method for replacing adders by approximate adders. It uses Amaranth to start (the initial DUT is an Amaranth description) and to get a measure of the error using it's simulation engine, it uses OpenLane for the synthesis in order to obtain metrics for comparison (area, power, delay).

The goal of the exploration is to try to obtain a pareto front based in a measure of the error (a MAE) between the approximate DUT and the original dut and a measure of the performance (in this case this is the product of area*delay).

For example if the DUT (dut_base.py) has 3 adders then the exploration would do something like the following:

Try one adder as a LOA with 3 approximate bits, other as a copy approximate adder with 1 approximate bit and the other as a standard one (with no approximation), save the results and try another one, the original dut would use three standard adders and this would be the reference to calculate the accuracy.

The branch exhaustive_search is just a bunch of fors to run and exhaustive search to obtain reference data, this run would never complete for a dut with a modest amount of adders so the idea is just to gather enough data for comparison.
The branch product_implementation is the final state of the project, it uses a genetic alghorithm from PYMOO to try to find the pareto front. The last configuration used obtains some interesting results but it won't get the pareto front, the current measures are accuracy vs delay*area so it is a 2 dimensional problem (this can be easily modified if needed).

To use this change the open_lane_path in synth_and_metrics.py, a container of OpenLane has to be running in a different terminal. Amaranth is also needed for the scripts to run, the OpenLane commit used is the tag 2022.11.19


## adder.py
Contains the different approximate adders to use.
## dut_builder.py
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
## dut_tb.py
This is the Amaranth testbench used to obtain the data for the calculation of the error (the MAE) between the approximation and the original dut.
## out_extract.py
This script takes the dut.vcd file after simulation and extracts the data. It generates a file called output_values.txt used by eda_flow.py.
## eda_flow.py 
This is the search flow, it runs all the scripts in order and performs the search algorithm, it generates the metrics for accuracy (the first run is the reference run without approximation) and calculates the MAE, it 
generates an output file named design_space_exploration.txt with all the results. It also generates a file called design_space.txt which is used by some of the other scripts (like adder_builder.py).
