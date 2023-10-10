###This is the database for approximate adders###################################################

from amaranth import *
from amaranth.cli import main

#######LOA for k-lower bits############################
class Adder_LOAK(Elaboratable):
    def __init__(self, width,a,b,o):

        self.a   = a
        self.b   = b
        self.o = o
        self.k = 8 

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.o[self.k:].eq(self.a[self.k:] + self.b[self.k:]+(self.a[self.k-1]&self.b[self.k-1]))
        for bit in range(self.k-1):
            m.d.comb += self.o[bit].eq(self.a[bit]|self.b[bit])
        return m


##################Standard adder with no approximation##################
class Adder_STD0(Elaboratable):
    def __init__(self, width,a,b,o):

        self.a   = a
        self.b   = b
        self.o = o


    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.o.eq(self.a + self.b)
        return m






