from flask import Flask, request, Response, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
    return redirect(url_for("api"))


@app.route('/test', methods=["GET","POST"])
def api():
    print(request.form)
    data = {
        "data": "some value"
    }
    return Response(response=data, status=200)


if __name__ == "__main__":
    app.run(debug=True)