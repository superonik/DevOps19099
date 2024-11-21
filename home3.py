
from PIL import Image, ImageDraw, ImageFont

try:
    a = 1 / 0
except:

    print("Dividing by zero !!!!!:")

try :
    x = 1
finally:
    print("finally")


with open("e:/words.txt", 'a') as f:
    f.write("RONEN\n")
with open("e:/words.txt", 'r') as f:
    str = f.read()
    print(str)
with open("e:/words.txt", 'a',encoding='utf-8') as f:
    f.write(input("\n תכתוב משהו בעברית\n"))
with open("e:/words.txt", 'r',encoding='utf-8') as f:
    str = f.read()
    print(str)




# Create a new image with a white background
width, height = 400, 200
image = Image.new("RGB", (width, height), "blue")

# Create a drawing context
draw = ImageDraw.Draw(image)

# Define a font and size
font = ImageFont.load_default()

# Define text and position
text = "Hello, RONEN!"
text_position = (175, 80)

# Draw text on the image
draw.text(text_position, text, fill="red", font=font)

# Save the image to a PNG file
image.save("e:/output_image.png")

print("Image created and saved as 'output_image.png'")



