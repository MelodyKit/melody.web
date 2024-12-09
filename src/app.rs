use axum::serve;
use clap::Parser;
use miette::Diagnostic;
use thiserror::Error;
use tokio::{net::TcpListener, runtime::Builder};
use tower_http::services::ServeDir;

use crate::{routes::router, types::Port};

pub const STATIC: &str = "/static";
pub const STATIC_PATH: &str = "static";

pub const DEFAULT_HOST: &str = "127.0.0.1";
pub const DEFAULT_PORT: Port = 4269;

#[derive(Debug, Parser)]
pub struct App {
    /// The host to run on.
    #[arg(
        short = 'H',
        long,
        name = "HOST",
        help = "Run on this host",
        default_value_t = DEFAULT_HOST.to_owned()
    )]
    pub host: String,

    /// The port to run on.
    #[arg(
        short = 'p',
        long,
        name = "PORT",
        help = "Run on this port",
        default_value_t = DEFAULT_PORT
    )]
    pub port: Port,
}

impl App {
    pub fn run(self) -> Result<(), Error> {
        run(self.host, self.port)
    }
}

#[derive(Debug, Error, Diagnostic)]
#[error("failed to bind to `{host}:{port}`")]
#[diagnostic(
    code(melody_web::app::bind),
    help("make sure the address is valid and accessible")
)]
pub struct BindError {
    pub source: std::io::Error,
    pub host: String,
    pub port: Port,
}

impl BindError {
    pub fn new(source: std::io::Error, host: String, port: Port) -> Self {
        Self { source, host, port }
    }
}

#[derive(Debug, Error, Diagnostic)]
#[error("serve failed")]
#[diagnostic(
    code(melody_web::app::serve),
    help("see the report for more information")
)]
pub struct ServeError(#[from] pub std::io::Error);

#[derive(Debug, Error, Diagnostic)]
#[error(transparent)]
#[diagnostic(transparent)]
pub enum RunErrorSource {
    Bind(#[from] BindError),
    Serve(#[from] ServeError),
}

#[derive(Debug, Error, Diagnostic)]
#[error("failed to asynchronously run")]
#[diagnostic(
    code(melody_web::app::async_run),
    help("see the report for more information")
)]
pub struct RunError {
    #[source]
    #[diagnostic_source]
    pub source: RunErrorSource,
}

impl RunError {
    pub fn new(source: RunErrorSource) -> Self {
        Self { source }
    }

    pub fn bind(error: BindError) -> Self {
        Self::new(error.into())
    }

    pub fn serve(error: ServeError) -> Self {
        Self::new(error.into())
    }

    pub fn new_bind(error: std::io::Error, host: String, port: Port) -> Self {
        Self::bind(BindError::new(error, host, port))
    }

    pub fn new_serve(error: std::io::Error) -> Self {
        Self::serve(ServeError(error))
    }
}

#[derive(Debug, Error, Diagnostic)]
#[error("failed to build runtime")]
#[diagnostic(
    code(melody_web::app::build),
    help("see the report for more information")
)]
pub struct BuildError(#[from] pub std::io::Error);

#[derive(Debug, Error, Diagnostic)]
#[error(transparent)]
#[diagnostic(transparent)]
pub enum ErrorSource {
    Build(#[from] BuildError),
    Run(#[from] RunError),
}

#[derive(Debug, Error, Diagnostic)]
#[error("failed to run")]
#[diagnostic(
    code(melody_web::app::run),
    help("see the report for more information")
)]
pub struct Error {
    #[source]
    #[diagnostic_source]
    pub source: ErrorSource,
}

impl Error {
    pub fn new(source: ErrorSource) -> Self {
        Self { source }
    }

    pub fn build(error: BuildError) -> Self {
        Self::new(error.into())
    }

    pub fn run(error: RunError) -> Self {
        Self::new(error.into())
    }

    pub fn new_build(error: std::io::Error) -> Self {
        Self::build(BuildError(error))
    }
}

pub async fn async_run<H: AsRef<str> + Send>(host: H, port: Port) -> Result<(), RunError> {
    let host = host.as_ref();

    let listener = TcpListener::bind((host, port))
        .await
        .map_err(|error| RunError::new_bind(error, host.to_owned(), port))?;

    let app = router().nest_service(STATIC, ServeDir::new(STATIC_PATH));

    serve(listener, app).await.map_err(RunError::new_serve)
}

pub fn run<H: AsRef<str> + Send>(host: H, port: Port) -> Result<(), Error> {
    let runtime = Builder::new_multi_thread()
        .enable_all()
        .build()
        .map_err(Error::new_build)?;

    runtime.block_on(async_run(host, port)).map_err(Error::run)
}
