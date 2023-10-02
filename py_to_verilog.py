from amaranth.back import verilog
from up_counter import *
from adder import *

top_add= Adder(8)
top_add1 = Adder_LOA1(8)
top_add2 = Adder_LOA2(8)
top_add3 = Adder_LOA3(8)

with open("adder.v", "w") as f:
    f.write(verilog.convert(top_add, ports=[top_add.a, top_add.b,top_add.o]))

with open("adder1.v", "w") as f:
    f.write(verilog.convert(top_add1, ports=[top_add1.a, top_add1.b,top_add1.o]))

with open("adder2.v", "w") as f:
    f.write(verilog.convert(top_add2, ports=[top_add2.a, top_add2.b,top_add2.o]))

with open("adder3.v", "w") as f:
    f.write(verilog.convert(top_add3, ports=[top_add3.a, top_add3.b,top_add3.o]))

