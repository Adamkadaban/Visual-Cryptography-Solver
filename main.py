from PIL import Image
import sys


def help():
	print(f"Visual Cryptography Solver for PNGs")
	print(f"Usage:\n\tpython3 {args[0]} <image 1> <image 2>\n\nExample:\n\tpython3 {args[0]} 'image1.png image2.png'\n")
	print(f"\nOptional arguments:\n\t-h: Show this help screen\n")

args = sys.argv

if len(args)!=3:
	help()
	exit()

if "-h" in args:
	help()
	exit()

image1 = Image.open(args[1])
image2 = Image.open(args[2])


image1Pixels = image1.load()
image2Pixels = image2.load()

newImage = Image.new(mode = "RGB", size = image1.size)

for i in range(image1.size[0]):
  for j in range(image1.size[1]):
    p1 = image1Pixels[i,j]
    p2 = image2Pixels[i,j]


    r = (p1[0] + p2[0]) % 256
    g = (p1[1] + p2[1]) % 256
    b = (p1[2] + p2[2]) % 256

    # print(r,g,b)
    newImage.putpixel((i,j), (r,g,b))


		

newImage.save("newImage.png")
print("Done!")
