from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello DigiWAS ... building images!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=True)
