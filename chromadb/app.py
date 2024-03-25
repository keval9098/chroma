import chromadb
import chromadb.config
from chromadb.server.fastapi import FastAPI
from fastapi import applications
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html

settings = chromadb.config.Settings()
server = FastAPI(settings)
app = server.app()
app.mount("/static", StaticFiles(directory="./static"), name="static")
def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args,
        **kwargs,
        swagger_js_url="/static/bundle.js",
        swagger_css_url="/static/swaggerui.css",
    )
applications.get_swagger_ui_html = swagger_monkey_patch