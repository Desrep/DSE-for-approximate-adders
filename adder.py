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
        for bit in range(self.k):
            m.d.comb += self.o[bit].eq(self.a[bit]|self.b[bit])
        
        m.d.comb += self.o[self.k:].eq(self.a[self.k:] + self.b[self.k:]+(self.a[self.k-1]&self.b[self.k-1]))
        return m

##################### Copy adder for k-lower bits##########################
######################cpies the k lower bits from operand b################

class Adder_COPYK(Elaboratable):
    def __init__(self, width,a,b,o):

        self.a   = a
        self.b   = b
        self.o = o
        self.k = 8

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.o[:self.k].eq(self.b[:self.k])
        m.d.comb += self.o[self.k:].eq(self.a[self.k:] + self.b[self.k:])
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

#######LOWA for k-lower bits, this must be replaced by truncation############################
class Adder_LOWAK(Elaboratable):
    def __init__(self, width,a,b,o):

        self.a   = a
        self.b   = b
        self.o = o
        self.k = 8

    def elaborate(self, platform):
        m = Module()
        for bit in range(self.k):
            m.d.comb += self.o[bit].eq(self.a[bit]|self.b[bit])

        m.d.comb += self.o[self.k:].eq(self.a[self.k:] + self.b[self.k:])
        return m

#################Truncate Adder, replace k-lsbs with 0s#############################
class Adder_TRUNK(Elaboratable):
    def __init__(self, width,a,b,o):

        self.a   = a
        self.b   = b
        self.o = o
        self.k = 8

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.o[:self.k].eq(0)
        m.d.comb += self.o[self.k:].eq(self.a[self.k:] + self.b[self.k:])
        return m
###################################################################################



