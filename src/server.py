from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Bora dormir!now and now"

if __name__ == "__main__":
    # app.run(host="127.0.0.0")
        app.run()