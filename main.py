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

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import cowsay as cs

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def landing(request: Request):
    char_list = cs.list_cows()
    return templates.TemplateResponse("landing.html", {
        "request": request,
        "characters": char_list
    })

@app.get("/cowsay")
def draw_cow(request: Request, message: str = "Moo", character: str = "default"):
    char_list = cs.list_cows()
    if character not in char_list:
        return templates.TemplateResponse("character_not_found.html", {
            "request": request,
            "available_characters": ", ".join(char_list)
        }, status_code=404)
    
    output = cs.cowsay(message, cow=character)
    return templates.TemplateResponse("cowsay.html", {
        "request": request,
        "output": output,
        "message": message,
        "character": character
    })
