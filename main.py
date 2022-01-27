from flask import Flask
from views import *
from utils import Console
import waitress
import socket
import logging


class Server(Flask):
    def __init__(self):
        super().__init__(__name__, template_folder="./templates", static_folder="./static", static_url_path="")
        self.console = Console()
        log = logging.getLogger("waitress.queue")
        log.disabled = True
        self.register_blueprints()

    def register_blueprints(self):
        self.register_blueprint(Root(self).blueprint, url_prefix="/")

    def start(self, host, port):
        self.console.server_log(f"Listening on http://{socket.gethostbyname(socket.gethostname())}:{port}/")
        try:
            waitress.serve(self, host=host, port=port)
        except Exception as e:
            self.console.error_log(e, f"line={e.__traceback__.tb_frame.f_lineno}")


if __name__ == '__main__':
    server = Server()
    server.start("0.0.0.0", 80)
