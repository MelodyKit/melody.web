use axum::{extract::Path, response::Redirect, routing::get, Router};

pub const PROJECTS: &str = "https://github.com/MelodyKit";

async fn redirect_projects(Path(name): Path<String>) -> Redirect {
    let url = format!("{PROJECTS}/{name}");

    Redirect::to(&url)
}

pub fn router() -> Router<()> {
    Router::new().route("/{name}", get(redirect_projects))
}
