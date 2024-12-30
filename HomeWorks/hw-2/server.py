from flask import Flask
from flask import jsonify
from dotenv import dotenv_values

app = Flask(__name__)


@app.route("/")
def server_info() -> str:
    return "My Server"


@app.route("/author")
def author():
    author_data = {
        "name": "Nazar",
        "course": 2,
        "age": 19
    }
    return jsonify(author_data)


def get_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return int(config["PORT"])
    return 5000


def debug_status() -> bool:
    config = dotenv_values(".env")
    if "DEBUG" in config:
        return bool(config["DEBUG"])
    return False


if __name__ == "__main__":
    app.run(debug=debug_status(), port=get_port())
