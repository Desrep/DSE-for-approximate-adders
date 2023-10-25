from amaranth.sim import Simulator, Settle, Delay
from dut import dut
import random


dut = dut(32)

random.seed(1)
def bench():
    for i in range(100):
        yield dut.a1.eq(random.randint(0,1000000))
        yield dut.b1.eq(random.randint(0,1000000))
        yield dut.a2.eq(random.randint(0,1000000))
        yield dut.b2.eq(random.randint(0,1000000))
        yield Delay(1e-9)
        yield Settle()


sim1 = Simulator(dut)

sim1.add_process(bench)

with sim1.write_vcd("dut.vcd"):
    sim1.run()

