`include "adder3.v" 
module tb();
reg [7:0] a;
reg [7:0] b; 
wire [8:0] o;


initial begin
a=1;
b=3;
#10 
$finish;
end


top a1(.a(a),.b(b),.o(o));

initial begin
$dumpfile("add3.vcd");
$dumpvars(0);
end



endmodule
