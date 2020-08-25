import os, json, numpy
from PIL import Image
from tqdm import tqdm

file = open("information.txt", "w")

avgPixelValue = {}
for i in tqdm(range(0, len(os.listdir("grayscale_image")))):
    img = Image.open(f"grayscale_image/{i}.jpg")
    pixels = numpy.array(img)
    average_intensity = int(sum(list(map(sum, pixels))) // 10000)
    file.write(
        (str(i) + ".jpg").rjust(10) + "\t" + str(average_intensity).rjust(15) + "\n"
    )
    try:
        avgPixelValue[average_intensity].append(str(i) + ".jpg")
    except Exception as e:
        avgPixelValue[average_intensity] = [str(i) + ".jpg"]

file.close()

with open("information.json", "w") as json_file:
    json.dump(avgPixelValue, json_file)

