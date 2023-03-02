from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("img.png")

# Pillow 가 설치되어 있어야함
ws.add_image(img, "C3") # C3위치에 img.png파일의 이미지를 삽임

wb.save("sample_image.xlsx")