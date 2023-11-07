from amaranth import *
from amaranth.cli import main
class Adder8(Elaboratable):
    def __init__(self, width,a,b,o):

        self.a   = a
        self.b   = b
        self.o = o


    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.o.eq(self.a + self.b)
        return m
