from flask import Flask, jsonify, request, Response
import os
from app import main

app = Flask(__name__)


# @app.route("/get", methods=["GET"])
# def get_data():
#     data = {"api_key": api_key}
#     return jsonify(data)


@app.route("/sendQuery", methods=["POST"])
def get_post_data():
    json = request.json
    query = json["query"]
    return Response(main.query(query), content_type="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT", default=5000), debug=True)
