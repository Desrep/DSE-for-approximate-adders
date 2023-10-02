`include "up_counter.v" 
module tb();
reg clk;
reg en;
reg count; 
reg rst;


initial begin
clk=0;
rst=1;
en=0;
#1
en=1;
rst=0;
#150 
$finish;
end

always #5 clk = ~clk;

top c1(.clk(clk),.en(en),.rst(rst));

initial begin
$dumpfile("wave.vcd");
$dumpvars(0);
end



endmodule
