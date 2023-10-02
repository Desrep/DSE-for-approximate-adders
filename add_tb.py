from amaranth.sim import Simulator, Settle, Delay
from adder import Adder, Adder_LOA1, Adder_LOA2, Adder_LOA3


add_1 = Adder_LOA1(8)
add_2 = Adder_LOA2(8)
add_3 = Adder_LOA3(8)
add = Adder(8)


def bench():
    yield add_1.a.eq(1)
    yield add_1.b.eq(3)

    yield add_2.a.eq(1)
    yield add_2.b.eq(3)

    yield add_3.a.eq(1)
    yield add_3.b.eq(3)

    yield add.a.eq(1)
    yield add.b.eq(3)
    yield Delay(1e-9)
    yield Settle()


sim1 = Simulator(add_1)
sim2 = Simulator(add_2)
sim3 = Simulator(add_3)
sim = Simulator(add)

sim.add_process(bench)
sim2.add_process(bench)
sim3.add_process(bench)
sim1.add_process(bench)

with sim1.write_vcd("adder1.vcd"):
    sim1.run()
with sim2.write_vcd("adder2.vcd"):
    sim2.run()
with sim3.write_vcd("adder3.vcd"):
    sim3.run()
with sim.write_vcd("adder.vcd"):

    sim.run()

