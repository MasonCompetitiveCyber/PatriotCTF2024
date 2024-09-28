use std::io::{self, Write};
use hex::{decode, encode};
#[macro_use]
extern crate litcrypt;

use_litcrypt!("N0_on3_wiLL_3v3r_fIgUrE_0ut_th!s_$up3R_SEcr3t_Phr4se");

fn main() {
	print!("Enter your password: ");
	let mut password = String::new();
	let _ = io::stdout().flush();
	io::stdin().read_line(&mut password).unwrap();
	check(&password);
}

fn check(password: &String) {
	let enc_flag = decode("240b316248312741432a1c710476335e500c463a20461405566f412a4076454c").unwrap();
	if verify(password) {
		let pass = decode(encode(password.trim())).unwrap();
		let flag: Vec<u8> = enc_flag
			.iter()
			.zip(pass.iter())
			.map(|(&b1, &b2)| b1 ^ b2)
			.collect();
		print!("correct!: ");
		for f in flag {
			print!("{}", f as char)
		}
		println!();
	} else {
		println!("Wrong!");
	}
}

fn verify(x: &String) -> bool {
	let secret: String = lc!("tHe$3cRetunBr3Akab!ep4$$w0rD!1!1");
	if x.trim().len() != secret.len() {
		return false;
	}
	for (i, j) in x.trim().chars().zip(secret.chars()) {
		if i != j {
			return false;
		}
	}
	return true;
}
