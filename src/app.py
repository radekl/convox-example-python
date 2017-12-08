from flask import Flask

# the all-important app variable:
app = Flask(__name__)

@app.route("/", defaults={"path":""})
@app.route("/<path:path>")
def hello(path):
    return "Oh, Hello World. v7 Your path: %s" % path

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=3000)
