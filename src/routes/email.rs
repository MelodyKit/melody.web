use axum::{extract::Path, response::Redirect, routing::get, Router};

async fn redirect_email(Path(name): Path<String>) -> Redirect {
    let uri = format!("mailto:{name}@melodykit.app");

    Redirect::to(&uri)
}

pub fn router() -> Router<()> {
    Router::new().route("/{name}", get(redirect_email))
}
