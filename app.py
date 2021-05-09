from flask import Flask, request, Response, redirect, url_for
import json

app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
    return redirect(url_for("api"))


@app.route('/test', methods=["GET","POST"])
def api():
    if request.method == "POST":
        print(request.form)
        print(request.files)
        data = {
            "data": str(request.form['data'])
        }
    else:
        data = "You've requested with get method"
    return Response(response=json.dumps(data), status=200)


if __name__ == "__main__":
    app.run(debug=True)