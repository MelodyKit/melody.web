use std::process::Command;

pub const DENO: &str = "deno";
pub const TASK: &str = "task";
pub const BUILD: &str = "build";

fn main() {
    Command::new(DENO).arg(TASK).arg(BUILD).status().unwrap();
}
