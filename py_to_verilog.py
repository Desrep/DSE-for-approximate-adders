from amaranth.back import verilog
from dut import *

dut_design = dut(8)

with open("dut.v", "w") as f:
    f.write(verilog.convert(dut_design, ports=[dut_design.a1, dut_design.b1,dut_design.a2,dut_design.b2,dut_design.o]))


