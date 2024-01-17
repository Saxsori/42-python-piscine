from load_image import ft_load
import matplotlib.pyplot as plt
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey



def main():
	image = ft_load("./img/landscape.jpg")
 
	# new_image = ft_invert(image)

	# new_image = ft_red(image)
 
	# new_image = ft_green(image)
 
	# new_image = ft_blue(image)
 
	new_image = ft_grey(image)
 
 
	plt.imshow(new_image)
	plt.show()

if __name__ == "__main__":
	main()