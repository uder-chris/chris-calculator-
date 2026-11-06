from PIL import Image, ImageDraw, ImageFont
img = Image.new("RGB", (512, 512), "#16a34a")
d = ImageDraw.Draw(img)
# Fremu ya calculator
d.rounded_rectangle([96, 96, 416, 416], radius=40, fill="white")
# Screen
d.rounded_rectangle([136, 136, 376, 200], radius=15, fill="#16a34a")
# Buttons
for y in [232, 296]:
    for x in [136, 216, 296]:
        d.rounded_rectangle([x, y, x+64, y+48], radius=10, fill="#dcfce7")
d.rounded_rectangle([136, 360, 376, 408], radius=10, fill="#16a34a")
img.save("icon.png")
print("icon mpya done")
