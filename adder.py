from amaranth import *
from amaranth.cli import main

class Adder_LOA1(Elaboratable):
    def __init__(self, width):
        self.a   = Signal(width)
        self.b   = Signal(width)
        self.o   = Signal(width+1)

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.o[1:].eq(self.a[1:] + self.b[1:]+(self.a[0]&self.b[0]))
        m.d.comb += self.o[0].eq(self.a[0]|self.b[0])
        return m




class Adder(Elaboratable):
    def __init__(self, width):
        self.a   = Signal(width)
        self.b   = Signal(width)
        self.o   = Signal(width+1)

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.o.eq(self.a + self.b)
        return m


class Adder_LOA2(Elaboratable):
    def __init__(self, width):
        self.a   = Signal(width)
        self.b   = Signal(width)
        self.o   = Signal(width+1)

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.o[2:].eq(self.a[2:] + self.b[2:]+(self.a[1]&self.b[1]))
        m.d.comb += self.o[0].eq(self.a[0]|self.b[0])
        m.d.comb += self.o[1].eq(self.a[1]|self.b[1])
        return m

class Adder_LOA3(Elaboratable):
    def __init__(self, width):
        self.a   = Signal(width)
        self.b   = Signal(width)
        self.o   = Signal(width+1)

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.o[3:].eq(self.a[3:] + self.b[3:]+(self.a[2]&self.b[2]))
        m.d.comb += self.o[0].eq(self.a[0]|self.b[0])
        m.d.comb += self.o[1].eq(self.a[1]|self.b[1])
        m.d.comb += self.o[2].eq(self.a[2]|self.b[2])
        return m




