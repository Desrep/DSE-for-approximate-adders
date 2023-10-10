from amaranth.sim import Simulator, Settle, Delay
from built_adder import Adder
from amaranth import *

a = Signal(8)
b= Signal(8)
o = Signal(9)

dut = Adder(8,a,b,o)


def bench():
    yield dut.a.eq(5)
    yield dut.b.eq(3)
    yield Delay(1e-9)
    yield Settle()


sim1 = Simulator(dut)

sim1.add_process(bench)

with sim1.write_vcd("add_test.vcd"):
    sim1.run()

