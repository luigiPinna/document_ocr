import pytesseract
import PIL.Image
import cv2
import io
import config as conf


print("File content: ", conf.file)


my_config = r"--psm 6 --oem 3"
img_text = pytesseract.image_to_string(PIL.Image.open(conf.file_path), config=my_config)
print(img_text)