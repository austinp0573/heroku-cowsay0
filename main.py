# Copyright (C) 2025 Austin P.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
        <pre id="cowsay-output">{output}</pre>
        <button onclick="copyToClipboard()">COPY TO CLIPBOARD</button>
        <br><br>
        <a href="/landing"><button>GO BACK and MAKE A NEW ONE</button></a><br>
        <br><br>
        <a href='https://github.com/austinp0573/heroku-cowsay0' target='_blank'>Project Repository</a>
        <br><br>
        <a href='https://github.com/austinp0573' target='_blank'>My GitHub</a>
        <br><br>
        466f724a616e6574
        <script>
        function copyToClipboard() {{
            const text = document.getElementById('cowsay-output').innerText;
            navigator.clipboard.writeText(text);
        }}
        </script>
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
