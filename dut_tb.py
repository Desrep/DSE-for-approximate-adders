from amaranth.sim import Simulator, Settle, Delay
from dut import dut
import random


dut = dut(32)
upper_limit = 2048

random.seed(1)
def bench():
    for i in range(1000):
        yield dut.a1.eq(random.randint(0,upper_limit))
        yield dut.a2.eq(random.randint(0,upper_limit))
        yield dut.a3.eq(random.randint(0,upper_limit))
        yield dut.a4.eq(random.randint(0,upper_limit))
        yield dut.a5.eq(random.randint(0,upper_limit))
        yield dut.a6.eq(random.randint(0,upper_limit))
        yield dut.a7.eq(random.randint(0,upper_limit))
        yield dut.a8.eq(random.randint(0,upper_limit))
        yield dut.a9.eq(random.randint(0,upper_limit))
        yield Delay(1e-9)
        yield Settle()


sim1 = Simulator(dut)

sim1.add_process(bench)

with sim1.write_vcd("dut.vcd"):
    sim1.run()

