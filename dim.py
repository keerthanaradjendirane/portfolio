from PIL import Image

img = Image.open("gdsc.png")
img = img.resize((300,200))  # e.g., (300, 200)
