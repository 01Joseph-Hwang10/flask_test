import io
from flask import Flask, request, Response, redirect, url_for
from werkzeug.utils import format_string
from bs4 import BeautifulSoup
import markdown
from flask.helpers import send_file
from PIL import Image, ImageDraw
import root

app = Flask(__name__)


app.register_blueprint(root.bp)


@app.route("/test", methods=["GET", "POST"])
def api():
    if request.method == "POST":
        print(request.form)
        print(request.files)
        data = {"data": str(request.form["data"])}
    else:
        data = {"data": "You've requested with get method"}
    return Response(response=data, status=200, mimetype="application/json")


@app.route("/image", methods=["GET"])
def get_image():
    im = Image.new("L", size=(100, 100))
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)
    fp = io.BytesIO()
    im.save(fp, format="PNG")
    fp = fp.getvalue()
    print(type(fp))
    return Response(response=fp, status=200, mimetype="image/*")
    # return Response(response=json.dumps("Got image successful"), status=200)


@app.route("/text", methods=["GET"])
def get_csv():
    return Response(
        response=open("./static/some_text.txt", "rb"), status=200, mimetype="text/*"
    )


@app.route("/html", methods=["GET"])
def get_html():
    # with  as f:
    #     soup = BeautifulSoup(f, "html.parser")
    #     for s in soup.select("script"):
    #         s.extract()
    #     for s in soup.select("iframe"):
    #         s.extract()
    #     for s in soup.select("link"):
    #         s.extract()
    return send_file(open("./static/test.html", "rb"), mimetype="text/html")


@app.route("/audio", methods=["GET"])
def get_audio():
    result = open("./static/example_audio.mp3", "rb")
    return Response(response=result, status=200, mimetype="audio/*")


@app.route("/markdown", methods=["GET"])
def get_markdown():
    result = open("./static/readme.md", "r")
    codelines = result.read()
    converted = markdown.markdown(codelines)
    result.close()
    return Response(response=converted, status=200, mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=True)
