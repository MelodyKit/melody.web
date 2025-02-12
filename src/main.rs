use clap::Parser;
use melody_web::app::App;
use miette::Result;

fn main() -> Result<()> {
    App::parse().run()?;

    Ok(())
}
