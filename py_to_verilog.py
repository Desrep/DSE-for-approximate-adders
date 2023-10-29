from amaranth.back import verilog
from dut import *

###################convert design from python to verilog######################################

dut_design = dut(32)

with open("dut.v", "w") as f:
    f.write(verilog.convert(dut_design, ports=[dut_design.a1, dut_design.a2,dut_design.a3,dut_design.a4,dut_design.a5,dut_design.a6,dut_design.a7,dut_design.a8,dut_design.a9,dut_design.o]))


