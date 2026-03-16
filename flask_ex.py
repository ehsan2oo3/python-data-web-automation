from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to My Flask App!"

@app.route("/api/data")
def data():
    return jsonify({"message": "Hello, this is my API endpoint!"})

if __name__ == "__main__":
    app.run(debug=True)