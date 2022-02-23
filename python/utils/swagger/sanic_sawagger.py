import Levenshtein
import pandas as pd
import numpy as np
from speech_model import ModelSpeech
from speech_model_zoo import SpeechModel251
from speech_features import Spectrogram
from LanguageModel2 import ModelLanguage
from utils.ops import read_wav_data

# for api server
import base64
import json
import os
from pathlib import Path
from datetime import datetime
from uuid import uuid4
from sanic import Sanic
from sanic.response import json
from app.constant import project_path

# sanic swagger
from sanic_openapi import swagger_blueprint, openapi
from sanic_openapi import doc, openapi2_blueprint
import warnings

warnings.simplefilter("ignore", DeprecationWarning)

# for asrt code
AUDIO_LENGTH = 1600
AUDIO_FEATURE_LENGTH = 200
CHANNELS = 1
# 默认输出的拼音的表示大小是1428，即1427个拼音+1个空白块
OUTPUT_SIZE = 1428
sm251 = SpeechModel251(
    input_shape=(AUDIO_LENGTH, AUDIO_FEATURE_LENGTH, CHANNELS),
    output_size=OUTPUT_SIZE
)
feat = Spectrogram()
ms = ModelSpeech(sm251, feat, max_label_length=64)
ms.load_model(str(Path(project_path, 'app/save_models')) + '/' + sm251.get_model_name() + '.model.h5')
ml = ModelLanguage('model_language')
ml.LoadModel()
# 加载依赖文件
df_std = pd.read_csv(str(Path(project_path, 'app/dependence/drop_dup_std.csv')))
std_hanzi = df_std['std_hanzi'].tolist()
cor_pinyin = df_std['cor_pinyin'].tolist()

##
# for swagger 注册app
app = Sanic("gxt_asrt")
app.blueprint(swagger_blueprint)


def asrt_pinyin(wavs, fs):
    r = ''
    try:
        r = ms.recognize_speech(wavs, fs)
    except Exception as ex:
        r = ''
        print('[*Message] Server raise a bug. ', ex)
        # print('[pingyin] ', r)
    return r


# 修改为async函数, 传入Path对象的地址.
async def recognize_from_path(pth, threshold=0.45):
    wavsignal, fs, _, _ = read_wav_data(pth)
    if len(wavsignal) > 0:
        r = asrt_pinyin(wavsignal, fs)
        en_s = ''.join([c for word in r for c in word if not c.isdigit()])
        dis = [Levenshtein.distance(en_s, p) / len(p) for p in cor_pinyin]
        if min(dis) > threshold:
            buf = "unknown"
        else:
            buf = std_hanzi[np.argmin(dis)]
    else:
        buf = "unknown"

    return buf


# 将swagger前端上传的文件字节内容, 写入保存为wav文件
def generate_file(bytes_file):
    now_datetime = datetime.now()
    wav_path = Path(project_path, 'data/tmp', str(now_datetime.strftime('%Y%m%d%H%M%S') + f'-{uuid4()}.wav'))

    with open(wav_path, 'wb') as wf:
        wf.write(bytes_file)

    return wav_path


@doc.tag("语音识别服务")
@app.post("/asrt")
@doc.description("请传入wav文件请求, 返回识别后的结果")
@doc.consumes(
    doc.File(name="file"), location="formData", content_type="multipart/form-data"
)
@doc.response(200, {"size": doc.Integer(), "type": doc.String(), 'res': str}, description="Response body")
async def asrt(request):
    file = request.files.get("file")
    size = len(file.body)

    bytes_file = file.body
    wav_path = generate_file(bytes_file)

    res = await recognize_from_path(str(wav_path))

    if Path.exists(wav_path):
        os.remove(wav_path)

    return json({"size": size, "type": file.type, 'res': res}, ensure_ascii=False)


if __name__ == "__main__":
    app.run()
