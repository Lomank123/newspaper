from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.routes import api_router

app = FastAPI()

# Routing
app.include_router(api_router, prefix='/api/v1')


# TODO: Remove after tests
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
