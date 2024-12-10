use std::borrow::Cow;

use maud::{html, Markup};

use crate::{
    date::{created, today, Datelike},
    templates::base::{base, head, HeadContext},
};

pub const TITLE: &str = "Home";
pub const DESCRIPTION: &str = "All your music, in one place.";

pub fn content() -> Markup {
    html! {
        nav class="absolute flex w-full" {
            div class="mx-auto max-w-md sm:max-w-3xl lg:max-w-7xl px-4 sm:px-6 lg:px-8 flex w-full items-center py-4" {
                a href="/" class="mr-auto flex items-center gap-4 lg:mr-12" {
                    object
                        type="image/svg+xml" data="/static/images/gradient.svg"
                        class="w-auto h-10 pointer-events-none" title="Logo" {}
                    h3 class="text-xl" { "MelodyKit" }
                }

                div class="hidden lg:flex lg:gap-x-12" {
                    a href="/download" class="hover-melody" { "Download" }
                    a href="/support" class="hover-melody" { "Support" }
                    a href="/premium" class="hover-melody" { "Premium" }
                }

                form class="relative ml-auto hidden md:block md:mr-10" action="/search" {
                    input class="
                        text-lg
                        h-10
                        rounded-xl
                        px-4
                        border-2
                        border-transparent
                        bg-neutral-300/50 dark:bg-black/50
                        placeholder-neutral-600 dark:placeholder-neutral-400
                        focus:border-neutral-500 dark:focus:border-neutral-700
                        focus:outline-none
                    " type="search" name="query" placeholder="Search";

                    button class="
                        absolute
                        right-0 top-0
                        mr-4 mt-2
                        text-neutral-600 dark:text-neutral-400
                    " aria-label="Search" type="submit" {
                        i class="fa-solid fa-search w-auto h-4" {}
                    }
                }

                a href="/open" class="
                    bg-gradient-to-b
                    from-melody-purple to-melody-blue
                    inline-flex
                    items-center justify-center
                    whitespace-nowrap
                    rounded-xl
                    px-4 py-2
                    text-xl
                    my-2
                " {
                    "Open"
                }
            }
        }

        div class="
            mx-auto
            max-w-md sm:max-w-3xl lg:max-w-7xl
            px-4 sm:px-6 lg:px-8
            flex flex-col lg:flex-row
            justify-between
            gap-5 pt-20
        " {
            div class="my-12 lg:my-24 w-full lg:w-1/2" {
                h1 class="text-5xl leading-none" {
                    span class="hover-melody" { "All" }
                    " " span class="hover-melody" { "your" }
                    " " span class="hover-melody" { "music" }
                    span class="hover-melody" { "," }
                    br;
                    span class="hover-melody" { "in" }
                    " " span class="hover-melody" { "one" }
                    " " span class="hover-melody" { "place" }
                    span class="hover-melody" { "." }
                }

                p class="text-xl text-neutral-600 dark:text-neutral-400 mt-4 mb-4" {
                    "Synchronize and listen to your favorite tracks across all music platforms."
                }

                a href="/intro" class="flex flex-row items-center gap-2 hover-melody hover:underline text-lg leading-none" {
                    "Watch the video" i class="w-auto h-4 fa-solid fa-arrow-right" {}
                }
            }
        }

        footer class="mx-auto max-w-md sm:max-w-3xl lg:max-w-7xl px-4 sm:px-6 lg:px-8 py-16" {
            div class="grid grid-cols-2 gap-y-4 lg:flex lg:flex-row lg:justify-between mb-8" {
                div class="ml-4 flex flex-col lg:ml-0" {
                    h4 class="mb-2 text-neutral-600 dark:text-neutral-400" { "MelodyKit" }
                    ul class="grid gap-2" {
                        li {
                            a href="/" class="hover-melody" { "Home" }
                        }
                        li {
                            a href="/status" class="hover-melody" { "Status" }
                        }
                    }
                }
                div class="ml-4 flex flex-col lg:ml-0" {
                    h4 class="mb-2 text-neutral-600 dark:text-neutral-400" { "Resources" }
                    ul class="grid gap-2" {
                        li {
                            a href="/download" class="hover-melody" { "Download" }
                        }
                        li {
                            a href="/support" class="hover-melody" { "Support" }
                        }
                        li {
                            a href="/premium" class="hover-melody" { "Premium" }
                        }
                        li {
                            a href="/dev" class="hover-melody" { "Developers" }
                        }
                    }
                }
                div class="ml-4 flex flex-col lg:ml-0" {
                    h4 class="mb-2 text-neutral-600 dark:text-neutral-400" { "Company" }
                    ul class="grid gap-2" {
                        li {
                            a href="/about" class="hover-melody" { "About" }
                        }
                        li {
                            a href="/contact" class="hover-melody" { "Contact" }
                        }
                    }
                }
                div class="ml-4 flex flex-col lg:ml-0" {
                    h4 class="mb-2 text-neutral-600 dark:text-neutral-400" { "Legal" }
                    ul class="grid gap-2" {
                        li {
                            a href="/privacy" class="hover-melody" { "Privacy" }
                        }
                        li {
                            a href="/terms" class="hover-melody" { "Terms" }
                        }
                    }
                }
            }

            div class="flex flex-row items-center justify-center" {
                a href="/discord" class="mx-4 flex flex-col lg:ml-0" aria-label="Discord" {
                    i class="w-auto h-8 fa-brands fa-discord text-discord" {}
                }
                a href="/x" class="mx-4 flex flex-col lg:ml-0" aria-label="X" {
                    i class="w-auto h-8 fa-brands fa-x-twitter" {}
                }
                a href="/reddit" class="mx-4 flex flex-col lg:ml-0" aria-label="Reddit" {
                    i class="w-auto h-8 fa-brands fa-reddit-alien text-reddit" {}
                }
                a href="/youtube" class="mx-4 flex flex-col lg:ml-0" aria-label="YouTube" {
                    i class="w-auto h-8 fa-brands fa-youtube text-youtube" {}
                }
                a href="/github" class="mx-4 flex flex-col lg:ml-0" aria-label="GitHub" {
                    i class="w-auto h-8 fa-brands fa-github" {}
                }
            }

            p class="min-w-full text-neutral-600 dark:text-neutral-400 text-center mt-8" {
                i class="fa-regular fa-copyright hover-melody" {}
                " MelodyKit " (created().year()) "-" (today().year()) "." " All rights reserved. "
                i class="fa-solid fa-heart hover-melody" {}
            }
        }
    }
}

pub fn index() -> Markup {
    base(
        &head(&HeadContext::new(
            Cow::Borrowed(TITLE),
            Cow::Borrowed(DESCRIPTION),
        )),
        &content(),
    )
}
