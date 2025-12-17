from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse, HTMLResponse, RedirectResponse
import cowsay as cs

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/landing")

@app.get("/", response_class=PlainTextResponse)
def welcome():
    return "Welcome to CaaS (Cowsay as a Service). Try /cowsay?message=Hello"

from fastapi.responses import HTMLResponse

@app.get("/cowsay", response_class=HTMLResponse)
def draw_cow(message: str = "Moo", character: str = "default"):
    char_list = cs.list_cows()
    if character not in char_list:
        return HTMLResponse(
            f"<p>Character not found. Try: {', '.join(char_list)}</p>"
            '<a href="/landing"><button>Back to landing</button></a>',
            status_code=404,
        )
    output = cs.cowsay(message, cow=character)
    return f"""
    <html>
      <body>
        <pre>{output}</pre>
        <a href="/landing"><button>DO IT AGAIN!!! YAY!!!</button></a><br>
        <br><br>
        <a href='https://github.com/austinp0573' target='_blank'>My GitHub</a>
        <br><br>
        466f724a616e6574
      </body>
    </html>
    """

@app.get("/landing", response_class=HTMLResponse)
def landing():
    char_list = cs.list_cows()
    options = "".join([f'<option value="{c}">{c}</option>' for c in char_list])
    return f"""
    <html>
      <body>
        <h1>Cowsay as a Service</h1>
        <form action="/cowsay" method="get">
          <label for="character">Character:</label>
          <select name="character" id="character">
            {options}
          </select>
          <br><br>
          <label for="message">Message:</label>
          <input type="text" id="message" name="message" value="Hello!">
          <br><br>
          <input type="submit" value="Say!">
        </form>
      </body>
    </html>
    """
