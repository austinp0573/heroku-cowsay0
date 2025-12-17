
# Cowsay as a Service (CaaS)

Cowsay as a Service (CaaS) is a simple FastAPI web app that lets you generate cowsay (and other character) ASCII art in your browser. You can run it locally or deploy it to Heroku.

## Features
- Choose from multiple cowsay characters
- Enter your own message
- Copy the output easily

## Getting Started

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the app locally:
   ```
   uvicorn main:app --reload
   ```
3. Open your browser and go to:
   [http://localhost:8000/landing](http://localhost:8000/landing)

## Deploying to Heroku
See `DEPLOY.md` for step-by-step instructions to deploy this app to Heroku and set up a custom domain.

## License
This project is licensed under the **GNU AGPLv3** License.
This is largely the first public deployment of an application that I've done, and while this code could have been written by someone on their first day learning python, and something like this probably already exists somewhere, I think open source matters. Aside from my Nvidia driver script, there's not really much in my repositories that anyone other many me uses, and I really like the idea of making things that others can use and benefit from for free. Given the simplicity of the project source, a license is sort of moot, but I put this here, because I think Open Source, and copy left matter.
See the LICENSE file for details.

&nbsp;

**466f724a616e6574**