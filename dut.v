/* Generated by Amaranth Yosys 0.25 (PyPI ver 0.25.0.0.post77, git sha1 e02b7f64b) */

(* \amaranth.hierarchy  = "top.adder1" *)
(* generator = "Amaranth" *)
module adder1(a1, b1, o1);
  (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *)
  wire [8:0] \$1 ;
  (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *)
  wire [7:0] \$2 ;
  (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *)
  wire \$4 ;
  (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *)
  wire [8:0] \$6 ;
  (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:24" *)
  wire \$8 ;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:9" *)
  input [7:0] a1;
  wire [7:0] a1;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:11" *)
  input [7:0] b1;
  wire [7:0] b1;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:13" *)
  output [8:0] o1;
  wire [8:0] o1;
  assign \$2  = a1[7:1] + (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *) b1[7:1];
  assign \$4  = a1[0] & (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *) b1[0];
  assign \$6  = \$2  + (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *) \$4 ;
  assign \$8  = a1[0] | (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:24" *) b1[0];
  assign \$1  = \$6 ;
  assign o1[0] = \$8 ;
  assign o1[8:1] = \$6 [7:0];
endmodule

(* \amaranth.hierarchy  = "top.adder2" *)
(* generator = "Amaranth" *)
module adder2(a2, b2, o2);
  (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *)
  wire [8:0] \$1 ;
  (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *)
  wire [7:0] \$2 ;
  (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *)
  wire \$4 ;
  (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *)
  wire [8:0] \$6 ;
  (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:24" *)
  wire \$8 ;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:10" *)
  input [7:0] a2;
  wire [7:0] a2;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:12" *)
  input [7:0] b2;
  wire [7:0] b2;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:14" *)
  output [8:0] o2;
  wire [8:0] o2;
  assign \$2  = a2[7:1] + (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *) b2[7:1];
  assign \$4  = a2[0] & (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *) b2[0];
  assign \$6  = \$2  + (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:22" *) \$4 ;
  assign \$8  = a2[0] | (* src = "/home/simuse/Desktop/Amaranth/test/built_adder.py:24" *) b2[0];
  assign \$1  = \$6 ;
  assign o2[0] = \$8 ;
  assign o2[8:1] = \$6 [7:0];
endmodule

(* \amaranth.hierarchy  = "top" *)
(* top =  1  *)
(* generator = "Amaranth" *)
module top(b1, a2, b2, o, a1);
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:23" *)
  wire [9:0] \$1 ;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:9" *)
  input [7:0] a1;
  wire [7:0] a1;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:10" *)
  input [7:0] a2;
  wire [7:0] a2;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:13" *)
  wire [8:0] adder1_o1;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:14" *)
  wire [8:0] adder2_o2;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:11" *)
  input [7:0] b1;
  wire [7:0] b1;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:12" *)
  input [7:0] b2;
  wire [7:0] b2;
  (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:8" *)
  output [9:0] o;
  wire [9:0] o;
  assign \$1  = adder1_o1 + (* src = "/home/simuse/Desktop/Amaranth/test/dut.py:23" *) adder2_o2;
  adder1 adder1 (
    .a1(a1),
    .b1(b1),
    .o1(adder1_o1)
  );
  adder2 adder2 (
    .a2(a2),
    .b2(b2),
    .o2(adder2_o2)
  );
  assign o = \$1 ;
endmodule
