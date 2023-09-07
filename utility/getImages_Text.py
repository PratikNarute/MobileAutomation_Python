import base64

from PIL import Image
import pytesseract
import io

@staticmethod
def getText(driver):
    screenshot = driver.get_screenshot_as_base64()
    # Convert the base64-encoded image to a Pillow Image object
    image_data = io.BytesIO(base64.b64decode(screenshot))
    screenshot_image = Image.open(image_data)
    # Use pytesseract to extract text from the screenshot
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # Update with your Tesseract path on Windows
    # Use pytesseract to extract text from the screenshot
    text = pytesseract.image_to_string(screenshot_image)
    print(text)
    return text