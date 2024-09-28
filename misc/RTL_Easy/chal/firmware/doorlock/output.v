module ICESTORM_LC (
    {'direction': 'input', 'bits': [2]} I0,
    {'direction': 'input', 'bits': [3]} I1,
    {'direction': 'input', 'bits': [4]} I2,
    {'direction': 'input', 'bits': [5]} I3,
    {'direction': 'input', 'bits': [6]} CIN,
    {'direction': 'input', 'bits': [7]} CLK,
    {'direction': 'input', 'bits': [8]} CEN,
    {'direction': 'input', 'bits': [9]} SR,
    {'direction': 'output', 'bits': [10]} LO,
    {'direction': 'output', 'bits': [11]} O,
    {'direction': 'output', 'bits': [12]} COUT
);

  $specify2 $specify$126 (
    .DST([12]),
    .EN(['1']),
    .SRC([6])
  );
  $specify2 $specify$127 (
    .DST([11]),
    .EN(['1']),
    .SRC([2])
  );
  $specify2 $specify$128 (
    .DST([10]),
    .EN(['1']),
    .SRC([2])
  );
  $specify2 $specify$129 (
    .DST([12]),
    .EN(['1']),
    .SRC([3])
  );
  $specify2 $specify$130 (
    .DST([11]),
    .EN(['1']),
    .SRC([3])
  );
  $specify2 $specify$131 (
    .DST([10]),
    .EN(['1']),
    .SRC([3])
  );
  $specify2 $specify$132 (
    .DST([12]),
    .EN(['1']),
    .SRC([4])
  );
  $specify2 $specify$133 (
    .DST([11]),
    .EN(['1']),
    .SRC([4])
  );
  $specify2 $specify$134 (
    .DST([10]),
    .EN(['1']),
    .SRC([4])
  );
  $specify2 $specify$135 (
    .DST([11]),
    .EN(['1']),
    .SRC([5])
  );
  $specify2 $specify$136 (
    .DST([10]),
    .EN(['1']),
    .SRC([5])
  );
  $specify3 $specify$137 (
    .DAT(['x']),
    .DST([11]),
    .EN(['1']),
    .SRC([7])
  );
  $specify2 $specify$138 (
    .DST([11]),
    .EN(['1']),
    .SRC([9])
  );
  $specrule $specify$139 (
    .DST([2]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$140 (
    .DST([2]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$141 (
    .DST([2]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$142 (
    .DST([2]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$143 (
    .DST([3]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$144 (
    .DST([3]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$145 (
    .DST([3]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$146 (
    .DST([3]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$147 (
    .DST([4]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$148 (
    .DST([4]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$149 (
    .DST([4]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$150 (
    .DST([4]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$151 (
    .DST([5]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$152 (
    .DST([5]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$153 (
    .DST([5]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$154 (
    .DST([5]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$155 (
    .DST([8]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$156 (
    .DST([8]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$157 (
    .DST([9]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$158 (
    .DST([9]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$159 (
    .DST([9]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );
  $specrule $specify$160 (
    .DST([9]),
    .DST_EN(['1']),
    .SRC([7]),
    .SRC_EN(['1'])
  );


endmodule
module ICESTORM_RAM (
    {'direction': 'output', 'bits': [2]} RDATA_15,
    {'direction': 'output', 'bits': [3]} RDATA_14,
    {'direction': 'output', 'bits': [4]} RDATA_13,
    {'direction': 'output', 'bits': [5]} RDATA_12,
    {'direction': 'output', 'bits': [6]} RDATA_11,
    {'direction': 'output', 'bits': [7]} RDATA_10,
    {'direction': 'output', 'bits': [8]} RDATA_9,
    {'direction': 'output', 'bits': [9]} RDATA_8,
    {'direction': 'output', 'bits': [10]} RDATA_7,
    {'direction': 'output', 'bits': [11]} RDATA_6,
    {'direction': 'output', 'bits': [12]} RDATA_5,
    {'direction': 'output', 'bits': [13]} RDATA_4,
    {'direction': 'output', 'bits': [14]} RDATA_3,
    {'direction': 'output', 'bits': [15]} RDATA_2,
    {'direction': 'output', 'bits': [16]} RDATA_1,
    {'direction': 'output', 'bits': [17]} RDATA_0,
    {'direction': 'input', 'bits': [18]} RCLK,
    {'direction': 'input', 'bits': [19]} RCLKE,
    {'direction': 'input', 'bits': [20]} RE,
    {'direction': 'input', 'bits': [21]} RADDR_10,
    {'direction': 'input', 'bits': [22]} RADDR_9,
    {'direction': 'input', 'bits': [23]} RADDR_8,
    {'direction': 'input', 'bits': [24]} RADDR_7,
    {'direction': 'input', 'bits': [25]} RADDR_6,
    {'direction': 'input', 'bits': [26]} RADDR_5,
    {'direction': 'input', 'bits': [27]} RADDR_4,
    {'direction': 'input', 'bits': [28]} RADDR_3,
    {'direction': 'input', 'bits': [29]} RADDR_2,
    {'direction': 'input', 'bits': [30]} RADDR_1,
    {'direction': 'input', 'bits': [31]} RADDR_0,
    {'direction': 'input', 'bits': [32]} WCLK,
    {'direction': 'input', 'bits': [33]} WCLKE,
    {'direction': 'input', 'bits': [34]} WE,
    {'direction': 'input', 'bits': [35]} WADDR_10,
    {'direction': 'input', 'bits': [36]} WADDR_9,
    {'direction': 'input', 'bits': [37]} WADDR_8,
    {'direction': 'input', 'bits': [38]} WADDR_7,
    {'direction': 'input', 'bits': [39]} WADDR_6,
    {'direction': 'input', 'bits': [40]} WADDR_5,
    {'direction': 'input', 'bits': [41]} WADDR_4,
    {'direction': 'input', 'bits': [42]} WADDR_3,
    {'direction': 'input', 'bits': [43]} WADDR_2,
    {'direction': 'input', 'bits': [44]} WADDR_1,
    {'direction': 'input', 'bits': [45]} WADDR_0,
    {'direction': 'input', 'bits': [46]} MASK_15,
    {'direction': 'input', 'bits': [47]} MASK_14,
    {'direction': 'input', 'bits': [48]} MASK_13,
    {'direction': 'input', 'bits': [49]} MASK_12,
    {'direction': 'input', 'bits': [50]} MASK_11,
    {'direction': 'input', 'bits': [51]} MASK_10,
    {'direction': 'input', 'bits': [52]} MASK_9,
    {'direction': 'input', 'bits': [53]} MASK_8,
    {'direction': 'input', 'bits': [54]} MASK_7,
    {'direction': 'input', 'bits': [55]} MASK_6,
    {'direction': 'input', 'bits': [56]} MASK_5,
    {'direction': 'input', 'bits': [57]} MASK_4,
    {'direction': 'input', 'bits': [58]} MASK_3,
    {'direction': 'input', 'bits': [59]} MASK_2,
    {'direction': 'input', 'bits': [60]} MASK_1,
    {'direction': 'input', 'bits': [61]} MASK_0,
    {'direction': 'input', 'bits': [62]} WDATA_15,
    {'direction': 'input', 'bits': [63]} WDATA_14,
    {'direction': 'input', 'bits': [64]} WDATA_13,
    {'direction': 'input', 'bits': [65]} WDATA_12,
    {'direction': 'input', 'bits': [66]} WDATA_11,
    {'direction': 'input', 'bits': [67]} WDATA_10,
    {'direction': 'input', 'bits': [68]} WDATA_9,
    {'direction': 'input', 'bits': [69]} WDATA_8,
    {'direction': 'input', 'bits': [70]} WDATA_7,
    {'direction': 'input', 'bits': [71]} WDATA_6,
    {'direction': 'input', 'bits': [72]} WDATA_5,
    {'direction': 'input', 'bits': [73]} WDATA_4,
    {'direction': 'input', 'bits': [74]} WDATA_3,
    {'direction': 'input', 'bits': [75]} WDATA_2,
    {'direction': 'input', 'bits': [76]} WDATA_1,
    {'direction': 'input', 'bits': [77]} WDATA_0
);



endmodule
module SB_CARRY (
    {'direction': 'output', 'bits': [2]} CO,
    {'direction': 'input', 'bits': [3]} I0,
    {'direction': 'input', 'bits': [4]} I1,
    {'direction': 'input', 'bits': [5]} CI
);



endmodule
module SB_DFF (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} D
);



endmodule
module SB_DFFE (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} E,
    {'direction': 'input', 'bits': [5]} D
);



endmodule
module SB_DFFER (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} E,
    {'direction': 'input', 'bits': [5]} R,
    {'direction': 'input', 'bits': [6]} D
);



endmodule
module SB_DFFES (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} E,
    {'direction': 'input', 'bits': [5]} S,
    {'direction': 'input', 'bits': [6]} D
);



endmodule
module SB_DFFESR (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} E,
    {'direction': 'input', 'bits': [5]} R,
    {'direction': 'input', 'bits': [6]} D
);



endmodule
module SB_DFFESS (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} E,
    {'direction': 'input', 'bits': [5]} S,
    {'direction': 'input', 'bits': [6]} D
);



endmodule
module SB_DFFN (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} D
);



endmodule
module SB_DFFNE (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} E,
    {'direction': 'input', 'bits': [5]} D
);



endmodule
module SB_DFFNER (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} E,
    {'direction': 'input', 'bits': [5]} R,
    {'direction': 'input', 'bits': [6]} D
);



endmodule
module SB_DFFNES (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} E,
    {'direction': 'input', 'bits': [5]} S,
    {'direction': 'input', 'bits': [6]} D
);



endmodule
module SB_DFFNESR (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} E,
    {'direction': 'input', 'bits': [5]} R,
    {'direction': 'input', 'bits': [6]} D
);



endmodule
module SB_DFFNESS (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} E,
    {'direction': 'input', 'bits': [5]} S,
    {'direction': 'input', 'bits': [6]} D
);



endmodule
module SB_DFFNR (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} R,
    {'direction': 'input', 'bits': [5]} D
);



endmodule
module SB_DFFNS (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} S,
    {'direction': 'input', 'bits': [5]} D
);



endmodule
module SB_DFFNSR (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} R,
    {'direction': 'input', 'bits': [5]} D
);



endmodule
module SB_DFFNSS (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} S,
    {'direction': 'input', 'bits': [5]} D
);



endmodule
module SB_DFFR (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} R,
    {'direction': 'input', 'bits': [5]} D
);



endmodule
module SB_DFFS (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} S,
    {'direction': 'input', 'bits': [5]} D
);



endmodule
module SB_DFFSR (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} R,
    {'direction': 'input', 'bits': [5]} D
);



endmodule
module SB_DFFSS (
    {'direction': 'output', 'bits': [2]} Q,
    {'direction': 'input', 'bits': [3]} C,
    {'direction': 'input', 'bits': [4]} S,
    {'direction': 'input', 'bits': [5]} D
);



endmodule
module SB_FILTER_50NS (
    {'direction': 'input', 'bits': [2]} FILTERIN,
    {'direction': 'output', 'bits': [3]} FILTEROUT
);



endmodule
module SB_GB (
    {'direction': 'input', 'bits': [2]} USER_SIGNAL_TO_GLOBAL_BUFFER,
    {'direction': 'output', 'bits': [3]} GLOBAL_BUFFER_OUTPUT
);



endmodule
module SB_GB_IO (
    {'direction': 'inout', 'bits': [2]} PACKAGE_PIN,
    {'direction': 'output', 'bits': [3]} GLOBAL_BUFFER_OUTPUT,
    {'direction': 'input', 'bits': [4]} LATCH_INPUT_VALUE,
    {'direction': 'input', 'bits': [5]} CLOCK_ENABLE,
    {'direction': 'input', 'bits': [6]} INPUT_CLK,
    {'direction': 'input', 'bits': [7]} OUTPUT_CLK,
    {'direction': 'input', 'bits': [8]} OUTPUT_ENABLE,
    {'direction': 'input', 'bits': [9]} D_OUT_0,
    {'direction': 'input', 'bits': [10]} D_OUT_1,
    {'direction': 'output', 'bits': [11]} D_IN_0,
    {'direction': 'output', 'bits': [12]} D_IN_1
);



endmodule
module SB_HFOSC (
    {'direction': 'input', 'bits': [2]} TRIM0,
    {'direction': 'input', 'bits': [3]} TRIM1,
    {'direction': 'input', 'bits': [4]} TRIM2,
    {'direction': 'input', 'bits': [5]} TRIM3,
    {'direction': 'input', 'bits': [6]} TRIM4,
    {'direction': 'input', 'bits': [7]} TRIM5,
    {'direction': 'input', 'bits': [8]} TRIM6,
    {'direction': 'input', 'bits': [9]} TRIM7,
    {'direction': 'input', 'bits': [10]} TRIM8,
    {'direction': 'input', 'bits': [11]} TRIM9,
    {'direction': 'input', 'bits': [12]} CLKHFPU,
    {'direction': 'input', 'bits': [13]} CLKHFEN,
    {'direction': 'output', 'bits': [14]} CLKHF
);



endmodule
module SB_I2C (
    {'direction': 'input', 'bits': [2]} SBCLKI,
    {'direction': 'input', 'bits': [3]} SBRWI,
    {'direction': 'input', 'bits': [4]} SBSTBI,
    {'direction': 'input', 'bits': [5]} SBADRI7,
    {'direction': 'input', 'bits': [6]} SBADRI6,
    {'direction': 'input', 'bits': [7]} SBADRI5,
    {'direction': 'input', 'bits': [8]} SBADRI4,
    {'direction': 'input', 'bits': [9]} SBADRI3,
    {'direction': 'input', 'bits': [10]} SBADRI2,
    {'direction': 'input', 'bits': [11]} SBADRI1,
    {'direction': 'input', 'bits': [12]} SBADRI0,
    {'direction': 'input', 'bits': [13]} SBDATI7,
    {'direction': 'input', 'bits': [14]} SBDATI6,
    {'direction': 'input', 'bits': [15]} SBDATI5,
    {'direction': 'input', 'bits': [16]} SBDATI4,
    {'direction': 'input', 'bits': [17]} SBDATI3,
    {'direction': 'input', 'bits': [18]} SBDATI2,
    {'direction': 'input', 'bits': [19]} SBDATI1,
    {'direction': 'input', 'bits': [20]} SBDATI0,
    {'direction': 'input', 'bits': [21]} SCLI,
    {'direction': 'input', 'bits': [22]} SDAI,
    {'direction': 'output', 'bits': [23]} SBDATO7,
    {'direction': 'output', 'bits': [24]} SBDATO6,
    {'direction': 'output', 'bits': [25]} SBDATO5,
    {'direction': 'output', 'bits': [26]} SBDATO4,
    {'direction': 'output', 'bits': [27]} SBDATO3,
    {'direction': 'output', 'bits': [28]} SBDATO2,
    {'direction': 'output', 'bits': [29]} SBDATO1,
    {'direction': 'output', 'bits': [30]} SBDATO0,
    {'direction': 'output', 'bits': [31]} SBACKO,
    {'direction': 'output', 'bits': [32]} I2CIRQ,
    {'direction': 'output', 'bits': [33]} I2CWKUP,
    {'direction': 'output', 'bits': [34]} SCLO,
    {'direction': 'output', 'bits': [35]} SCLOE,
    {'direction': 'output', 'bits': [36]} SDAO,
    {'direction': 'output', 'bits': [37]} SDAOE
);



endmodule
module SB_IO (
    {'direction': 'inout', 'bits': [2]} PACKAGE_PIN,
    {'direction': 'input', 'bits': [3]} LATCH_INPUT_VALUE,
    {'direction': 'input', 'bits': [4]} CLOCK_ENABLE,
    {'direction': 'input', 'bits': [5]} INPUT_CLK,
    {'direction': 'input', 'bits': [6]} OUTPUT_CLK,
    {'direction': 'input', 'bits': [7]} OUTPUT_ENABLE,
    {'direction': 'input', 'bits': [8]} D_OUT_0,
    {'direction': 'input', 'bits': [9]} D_OUT_1,
    {'direction': 'output', 'bits': [10]} D_IN_0,
    {'direction': 'output', 'bits': [11]} D_IN_1
);



endmodule
module SB_IO_I3C (
    {'direction': 'inout', 'bits': [2]} PACKAGE_PIN,
    {'direction': 'input', 'bits': [3]} LATCH_INPUT_VALUE,
    {'direction': 'input', 'bits': [4]} CLOCK_ENABLE,
    {'direction': 'input', 'bits': [5]} INPUT_CLK,
    {'direction': 'input', 'bits': [6]} OUTPUT_CLK,
    {'direction': 'input', 'bits': [7]} OUTPUT_ENABLE,
    {'direction': 'input', 'bits': [8]} D_OUT_0,
    {'direction': 'input', 'bits': [9]} D_OUT_1,
    {'direction': 'output', 'bits': [10]} D_IN_0,
    {'direction': 'output', 'bits': [11]} D_IN_1,
    {'direction': 'input', 'bits': [12]} PU_ENB,
    {'direction': 'input', 'bits': [13]} WEAK_PU_ENB
);



endmodule
module SB_IO_OD (
    {'direction': 'inout', 'bits': [2]} PACKAGEPIN,
    {'direction': 'input', 'bits': [3]} LATCHINPUTVALUE,
    {'direction': 'input', 'bits': [4]} CLOCKENABLE,
    {'direction': 'input', 'bits': [5]} INPUTCLK,
    {'direction': 'input', 'bits': [6]} OUTPUTCLK,
    {'direction': 'input', 'bits': [7]} OUTPUTENABLE,
    {'direction': 'input', 'bits': [8]} DOUT1,
    {'direction': 'input', 'bits': [9]} DOUT0,
    {'direction': 'output', 'bits': [10]} DIN1,
    {'direction': 'output', 'bits': [11]} DIN0
);



endmodule
module SB_LEDDA_IP (
    {'direction': 'input', 'bits': [2]} LEDDCS,
    {'direction': 'input', 'bits': [3]} LEDDCLK,
    {'direction': 'input', 'bits': [4]} LEDDDAT7,
    {'direction': 'input', 'bits': [5]} LEDDDAT6,
    {'direction': 'input', 'bits': [6]} LEDDDAT5,
    {'direction': 'input', 'bits': [7]} LEDDDAT4,
    {'direction': 'input', 'bits': [8]} LEDDDAT3,
    {'direction': 'input', 'bits': [9]} LEDDDAT2,
    {'direction': 'input', 'bits': [10]} LEDDDAT1,
    {'direction': 'input', 'bits': [11]} LEDDDAT0,
    {'direction': 'input', 'bits': [12]} LEDDADDR3,
    {'direction': 'input', 'bits': [13]} LEDDADDR2,
    {'direction': 'input', 'bits': [14]} LEDDADDR1,
    {'direction': 'input', 'bits': [15]} LEDDADDR0,
    {'direction': 'input', 'bits': [16]} LEDDDEN,
    {'direction': 'input', 'bits': [17]} LEDDEXE,
    {'direction': 'input', 'bits': [18]} LEDDRST,
    {'direction': 'output', 'bits': [19]} PWMOUT0,
    {'direction': 'output', 'bits': [20]} PWMOUT1,
    {'direction': 'output', 'bits': [21]} PWMOUT2,
    {'direction': 'output', 'bits': [22]} LEDDON
);



endmodule
module SB_LED_DRV_CUR (
    {'direction': 'input', 'bits': [2]} EN,
    {'direction': 'output', 'bits': [3]} LEDPU
);



endmodule
module SB_LFOSC (
    {'direction': 'input', 'bits': [2]} CLKLFPU,
    {'direction': 'input', 'bits': [3]} CLKLFEN,
    {'direction': 'output', 'bits': [4]} CLKLF
);



endmodule
module SB_LUT4 (
    {'direction': 'output', 'bits': [2]} O,
    {'direction': 'input', 'bits': [3]} I0,
    {'direction': 'input', 'bits': [4]} I1,
    {'direction': 'input', 'bits': [5]} I2,
    {'direction': 'input', 'bits': [6]} I3
);



endmodule
module SB_MAC16 (
    {'direction': 'input', 'bits': [2]} CLK,
    {'direction': 'input', 'bits': [3]} CE,
    {'direction': 'input', 'bits': [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]} C,
    {'direction': 'input', 'bits': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]} A,
    {'direction': 'input', 'bits': [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]} B,
    {'direction': 'input', 'bits': [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]} D,
    {'direction': 'input', 'bits': [68]} AHOLD,
    {'direction': 'input', 'bits': [69]} BHOLD,
    {'direction': 'input', 'bits': [70]} CHOLD,
    {'direction': 'input', 'bits': [71]} DHOLD,
    {'direction': 'input', 'bits': [72]} IRSTTOP,
    {'direction': 'input', 'bits': [73]} IRSTBOT,
    {'direction': 'input', 'bits': [74]} ORSTTOP,
    {'direction': 'input', 'bits': [75]} ORSTBOT,
    {'direction': 'input', 'bits': [76]} OLOADTOP,
    {'direction': 'input', 'bits': [77]} OLOADBOT,
    {'direction': 'input', 'bits': [78]} ADDSUBTOP,
    {'direction': 'input', 'bits': [79]} ADDSUBBOT,
    {'direction': 'input', 'bits': [80]} OHOLDTOP,
    {'direction': 'input', 'bits': [81]} OHOLDBOT,
    {'direction': 'input', 'bits': [82]} CI,
    {'direction': 'input', 'bits': [83]} ACCUMCI,
    {'direction': 'input', 'bits': [84]} SIGNEXTIN,
    {'direction': 'output', 'bits': [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]} O,
    {'direction': 'output', 'bits': [117]} CO,
    {'direction': 'output', 'bits': [118]} ACCUMCO,
    {'direction': 'output', 'bits': [119]} SIGNEXTOUT
);



endmodule
module SB_PLL40_2F_CORE (
    {'direction': 'input', 'bits': [2]} REFERENCECLK,
    {'direction': 'output', 'bits': [3]} PLLOUTCOREA,
    {'direction': 'output', 'bits': [4]} PLLOUTGLOBALA,
    {'direction': 'output', 'bits': [5]} PLLOUTCOREB,
    {'direction': 'output', 'bits': [6]} PLLOUTGLOBALB,
    {'direction': 'input', 'bits': [7]} EXTFEEDBACK,
    {'direction': 'input', 'bits': [8, 9, 10, 11, 12, 13, 14, 15]} DYNAMICDELAY,
    {'direction': 'output', 'bits': [16]} LOCK,
    {'direction': 'input', 'bits': [17]} BYPASS,
    {'direction': 'input', 'bits': [18]} RESETB,
    {'direction': 'input', 'bits': [19]} LATCHINPUTVALUE,
    {'direction': 'output', 'bits': [20]} SDO,
    {'direction': 'input', 'bits': [21]} SDI,
    {'direction': 'input', 'bits': [22]} SCLK
);



endmodule
module SB_PLL40_2F_PAD (
    {'direction': 'input', 'bits': [2]} PACKAGEPIN,
    {'direction': 'output', 'bits': [3]} PLLOUTCOREA,
    {'direction': 'output', 'bits': [4]} PLLOUTGLOBALA,
    {'direction': 'output', 'bits': [5]} PLLOUTCOREB,
    {'direction': 'output', 'bits': [6]} PLLOUTGLOBALB,
    {'direction': 'input', 'bits': [7]} EXTFEEDBACK,
    {'direction': 'input', 'bits': [8, 9, 10, 11, 12, 13, 14, 15]} DYNAMICDELAY,
    {'direction': 'output', 'bits': [16]} LOCK,
    {'direction': 'input', 'bits': [17]} BYPASS,
    {'direction': 'input', 'bits': [18]} RESETB,
    {'direction': 'input', 'bits': [19]} LATCHINPUTVALUE,
    {'direction': 'output', 'bits': [20]} SDO,
    {'direction': 'input', 'bits': [21]} SDI,
    {'direction': 'input', 'bits': [22]} SCLK
);



endmodule
module SB_PLL40_2_PAD (
    {'direction': 'input', 'bits': [2]} PACKAGEPIN,
    {'direction': 'output', 'bits': [3]} PLLOUTCOREA,
    {'direction': 'output', 'bits': [4]} PLLOUTGLOBALA,
    {'direction': 'output', 'bits': [5]} PLLOUTCOREB,
    {'direction': 'output', 'bits': [6]} PLLOUTGLOBALB,
    {'direction': 'input', 'bits': [7]} EXTFEEDBACK,
    {'direction': 'input', 'bits': [8, 9, 10, 11, 12, 13, 14, 15]} DYNAMICDELAY,
    {'direction': 'output', 'bits': [16]} LOCK,
    {'direction': 'input', 'bits': [17]} BYPASS,
    {'direction': 'input', 'bits': [18]} RESETB,
    {'direction': 'input', 'bits': [19]} LATCHINPUTVALUE,
    {'direction': 'output', 'bits': [20]} SDO,
    {'direction': 'input', 'bits': [21]} SDI,
    {'direction': 'input', 'bits': [22]} SCLK
);



endmodule
module SB_PLL40_CORE (
    {'direction': 'input', 'bits': [2]} REFERENCECLK,
    {'direction': 'output', 'bits': [3]} PLLOUTCORE,
    {'direction': 'output', 'bits': [4]} PLLOUTGLOBAL,
    {'direction': 'input', 'bits': [5]} EXTFEEDBACK,
    {'direction': 'input', 'bits': [6, 7, 8, 9, 10, 11, 12, 13]} DYNAMICDELAY,
    {'direction': 'output', 'bits': [14]} LOCK,
    {'direction': 'input', 'bits': [15]} BYPASS,
    {'direction': 'input', 'bits': [16]} RESETB,
    {'direction': 'input', 'bits': [17]} LATCHINPUTVALUE,
    {'direction': 'output', 'bits': [18]} SDO,
    {'direction': 'input', 'bits': [19]} SDI,
    {'direction': 'input', 'bits': [20]} SCLK
);



endmodule
module SB_PLL40_PAD (
    {'direction': 'input', 'bits': [2]} PACKAGEPIN,
    {'direction': 'output', 'bits': [3]} PLLOUTCORE,
    {'direction': 'output', 'bits': [4]} PLLOUTGLOBAL,
    {'direction': 'input', 'bits': [5]} EXTFEEDBACK,
    {'direction': 'input', 'bits': [6, 7, 8, 9, 10, 11, 12, 13]} DYNAMICDELAY,
    {'direction': 'output', 'bits': [14]} LOCK,
    {'direction': 'input', 'bits': [15]} BYPASS,
    {'direction': 'input', 'bits': [16]} RESETB,
    {'direction': 'input', 'bits': [17]} LATCHINPUTVALUE,
    {'direction': 'output', 'bits': [18]} SDO,
    {'direction': 'input', 'bits': [19]} SDI,
    {'direction': 'input', 'bits': [20]} SCLK
);



endmodule
module SB_RAM40_4K (
    {'direction': 'output', 'bits': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]} RDATA,
    {'direction': 'input', 'bits': [18]} RCLK,
    {'direction': 'input', 'bits': [19]} RCLKE,
    {'direction': 'input', 'bits': [20]} RE,
    {'direction': 'input', 'bits': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]} RADDR,
    {'direction': 'input', 'bits': [32]} WCLK,
    {'direction': 'input', 'bits': [33]} WCLKE,
    {'direction': 'input', 'bits': [34]} WE,
    {'direction': 'input', 'bits': [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]} WADDR,
    {'direction': 'input', 'bits': [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]} MASK,
    {'direction': 'input', 'bits': [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]} WDATA
);

  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1661$245 (
    .A([34]),
    .B([33]),
    .Y([78])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1663$246 (
    .A([20]),
    .B([19]),
    .Y([79])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1669$247 (
    .A([34]),
    .B([33]),
    .Y([80])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1673$248 (
    .A([34]),
    .B([33]),
    .Y([81])
  );
  $specrule $specify$90 (
    .DST([32]),
    .DST_EN([78]),
    .SRC([46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]),
    .SRC_EN(['1'])
  );
  $specrule $specify$91 (
    .DST([18]),
    .DST_EN([79]),
    .SRC([21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),
    .SRC_EN(['1'])
  );
  $specrule $specify$92 (
    .DST([18]),
    .DST_EN(['1']),
    .SRC([19]),
    .SRC_EN(['1'])
  );
  $specrule $specify$93 (
    .DST([18]),
    .DST_EN(['1']),
    .SRC([20]),
    .SRC_EN(['1'])
  );
  $specrule $specify$94 (
    .DST([32]),
    .DST_EN([80]),
    .SRC([35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]),
    .SRC_EN(['1'])
  );
  $specrule $specify$95 (
    .DST([32]),
    .DST_EN(['1']),
    .SRC([33]),
    .SRC_EN(['1'])
  );
  $specrule $specify$96 (
    .DST([32]),
    .DST_EN([81]),
    .SRC([62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]),
    .SRC_EN(['1'])
  );
  $specrule $specify$97 (
    .DST([32]),
    .DST_EN(['1']),
    .SRC([34]),
    .SRC_EN(['1'])
  );
  $specify3 $specify$98 (
    .DAT(['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']),
    .DST([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]),
    .EN(['1']),
    .SRC([18])
  );


endmodule
module SB_RAM40_4KNR (
    {'direction': 'output', 'bits': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]} RDATA,
    {'direction': 'input', 'bits': [18]} RCLKN,
    {'direction': 'input', 'bits': [19]} RCLKE,
    {'direction': 'input', 'bits': [20]} RE,
    {'direction': 'input', 'bits': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]} RADDR,
    {'direction': 'input', 'bits': [32]} WCLK,
    {'direction': 'input', 'bits': [33]} WCLKE,
    {'direction': 'input', 'bits': [34]} WE,
    {'direction': 'input', 'bits': [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]} WADDR,
    {'direction': 'input', 'bits': [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]} MASK,
    {'direction': 'input', 'bits': [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]} WDATA
);

  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1797$249 (
    .A([34]),
    .B([33]),
    .Y([78])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1799$250 (
    .A([20]),
    .B([19]),
    .Y([79])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1805$251 (
    .A([34]),
    .B([33]),
    .Y([80])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1809$252 (
    .A([34]),
    .B([33]),
    .Y([81])
  );
  $specrule $specify$100 (
    .DST([18]),
    .DST_EN([79]),
    .SRC([21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),
    .SRC_EN(['1'])
  );
  $specrule $specify$101 (
    .DST([18]),
    .DST_EN(['1']),
    .SRC([19]),
    .SRC_EN(['1'])
  );
  $specrule $specify$102 (
    .DST([18]),
    .DST_EN(['1']),
    .SRC([20]),
    .SRC_EN(['1'])
  );
  $specrule $specify$103 (
    .DST([32]),
    .DST_EN([80]),
    .SRC([35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]),
    .SRC_EN(['1'])
  );
  $specrule $specify$104 (
    .DST([32]),
    .DST_EN(['1']),
    .SRC([33]),
    .SRC_EN(['1'])
  );
  $specrule $specify$105 (
    .DST([32]),
    .DST_EN([81]),
    .SRC([62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]),
    .SRC_EN(['1'])
  );
  $specrule $specify$106 (
    .DST([32]),
    .DST_EN(['1']),
    .SRC([34]),
    .SRC_EN(['1'])
  );
  $specify3 $specify$107 (
    .DAT(['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']),
    .DST([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]),
    .EN(['1']),
    .SRC([18])
  );
  $specrule $specify$99 (
    .DST([32]),
    .DST_EN([78]),
    .SRC([46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]),
    .SRC_EN(['1'])
  );


endmodule
module SB_RAM40_4KNRNW (
    {'direction': 'output', 'bits': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]} RDATA,
    {'direction': 'input', 'bits': [18]} RCLKN,
    {'direction': 'input', 'bits': [19]} RCLKE,
    {'direction': 'input', 'bits': [20]} RE,
    {'direction': 'input', 'bits': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]} RADDR,
    {'direction': 'input', 'bits': [32]} WCLKN,
    {'direction': 'input', 'bits': [33]} WCLKE,
    {'direction': 'input', 'bits': [34]} WE,
    {'direction': 'input', 'bits': [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]} WADDR,
    {'direction': 'input', 'bits': [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]} MASK,
    {'direction': 'input', 'bits': [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]} WDATA
);

  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:2069$257 (
    .A([34]),
    .B([33]),
    .Y([78])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:2071$258 (
    .A([20]),
    .B([19]),
    .Y([79])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:2077$259 (
    .A([34]),
    .B([33]),
    .Y([80])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:2081$260 (
    .A([34]),
    .B([33]),
    .Y([81])
  );
  $specrule $specify$117 (
    .DST([32]),
    .DST_EN([78]),
    .SRC([46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]),
    .SRC_EN(['1'])
  );
  $specrule $specify$118 (
    .DST([18]),
    .DST_EN([79]),
    .SRC([21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),
    .SRC_EN(['1'])
  );
  $specrule $specify$119 (
    .DST([18]),
    .DST_EN(['1']),
    .SRC([19]),
    .SRC_EN(['1'])
  );
  $specrule $specify$120 (
    .DST([18]),
    .DST_EN(['1']),
    .SRC([20]),
    .SRC_EN(['1'])
  );
  $specrule $specify$121 (
    .DST([32]),
    .DST_EN([80]),
    .SRC([35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]),
    .SRC_EN(['1'])
  );
  $specrule $specify$122 (
    .DST([32]),
    .DST_EN(['1']),
    .SRC([33]),
    .SRC_EN(['1'])
  );
  $specrule $specify$123 (
    .DST([32]),
    .DST_EN([81]),
    .SRC([62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]),
    .SRC_EN(['1'])
  );
  $specrule $specify$124 (
    .DST([32]),
    .DST_EN(['1']),
    .SRC([34]),
    .SRC_EN(['1'])
  );
  $specify3 $specify$125 (
    .DAT(['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']),
    .DST([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]),
    .EN(['1']),
    .SRC([18])
  );


endmodule
module SB_RAM40_4KNW (
    {'direction': 'output', 'bits': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]} RDATA,
    {'direction': 'input', 'bits': [18]} RCLK,
    {'direction': 'input', 'bits': [19]} RCLKE,
    {'direction': 'input', 'bits': [20]} RE,
    {'direction': 'input', 'bits': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]} RADDR,
    {'direction': 'input', 'bits': [32]} WCLKN,
    {'direction': 'input', 'bits': [33]} WCLKE,
    {'direction': 'input', 'bits': [34]} WE,
    {'direction': 'input', 'bits': [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]} WADDR,
    {'direction': 'input', 'bits': [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]} MASK,
    {'direction': 'input', 'bits': [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]} WDATA
);

  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1933$253 (
    .A([34]),
    .B([33]),
    .Y([78])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1935$254 (
    .A([20]),
    .B([19]),
    .Y([79])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1941$255 (
    .A([34]),
    .B([33]),
    .Y([80])
  );
  $logic_and $logic_and$/usr/bin/../share/yosys/ice40/cells_sim.v:1945$256 (
    .A([34]),
    .B([33]),
    .Y([81])
  );
  $specrule $specify$108 (
    .DST([32]),
    .DST_EN([78]),
    .SRC([46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]),
    .SRC_EN(['1'])
  );
  $specrule $specify$109 (
    .DST([18]),
    .DST_EN([79]),
    .SRC([21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),
    .SRC_EN(['1'])
  );
  $specrule $specify$110 (
    .DST([18]),
    .DST_EN(['1']),
    .SRC([19]),
    .SRC_EN(['1'])
  );
  $specrule $specify$111 (
    .DST([18]),
    .DST_EN(['1']),
    .SRC([20]),
    .SRC_EN(['1'])
  );
  $specrule $specify$112 (
    .DST([32]),
    .DST_EN([80]),
    .SRC([35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]),
    .SRC_EN(['1'])
  );
  $specrule $specify$113 (
    .DST([32]),
    .DST_EN(['1']),
    .SRC([33]),
    .SRC_EN(['1'])
  );
  $specrule $specify$114 (
    .DST([32]),
    .DST_EN([81]),
    .SRC([62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]),
    .SRC_EN(['1'])
  );
  $specrule $specify$115 (
    .DST([32]),
    .DST_EN(['1']),
    .SRC([34]),
    .SRC_EN(['1'])
  );
  $specify3 $specify$116 (
    .DAT(['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']),
    .DST([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]),
    .EN(['1']),
    .SRC([18])
  );


endmodule
module SB_RGBA_DRV (
    {'direction': 'input', 'bits': [2]} CURREN,
    {'direction': 'input', 'bits': [3]} RGBLEDEN,
    {'direction': 'input', 'bits': [4]} RGB0PWM,
    {'direction': 'input', 'bits': [5]} RGB1PWM,
    {'direction': 'input', 'bits': [6]} RGB2PWM,
    {'direction': 'output', 'bits': [7]} RGB0,
    {'direction': 'output', 'bits': [8]} RGB1,
    {'direction': 'output', 'bits': [9]} RGB2
);



endmodule
module SB_RGB_DRV (
    {'direction': 'input', 'bits': [2]} RGBLEDEN,
    {'direction': 'input', 'bits': [3]} RGB0PWM,
    {'direction': 'input', 'bits': [4]} RGB1PWM,
    {'direction': 'input', 'bits': [5]} RGB2PWM,
    {'direction': 'input', 'bits': [6]} RGBPU,
    {'direction': 'output', 'bits': [7]} RGB0,
    {'direction': 'output', 'bits': [8]} RGB1,
    {'direction': 'output', 'bits': [9]} RGB2
);



endmodule
module SB_SPI (
    {'direction': 'input', 'bits': [2]} SBCLKI,
    {'direction': 'input', 'bits': [3]} SBRWI,
    {'direction': 'input', 'bits': [4]} SBSTBI,
    {'direction': 'input', 'bits': [5]} SBADRI7,
    {'direction': 'input', 'bits': [6]} SBADRI6,
    {'direction': 'input', 'bits': [7]} SBADRI5,
    {'direction': 'input', 'bits': [8]} SBADRI4,
    {'direction': 'input', 'bits': [9]} SBADRI3,
    {'direction': 'input', 'bits': [10]} SBADRI2,
    {'direction': 'input', 'bits': [11]} SBADRI1,
    {'direction': 'input', 'bits': [12]} SBADRI0,
    {'direction': 'input', 'bits': [13]} SBDATI7,
    {'direction': 'input', 'bits': [14]} SBDATI6,
    {'direction': 'input', 'bits': [15]} SBDATI5,
    {'direction': 'input', 'bits': [16]} SBDATI4,
    {'direction': 'input', 'bits': [17]} SBDATI3,
    {'direction': 'input', 'bits': [18]} SBDATI2,
    {'direction': 'input', 'bits': [19]} SBDATI1,
    {'direction': 'input', 'bits': [20]} SBDATI0,
    {'direction': 'input', 'bits': [21]} MI,
    {'direction': 'input', 'bits': [22]} SI,
    {'direction': 'input', 'bits': [23]} SCKI,
    {'direction': 'input', 'bits': [24]} SCSNI,
    {'direction': 'output', 'bits': [25]} SBDATO7,
    {'direction': 'output', 'bits': [26]} SBDATO6,
    {'direction': 'output', 'bits': [27]} SBDATO5,
    {'direction': 'output', 'bits': [28]} SBDATO4,
    {'direction': 'output', 'bits': [29]} SBDATO3,
    {'direction': 'output', 'bits': [30]} SBDATO2,
    {'direction': 'output', 'bits': [31]} SBDATO1,
    {'direction': 'output', 'bits': [32]} SBDATO0,
    {'direction': 'output', 'bits': [33]} SBACKO,
    {'direction': 'output', 'bits': [34]} SPIIRQ,
    {'direction': 'output', 'bits': [35]} SPIWKUP,
    {'direction': 'output', 'bits': [36]} SO,
    {'direction': 'output', 'bits': [37]} SOE,
    {'direction': 'output', 'bits': [38]} MO,
    {'direction': 'output', 'bits': [39]} MOE,
    {'direction': 'output', 'bits': [40]} SCKO,
    {'direction': 'output', 'bits': [41]} SCKOE,
    {'direction': 'output', 'bits': [42]} MCSNO3,
    {'direction': 'output', 'bits': [43]} MCSNO2,
    {'direction': 'output', 'bits': [44]} MCSNO1,
    {'direction': 'output', 'bits': [45]} MCSNO0,
    {'direction': 'output', 'bits': [46]} MCSNOE3,
    {'direction': 'output', 'bits': [47]} MCSNOE2,
    {'direction': 'output', 'bits': [48]} MCSNOE1,
    {'direction': 'output', 'bits': [49]} MCSNOE0
);



endmodule
module SB_SPRAM256KA (
    {'direction': 'input', 'bits': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]} ADDRESS,
    {'direction': 'input', 'bits': [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]} DATAIN,
    {'direction': 'input', 'bits': [32, 33, 34, 35]} MASKWREN,
    {'direction': 'input', 'bits': [36]} WREN,
    {'direction': 'input', 'bits': [37]} CHIPSELECT,
    {'direction': 'input', 'bits': [38]} CLOCK,
    {'direction': 'input', 'bits': [39]} STANDBY,
    {'direction': 'input', 'bits': [40]} SLEEP,
    {'direction': 'input', 'bits': [41]} POWEROFF,
    {'direction': 'output', 'bits': [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]} DATAOUT
);



endmodule
module SB_WARMBOOT (
    {'direction': 'input', 'bits': [2]} BOOT,
    {'direction': 'input', 'bits': [3]} S1,
    {'direction': 'input', 'bits': [4]} S0
);



endmodule
module top (
    {'direction': 'input', 'bits': [2]} clock,
    {'direction': 'input', 'bits': [3, 4, 5, 6, 7, 8, 9, 10]} din,
    {'direction': 'output', 'bits': [3, 11, 5, 6, 7, 8, 9, 10]} dout
);

  SB_LUT4 dout_SB_LUT4_O (
    .I0(['0']),
    .I1(['0']),
    .I2(['0']),
    .I3([4]),
    .O([11])
  );


endmodule
