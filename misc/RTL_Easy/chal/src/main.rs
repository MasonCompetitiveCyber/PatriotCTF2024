use rust_hdl::prelude::*;
use rust_hdl_bsp_alchitry_cu::pins::CLOCK_SPEED_100MHZ;
use rust_hdl_bsp_alchitry_cu::{pins, synth};
use std::time::Duration;

const CLOCK_SPEED_HZ: u64 = 10_000;

#[derive(LogicBlock)]
pub struct Encryption {
    clock: Signal<In, Clock>,
    pulser: Pulser,
    din: Signal<In, Bits<8>>,
    temp: Signal<Local, Bits<10>>,
    dout: Signal<Out, Bits<8>>,
}

impl Logic for Encryption {
    #[hdl_gen]
    fn update(&mut self) {
        self.pulser.enable.next = true;
        self.pulser.clock.next = self.clock.val();
        self.temp.next = bit_cast::<10, 8>(self.din.val()) << 2 ^ 10;
        self.dout.next = bit_cast::<8, 10>(self.temp.val() >> 2);
    }
}

impl Default for Encryption {
    fn default() -> Self {
        let pulser = Pulser::new(CLOCK_SPEED_100MHZ.into(), 1.0, Duration::from_millis(250));
        Encryption {
            pulser,
            clock: pins::clock(),
            temp: Default::default(),
            din: Default::default(),
            dout: pins::leds(),
        }
    }
}

fn main() {
    let uut = Encryption::default();
    let flag = "PCTF{H@rd_Encryption_is_3asy}";

    // Simulate the encryption
    //
    let mut sim = simple_sim!(Encryption, clock, CLOCK_SPEED_HZ, ep, {
        let mut x = ep.init()?;

        for f in flag.chars() {
            x.din.next = bits(f as u64);
            wait_clock_cycle!(ep, clock, x);
        }

        ep.done(x)
    });

    sim.run_to_file(
        Encryption::default().into(),
        3 * sim_time::ONE_MILLISECOND,
        &vcd_path!("flag.vcd"),
    )
    .unwrap();

    vcd_to_svg(
        &vcd_path!("flag.vcd"),
        "flag.svg",
        &["uut.dout", "uut.clock"],
        0,
        3 * sim_time::ONE_MILLISECOND,
    )
    .unwrap();

    synth::generate_bitstream(uut, "firmware/doorlock")
}
