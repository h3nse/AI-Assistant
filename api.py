from flask import Flask, jsonify, request
import os

app = Flask(__name__)

api_key: str = os.getenv("API_KEY")


@app.route("/get", methods=["GET"])
def get_data():
    data = {"api_key": api_key}
    return jsonify(data)


@app.route("/post", methods=["POST"])
def get_post_data():
    json = request.json
    print(json)
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT", default=5000), debug=False)
