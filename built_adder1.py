from amaranth import *
from amaranth.cli import main
class Adder1(Elaboratable):
    def __init__(self, width,a,b,o):

        self.a   = a
        self.b   = b
        self.o = o
        self.k = 1


    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.o[:self.k].eq(self.b[:self.k])
        m.d.comb += self.o[self.k:].eq(self.a[self.k:] + self.b[self.k:])
        return m
