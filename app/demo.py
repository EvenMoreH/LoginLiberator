from fasthtml.common import *
from asyncio import sleep
from scripts import *


def user_auth(req, session):
    if not session.get("auth"):
        return login_redirect

bware = Beforeware(user_auth, skip=[
    r"^/login$",             # exact match
    r"^/captcha$",           # exact match
    r"^/solve$",
    r"^/static/.*",          # any file under /static/
    r"^/css/.*",             # # any file under /css/
    r"^/favicon\.ico$",      # literal favicon.ico
])

app, rt = fast_app(before=bware, static_path="app/static")

default_header = Head(
                    Title("demo_page"),
                    Meta(charset="UTF-8"),
                    Meta(name="viewport", content="width=device-width, initial-scale=1"),
                    Meta(name="description", content="demo_page"),
                    Meta(name="author", content="EvenMoreH"),
                    Script(src="https://unpkg.com/htmx.org"),
                    Link(rel="stylesheet", href="css/tailwind.css"),
                    Link(rel="icon", href="images/favicon.ico", type="image/x-icon"),
                    Link(rel="icon", href="images/favicon.png", type="image/png"),
                )

DEMO_USER = "admin"
DEMO_PASSWORD = "admin1"

CAPTCHA_PASS = "passed"

@dataclass
class LoginForm:
    username: str
    password: str

login_redirect = RedirectResponse("/login", status_code=303)
captcha_redirect = RedirectResponse("/captcha", status_code=303)

@rt("/captcha")
def get(session):
    session.get("captcha")
    session["captcha"] = ""

    return Html(
        default_header,
        Body(
            Script(captcha_button),
            Script(captcha_message),
            H1("CAPTCHA Demo", cls="pt-8 pb-1 text-2xl text-center"),
            Div(
                P("I am a robot!", id="robotP", cls="w-64 p-4 m-2 items-center text-center font-semibold"),
                Form(
                    Label(
                        Input(type="checkbox", name="captcha", id="captcha-box", required=True,
                            onclick="captchaMessage()",
                            cls="scale-150 p-2 m-2")
                    ),
                    Button("Verify", type="submit", id="verify-btn",
                            onclick="captchaSuccess()",
                            cls="btn"
                        ),
                    action="solve", method="post",
                    cls="flex flex-row justify-center items-center",
                ),
                cls="flex flex-col justify-center items-center",
            ),
            # whole body CSS
            cls="body"
        ),
    lang="en",
    )

@rt("/solve")
async def post(req, session):
    session["captcha"] = CAPTCHA_PASS
    await sleep(2)
    return login_redirect


@rt("/login")
def get(session):
    captcha = session.get("captcha")
    if not captcha == CAPTCHA_PASS:
        return captcha_redirect
    else:
        return Html(
            default_header,
            Body(
                H1("Login", cls="pt-4 pb-1 text-2xl"),
                Form(
                    Input(name="username", placeholder="Username", cls="input"),
                    Input(name="password", placeholder="Password", cls="input"),
                    Button("Login", type="submit", cls="btn"),
                    action="login", method="post"
                ),
                # whole body CSS
                cls="body"
            ),
        lang="en",
        )

@rt("/login")
def post(data: LoginForm, session):
    if data.username == DEMO_USER and data.password == DEMO_PASSWORD:
        session["auth"] = data.username
        return RedirectResponse("/", status_code=303)
    else:
        return Html(
            default_header,
            Body(
                H1("Login Failed", cls="pt-4 pb-1 text-2xl text-center"),
                Div(
                    P("Invalid Credentials. Try again.", cls="p-2 m-2"),
                    A("Retry", href="/login", hx_push_url="true", cls="btn"),
                    cls="flex flex-col justify-center items-center"
                ),
                # whole body CSS
                cls="body"
            ),
        lang="en",
        )


@rt("/")
def get():
    return Html(
        default_header,
        Body(
            H1("Hello There", cls="pt-8 pb-1 mb-4 text-2xl text-center"),
            Div(
                A("Reset the Page", href="/back", hx_push_url="true", cls="btn"),
                cls="flex justify-center"
            ),
            # whole body CSS
            cls="body"
        ),
    lang="en",
    )


@rt("/back")
def get(session):
    session.get("auth")
    session.get("captcha")
    session["auth"] = ""
    session["captcha"] = ""
    print("\t  >> Resetting the page...")
    return RedirectResponse("/", status_code=303)


serve()