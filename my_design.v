/* Machine-generated using Migen */
module top(
	input sys_clk,
    input sys_rst,
    input start,
    input [1023:0] dividend,
    input [1023:0] divisor,
    output [1023:0] quotient,
    output [1023:0] remainder,
    output done,
    output ready
);


reg start = 1'd0;
reg [1023:0] quotient0 = 1024'd0;
reg [1023:0] remainder0 = 1024'd0;
wire ready;
reg done = 1'd0;


reg [15:0] count = 16'd0;
reg [1024:0] remainder1 = 1025'd0;
reg [1023:0] quotient1 = 1024'd0;
reg [1023:0] dividend_reg = 1024'd0;
reg [1023:0] divisor_reg = 1024'd0;
reg is_ongoing;
reg [1:0] state = 2'd0;
reg [1:0] next_state;
reg done_next_value0;
reg done_next_value_ce0;
reg [1023:0] dividend_reg_next_value1;
reg dividend_reg_next_value_ce1;
reg [1023:0] divisor_reg_next_value2;
reg divisor_reg_next_value_ce2;
reg [1024:0] remainder1_next_value3;
reg remainder1_next_value_ce3;
reg [1023:0] quotient1_next_value4;
reg quotient1_next_value_ce4;
reg [15:0] count_next_value5;
reg count_next_value_ce5;
reg [1023:0] quotient0_next_value6;
reg quotient0_next_value_ce6;
reg [1023:0] remainder0_next_value7;
reg remainder0_next_value_ce7;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on

assign ready = is_ongoing;

// synthesis translate_off
reg dummy_d;
// synthesis translate_on
always @(*) begin
	is_ongoing <= 1'd0;
	next_state <= 2'd0;
	done_next_value0 <= 1'd0;
	done_next_value_ce0 <= 1'd0;
	dividend_reg_next_value1 <= 1024'd0;
	dividend_reg_next_value_ce1 <= 1'd0;
	divisor_reg_next_value2 <= 1024'd0;
	divisor_reg_next_value_ce2 <= 1'd0;
	remainder1_next_value3 <= 1025'd0;
	remainder1_next_value_ce3 <= 1'd0;
	quotient1_next_value4 <= 1024'd0;
	quotient1_next_value_ce4 <= 1'd0;
	count_next_value5 <= 16'd0;
	count_next_value_ce5 <= 1'd0;
	quotient0_next_value6 <= 1024'd0;
	quotient0_next_value_ce6 <= 1'd0;
	remainder0_next_value7 <= 1024'd0;
	remainder0_next_value_ce7 <= 1'd0;
	next_state <= state;
	case (state)
		1'd1: begin
			remainder1_next_value3 <= ((remainder1 <<< 1'd1) | ((dividend_reg >>> 10'd1023) & 1'd1));
			remainder1_next_value_ce3 <= 1'd1;
			dividend_reg_next_value1 <= (dividend_reg <<< 1'd1);
			dividend_reg_next_value_ce1 <= 1'd1;
			next_state <= 2'd2;
		end
		2'd2: begin
			if ((remainder1 >= divisor_reg)) begin
				remainder1_next_value3 <= (remainder1 - divisor_reg);
				remainder1_next_value_ce3 <= 1'd1;
				quotient1_next_value4 <= ((quotient1 <<< 1'd1) | 1'd1);
				quotient1_next_value_ce4 <= 1'd1;
			end else begin
				quotient1_next_value4 <= (quotient1 <<< 1'd1);
				quotient1_next_value_ce4 <= 1'd1;
			end
			count_next_value5 <= (count + 1'd1);
			count_next_value_ce5 <= 1'd1;
			if ((count == 10'd1023)) begin
				next_state <= 2'd3;
			end else begin
				next_state <= 1'd1;
			end
		end
		2'd3: begin
			quotient0_next_value6 <= quotient1;
			quotient0_next_value_ce6 <= 1'd1;
			remainder0_next_value7 <= remainder1[1023:0];
			remainder0_next_value_ce7 <= 1'd1;
			done_next_value0 <= 1'd1;
			done_next_value_ce0 <= 1'd1;
			next_state <= 1'd0;
		end
		default: begin
			is_ongoing <= 1'd1;
			done_next_value0 <= 1'd0;
			done_next_value_ce0 <= 1'd1;
			if (start) begin
				dividend_reg_next_value1 <= dividend;
				dividend_reg_next_value_ce1 <= 1'd1;
				divisor_reg_next_value2 <= divisor;
				divisor_reg_next_value_ce2 <= 1'd1;
				remainder1_next_value3 <= 1'd0;
				remainder1_next_value_ce3 <= 1'd1;
				quotient1_next_value4 <= 1'd0;
				quotient1_next_value_ce4 <= 1'd1;
				count_next_value5 <= 1'd0;
				count_next_value_ce5 <= 1'd1;
				next_state <= 1'd1;
			end
		end
	endcase
// synthesis translate_off
	dummy_d <= dummy_s;
// synthesis translate_on
end

always @(posedge sys_clk) begin
	state <= next_state;
	if (done_next_value_ce0) begin
		done <= done_next_value0;
	end
	if (dividend_reg_next_value_ce1) begin
		dividend_reg <= dividend_reg_next_value1;
	end
	if (divisor_reg_next_value_ce2) begin
		divisor_reg <= divisor_reg_next_value2;
	end
	if (remainder1_next_value_ce3) begin
		remainder1 <= remainder1_next_value3;
	end
	if (quotient1_next_value_ce4) begin
		quotient1 <= quotient1_next_value4;
	end
	if (count_next_value_ce5) begin
		count <= count_next_value5;
	end
	if (quotient0_next_value_ce6) begin
		quotient0 <= quotient0_next_value6;
	end
	if (remainder0_next_value_ce7) begin
		remainder0 <= remainder0_next_value7;
	end
	if (sys_rst) begin
		quotient0 <= 1024'd0;
		remainder0 <= 1024'd0;
		done <= 1'd0;
		count <= 16'd0;
		remainder1 <= 1025'd0;
		quotient1 <= 1024'd0;
		dividend_reg <= 1024'd0;
		divisor_reg <= 1024'd0;
		state <= 2'd0;
	end
end

endmodule
