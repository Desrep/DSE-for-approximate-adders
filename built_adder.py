from amaranth import *
from amaranth.cli import main
class Adder(Elaboratable):
    def __init__(self, width,a,b,o):



        self.a   = a

        self.b   = b

        self.o = o





    def elaborate(self, platform):

        m = Module()

        m.d.comb += self.o[3:].eq(self.a[3:] + self.b[3:]+(self.a[2]&self.b[2]))

        m.d.comb += self.o[0].eq(self.a[0]|self.b[0])

        m.d.comb += self.o[1].eq(self.a[1]|self.b[1])

        m.d.comb += self.o[2].eq(self.a[2]|self.b[2])

        return m

