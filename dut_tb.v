`include "dut.v" 
module tb();
reg [7:0] a1,b1,a2,b2;
wire [9:0] o;


initial begin
a1=5;
b1=3;
a2=1;
b2=0;
#10 
$finish;
end


top dut1(.a1(a1),.b1(b1),.a2(a2),.b2(b2),.o(o));

initial begin
$dumpfile("dut_verilog.vcd");
$dumpvars(0);
end



endmodule
