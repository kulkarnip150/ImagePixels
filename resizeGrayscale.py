from PIL import Image
import os

if not os.path.exists("grayscale_image"):
    print("making grayscale_image folder")
    os.makedirs("grayscale_image")
for i in range(0, len(os.listdir("raw_image"))):
    # print(f"raw_image/{i}.jpg")
    img = Image.open(f"raw_image/{i}.jpg").convert("L")
    resized_im = img.resize((100, 100))
    # resized_im.show()
    resized_im.save(f"grayscale_image/{i}.jpg")
    print(f"{i} done")
