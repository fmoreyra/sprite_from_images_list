from PIL import Image

# 1. Crear imagen con pillow

image = Image.new("RGB", (128, 128))
image.save("./trail2.jpeg", "JPEG", progressive=True)

# 2. Abrir imagen con pillow

with Image.open("piso1.jpg") as im:
    im.show()


# 3. abrir y achicar imagen

with Image.open("piso1.jpg") as im:
    # (width, height) = (im.width // 2, im.height // 2)
    width = 288
    height = (width * 9) // 16
    im_resized = im.resize((width, height))
    im_resized.save("./resized_with_60_quality.jpg", "JPEG", progressive=True, quality=60)

# 4. abrir dos imagenes y ponerlas una debajo de la otra
n_img = 2
width = 1920
height = ((width * 9) // 16) * n_img

x = 0
y = 0

sprite = Image.new("RGB", (width, height))
with Image.open("piso1.jpg") as im:
    sprite.paste(im, (x, y))
with Image.open("piso2.jpg") as im2:
    y = height // 2
    sprite.paste(im2, (x, y))

sprite.save("./sprite1.jpg", "JPEG")

# 5. abrir dos imagenes, achicarlas y ponerlas una debajo de la otra

n_img = 2
width = 192
height = ((width * 9) // 16) * n_img

im_width = 192
im_height = (width * 9) // 16

x = 0
y = 0

sprite = Image.new("RGB", (width, height))
with Image.open("piso1.jpg") as im:
    resized_im = im.resize((im_width, im_height))
    sprite.paste(resized_im, (x, y))
with Image.open("piso2.jpg") as im2:
    y = height // 2
    resized_im = im2.resize((im_width, im_height))
    sprite.paste(resized_im, (x, y))

sprite.save("./sprite4.jpg", "JPEG")

# 5. abrir n imagenes, achicarlas y ponerlas una debajo de la otra

floor_images = ["piso1.jpg", "piso2.jpg", "piso1.jpg", "piso2.jpg", "piso1.jpg"] * 5

n_img = len(floor_images)

im_width = 288
im_height = (im_width * 9) // 16

sprite_width = im_width
sprite_height = im_height * n_img

x = 0
y = 0

sprite = Image.new("RGB", (sprite_width, sprite_height))
for (index, image_route) in enumerate(floor_images):
    with Image.open(image_route) as im:
        y = im_height * index
        resized_im = im.resize((im_width, im_height))
        sprite.paste(resized_im, (x, y))

sprite.save(f"./sprite_{len(floor_images)}_pisos_{sprite_width}_width.jpg", "JPEG", quality=60, progressive=True)
