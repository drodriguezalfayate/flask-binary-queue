from flask import Flask
from flask import request


# Para ejecutar la función de procesado que emitirá la respuesta al otro extremo
# no hacemos mucho, en realidad
from queue_app_provider.AppProvider import AppProvider
from queue_app_provider.HandlerOutput import HandlerOutput


def process(file):
    print(file)
    return HandlerOutput(success=True, text="prueba")


app_provider = AppProvider(handler=process)

app = Flask(__name__)


@app.route("/send", methods=['POST'])
def upload():
    return app_provider.process(request)
