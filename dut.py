from amaranth import *
from amaranth.cli import main
from built_adder import Adder


class dut(Elaboratable):
    def __init__(self, width):
        self.o  = Signal(width+2)
        self.a1 = Signal(width)
        self.a2 = Signal(width)
        self.b1 = Signal(width)
        self.b2 = Signal(width)
        self.o1 = Signal(width+1)
        self.o2 = Signal(width+1)


    def elaborate(self, platform):
        m = Module()
        

        adder1 = m.submodules.adder1 = Adder(8,self.a1,self.b1,self.o1)
        adder2 = m.submodules.adder2 = Adder(8,self.a2,self.b2,self.o2)
        m.d.comb += self.o.eq(self.o1+self.o2)
        
        
        return m





