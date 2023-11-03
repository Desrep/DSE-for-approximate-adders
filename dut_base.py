class dut(Elaboratable):
    def __init__(self, width=32):
        self.o  = Signal(width)
        self.a1 = Signal(width)
        self.a2 = Signal(width)
        self.a3 = Signal(width)
        self.a4 = Signal(width)
        self.a5 = Signal(width)
        self.a6 = Signal(width)
        self.a7 = Signal(width)
        self.a8 = Signal(width)
        self.a9 = Signal(width)
        self.o1 = Signal(width)
        self.o2 = Signal(width)
        self.o3 = Signal(width)
        self.o4 = Signal(width)
        self.o5 = Signal(width)
        self.o6 = Signal(width)
        self.o7 = Signal(width)
        self.o8 = Signal(width)
        self.a2p = Signal(width)
        self.a4p = Signal(width)
        self.a5p = Signal(width)
        self.a6p = Signal(width)
        self.a8p = Signal(width)
        self.width = width


    def elaborate(self, platform):
        m = Module()
        
        
        m.d.comb += self.a2.eq(self.a2p <<1)
        m.d.comb += self.a4.eq(self.a4p <<1)
        m.d.comb += self.a5.eq(self.a5p <<2)
        m.d.comb += self.a6.eq(self.a6p <<1)
        m.d.comb += self.a8.eq(self.a8p <<1)
        adder1 = m.submodules.adder1 = Adder(self.width,self.a1,self.a2,self.o1)
        adder2 = m.submodules.adder2 = Adder(self.width,self.a3,self.a4,self.o2)
        adder3 = m.submodules.adder3 = Adder(self.width,self.a5,self.a6,self.o3)
        adder4 = m.submodules.adder4 = Adder(self.width,self.a7,self.a8,self.o4)
        adder5 = m.submodules.adder5 = Adder(self.width,self.o1,self.o2,self.o5)
        adder6 = m.submodules.adder6 = Adder(self.width,self.o3,self.o4,self.o6)
        adder7 = m.submodules.adder7 = Adder(self.width,self.o5,self.o6,self.o7)
        adder8 = m.submodules.adder8 = Adder(self.width,self.o7,self.a9,self.o8)
        m.d.comb += self.o.eq(self.o8 >> 4)
        
        
        return m





