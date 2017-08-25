from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def homepage():
    try:
        metadata_url = request.args["metadata"]
        biom_url = request.args["biom"]
    except:
        return "ERROR"

    return metadata_url


    return "NONE"
