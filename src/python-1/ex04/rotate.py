import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt

def main():
	image = ft_load("./img/animal.jpeg")
	print(image)

	image_array = image[100:100+400, 460:460+400, :1]

	transposed_image = image_array.transpose(1,0,2)
	print("New Shape after transpose : ", transposed_image.shape)
	print(transposed_image)

	plt.imshow(transposed_image, cmap='gray')
	plt.show()

if __name__ == "__main__":
	main()