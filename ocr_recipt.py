# ocr_card.py
import os
from PIL import Image
import pyocr
import pyocr.builders

pyocr.tesseract.TESSERACT_CMD = r'C:\env\Tesseract\tesseract.exe'

# 1.インストール済みのTesseractのパスを通す
# path_tesseract = 'C:\env\Tesseract'
# if path_tesseract not in os.environ["PATH"].split(os.pathsep):
#     os.environ["PATH"] += os.pathsep + path_tesseract

# 2.OCRエンジンの取得
tools = pyocr.get_available_tools()
print(tools)
tool = tools[0]

# 3.原稿画像の読み込み
img_org = Image.open("./recipt_1_01.jpeg")

# 4.ＯＣＲ実行
builder = pyocr.builders.TextBuilder()
result = tool.image_to_string(img_org, lang="jpn", builder=builder)

print(result)