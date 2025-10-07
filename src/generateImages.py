from PIL import Image, ImageDraw

# Medidas del lienzo e imagen
canvas_size = (100, 100)
w, h = 30, 50  # ancho y alto del rectángulo

# ===== Imagen 1: rectángulo en (21, 21) =====
img1 = Image.new("RGB", canvas_size, "white")
draw1 = ImageDraw.Draw(img1)

x1, y1 = 21, 21
draw1.rectangle([x1, y1, x1 + w, y1 + h], outline="black", fill="black")

img1.save("src/resources/I_k-1.png")
img1.show()

# ===== Imagen 2: rectángulo en (31, 16) =====
img2 = Image.new("RGB", canvas_size, "white")
draw2 = ImageDraw.Draw(img2)

x2, y2 = 31, 16
draw2.rectangle([x2, y2, x2 + w, y2 + h], outline="black", fill="black")

img2.save("src/resources/I_k.png")
img2.show()