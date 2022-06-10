import flask

from chat import get_response

app = flask.Flask(__name__)


@app.get("/")
def index_get():
    return flask.render_template("base.html")


@app.post("predict")
def predict():
    text = flask.request.get_json().get("message")

    response = get_response(text)
    message = {"answer": response}
    return flask.jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)