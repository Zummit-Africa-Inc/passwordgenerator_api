from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from password_function import password_generator

app = FastAPI(title='API for password generator')


app = FastAPI(
    title="Password Generator API",
    description="""An API for generating strong and secure passwords."""
)


@app.get("/", response_class=PlainTextResponse, tags=["home"])
async def home():
    note = """
    Password Generator API
    An API for generating strong and secure passwords!
    Note: add "/redoc" to get the complete documentation.
    """
    return note


@app.get("/password", tags=['Password'])
def generate_password() -> dict:
    return {"password": password_generator()}
