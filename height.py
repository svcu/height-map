from skimage import io
from skimage.color import rgb2gray

url = input("Introduzca una URL: ")
image=io.imread(url)
output=rgb2gray(image)
io.imsave("height.png", output)
print("Finished")