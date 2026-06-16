import subprocess
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    result = subprocess.check_output(
        ["ffmpeg", "-version"]
    ).decode("utf-8")

    return f"<pre>{result}</pre>"
