// use std::env;
use hex::FromHex;
use roxmltree;
use std::fs;

fn main() {
    let content = fs::read_to_string("flag.svg").expect("File not found");

    let doc = roxmltree::Document::parse(content.as_str());
    match doc {
        Ok(d) => {
            for node in d.descendants().filter(|n| {
                (n.tag_name().name() == "text") && n.attribute("font-size") == Some("8")
            }) {
                let encrypted_flag = node.text().unwrap();
                let num = <[u8; 1]>::from_hex(encrypted_flag.trim().replace("0h", "")).unwrap()[0];
                let decrypted_flag = ((((num as u16) << 2) ^ 10) >> 2) as u8;
                print!("{}", char::from(decrypted_flag));
            }
        }
        Err(_) => {}
    }
}
