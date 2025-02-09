use std::process::Command;

pub const CSS: &str = "tailwindcss";
pub const INPUT: &str = "--input";
pub const OUTPUT: &str = "--output";
pub const MINIFY: &str = "--minify";

pub const INPUT_PATH: &str = "static/css/input.css";
pub const OUTPUT_PATH: &str = "static/css/output.css";

fn main() {
    Command::new(CSS)
        .arg(INPUT)
        .arg(INPUT_PATH)
        .arg(OUTPUT)
        .arg(OUTPUT_PATH)
        .arg(MINIFY)
        .status()
        .unwrap();
}
