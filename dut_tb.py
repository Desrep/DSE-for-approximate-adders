from amaranth.sim import Simulator, Settle, Delay
from dut import dut


dut = dut(8)


def bench():
    yield dut.a1.eq(5)
    yield dut.b1.eq(3)
    yield dut.a2.eq(0)
    yield dut.b2.eq(1)
    yield Delay(1e-9)
    yield Settle()


sim1 = Simulator(dut)

sim1.add_process(bench)

with sim1.write_vcd("dut.vcd"):
    sim1.run()

