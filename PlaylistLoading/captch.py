from captcha.image import ImageCaptcha 
from PIL import Image
import random

# Specify the image size
image = ImageCaptcha(width=450, height=100)
# Generate random captcha text
def generate_random_captcha_text(length=6):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    captcha_text = ''.join(random.choice(characters) for _ in range(length))
    return captcha_text
# Get random captcha text
captcha_text = generate_random_captcha_text()
# Generate the image of the given text
data = image.generate(captcha_text)
# Write the image on the given file and save it
image.write(captcha_text, 'CAPTCHA1.png')
Image.open('CAPTCHA1.png')