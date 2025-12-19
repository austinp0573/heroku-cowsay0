# Cowsay as a Service

A web app that generates ASCII art using cowsay and various characters. Built with FastAPI and deployed on Heroku.

**Live:** [https://caas.tusko.org](https://caas.tusko.org)

## Background

I had some free Heroku credits and wanted to deploy something that wasn't just a tutorial project. Cowsay seemed like a fun candidate since it's simple but could be made into something actually usable. The initial version was pretty rough - just some inline HTML strings in a single Python file. It worked, but it wasn't something I'd want anyone to actually use.

After getting the basic functionality working, I went back and spent time making it better. The main things I wanted to address were proper project structure, mobile usability, and making it look like an actual application instead of a quick hack.

## What I Learned

**Project structure**: Started with everything crammed into one file with inline HTML. Refactored to use Jinja2 templates properly, separated concerns, and organized it in a way that would actually be maintainable if I wanted to add features later.

**Mobile-first design**: Most people would access this from their phones, so I spent time getting the viewport scaling right. Small ASCII art should scale up to fill the screen, large stuff like the dragon needs to scale down to fit. Getting the math right on the container sizing took some iteration but it was worth it to make it actually pleasant to use on mobile.

**UI/UX considerations**: The original version assumed people knew what cowsay was and which characters existed. Added better labels, changed the default message to something less generic, and implemented localStorage so returning users don't have to re-enter everything. Small things, but they make it more approachable.

**Dark theme implementation**: Wanted to give it some personality beyond default browser styles. Went with a dark theme inspired by GitHub's UI - it fits the "hacker tool" vibe of cowsay while still being readable and polished.

## Features

- Select from 50+ ASCII art characters
- Generate custom messages with any character
- Automatic mobile viewport scaling (zooms appropriately based on output size)
- Copy output to clipboard
- Remembers your last character and message (localStorage)
- Dark theme with proper focus states and transitions
- Deployed on Heroku with custom domain

## Tech Stack

- **Backend**: FastAPI (Python 3.13)
- **Frontend**: Jinja2 templates, vanilla JavaScript
- **Deployment**: Heroku with uvicorn
- **ASCII art**: python-cowsay library

## Running Locally

**Prerequisites**: Python 3.13+ (might work on earlier versions but untested)

Clone the repository:
```bash
git clone https://github.com/austinp0573/heroku-cowsay0.git
cd heroku-cowsay0
```

Set up a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the development server:
```bash
uvicorn main:app --reload
```

The app will be available at [http://localhost:8000](http://localhost:8000)

The `--reload` flag enables hot reloading, so changes to Python files will automatically restart the server. Template changes are picked up immediately.

## Deployment

See [DEPLOY.md](DEPLOY.md) for complete deployment instructions including Heroku setup and custom domain configuration.

## License

This project is licensed under the **GNU AGPLv3** License.
This is largely the first public deployment of an application that I've done, and while this code could have been written by someone on their first day learning python, and something like this probably already exists somewhere, I think open source matters. Aside from my Nvidia driver script, there's not really much in my repositories that anyone other many me uses, and I really like the idea of making things that others can use and benefit from for free. Given the simplicity of the project source, a license is sort of moot, but I put this here, because I think Open Source, and copy left matter.
See the LICENSE file for details.

&nbsp;

**466f724a616e6574**