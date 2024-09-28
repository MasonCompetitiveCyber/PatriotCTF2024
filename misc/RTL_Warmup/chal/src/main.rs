use rust_hdl::prelude::*;
use rust_hdl_bsp_alchitry_cu::{pins, synth};

const CLOCK_SPEED_HZ: u64 = 10_000;

#[derive(LogicBlock)] // Tuns struct into something that you can simulate
struct Flag {
    pub clock: Signal<In, Clock>, // Input signal of type clock
    // pulser: Pulser,
    pub dout: Signal<Out, Bits<8>>, // 8 bit output for each clock cycle
    pub din: Signal<In, Bits<8>>,
    // pub addr: Signal<In, Bits<2>>,
}

impl Default for Flag {
    fn default() -> Self {
        Self {
            clock: Default::default(),
            // pulser: Pulser::new(CLOCK_SPEED_HZ, 1.0, Duration::from_millis(250)),
            dout: Default::default(),
            // addr: Default::default(),
            din: Default::default(),
        }
    }
}

impl Logic for Flag {
    #[hdl_gen] // turns the update function into an HDL Kernel that can be turned into verilog
    fn update(&mut self) {
        // self.pulser.clock.next = self.clock.val();
        // self.pulser.enable.next = true.into();
        self.dout.next = self.din.val();
    }
}

fn main() {
    let flag_val = vec![
        0x50, 0x43, 0x54, 0x46, 0x7B, 0x52, 0x54, 0x4C, 0x5F, 0x69, 0x24, 0x5F, 0x44, 0x40, 0x44,
        0x5F, 0x30, 0x46, 0x5F, 0x48, 0x40, 0x72, 0x64, 0x77, 0x40, 0x72, 0x33, 0x7D,
    ];

    let mut sim = simple_sim!(Flag, clock, CLOCK_SPEED_HZ, ep, {
        let mut x = ep.init()?;

        for f in &flag_val {
            x.din.next = bits(*f as u64);
            wait_clock_cycle!(ep, clock, x);
        }

        ep.done(x)
    });

    sim.run_to_file(
        Flag::default().into(),
        3 * sim_time::ONE_MILLISECOND,
        "flag.vcd",
    )
    .unwrap();
}
