from flask import Flask, send_file
from pathlib import Path

from common.constant import IMG_WORN_PATH, IMG_ORIGIN_PATH, IMG_PERSON_PATH

app = Flask(__name__)


@app.route("/image/<date>/<image_id>")
def index(date, image_id):
    # 图片名格式: 通道_日期时间.png
    image = Path(IMG_PERSON_PATH, f'{date}/{image_id}')
    resp = send_file(image, mimetype='image/jpeg')
    return resp


@app.route("/origin/<date>/<image_id>")
def origin(date, image_id):
    image = Path(IMG_ORIGIN_PATH, f'{date}/{image_id}')
    resp = send_file(image, mimetype='image/jpeg')
    return resp


@app.route("/worn/<date>/<image_id>")
def worn(date, image_id):
    image = Path(IMG_WORN_PATH, f'{date}/{image_id}')
    resp = send_file(image, mimetype='image/jpeg')
    return resp


if __name__ == '__main__':
    app.run()
