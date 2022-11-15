import pyocr as ocr
import pyocr.builders
from PIL import Image

def main():
	img_path = "test.ong"

	tools = pyocr.get_available_tools()
	if len(tools) == 0:
		print("No OCR tool found")
		sys.exit(1)

	tool = tools[0]
	res = tool.image_to_string(Image.open(img_path),
							builder=pyocr.builders.TextBuilder(tesseract_layout=6))
	print(res)

if __name__ == '__main__':
	main()