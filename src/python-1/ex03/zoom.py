import numpy as np
from PIL import Image
from load_image import ft_load
# import gi  # check if module isworking
# import gtk  # check if module is working
# import cairo  # check if module is working
import matplotlib as mpl
mpl.use("GTK3Agg") # or mpl.use("GTK3Cairo")
mpl.get_backend()
import matplotlib.pyplot as plt # --> this will throw the error 'Namespace Gtk not available'

def main():
	image = ft_load("./img/animal.jpeg")
	print(image)

	image_array = image[100:100+400, 460:460+400, :1]
	print("New Shape after slicing : ", image_array.shape)
	print(image_array)
	plt.imshow(image_array, cmap='gray')
	plt.show()

if __name__ == "__main__":
	main()