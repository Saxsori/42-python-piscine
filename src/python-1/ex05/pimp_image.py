import numpy as np

def ft_invert(array: np.ndarray) -> np.ndarray:
	"""Invert the color of an image
	invert means to make the white color black and the black color white
	subtract the value of each pixel to 255 to invert the color
	because the maximum value of a pixel is 255 and the minimum is 0
 	"""
	return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """make the image red
    by setting the green and blue channels to 0
    and keeping the red channel untouched
    Channel means the color of the pixel, each pixel has 3 channels, red, green, blue
    0 channel is the first channel which is the red channel
	1 channel is the second channel which is the green channel
	2 channel is the third channel which is the blue channel
    """
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    return array



def ft_green(array: np.ndarray) -> np.ndarray:
    """make the image green
	by setting the red and blue channels to 0
	and keeping the green channel untouched
    Channel means the color of the pixel, each pixel has 3 channels, red, green, blue
	0 channel is the first channel which is the red channel
	1 channel is the second channel which is the green channel
	2 channel is the third channel which is the blue channel
	"""
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    return array


def ft_blue(array: np.ndarray) -> np.ndarray:
	"""make the image blue
	by setting the red and green channels to 0
	and keeping the blue channel untouched
	Channel means the color of the pixel, each pixel has 3 channels, red, green, blue
	0 channel is the first channel which is the red channel
	1 channel is the second channel which is the green channel
	2 channel is the third channel which is the blue channel
	"""
	array[:, :, 0] = 0
	array[:, :, 1] = 0
	return array


def ft_grey(array) -> np.ndarray:
	"""make the image grey
	by setting the red and green and blue channels to the average of the three channels
	Channel means the color of the pixel, each pixel has 3 channels, red, green, blue
	0 channel is the first channel which is the red channel
	1 channel is the second channel which is the green channel
	2 channel is the third channel which is the blue channel
	(array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3)
	is the average of the three channels of the image, we set the three channels to the average
	which makes the image grey, the average of the three channels is the grey color
	
	"""
	gray_scale = (array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3)
	array[:, :, 0] = gray_scale
	array[:, :, 1] = gray_scale
	array[:, :, 2] = gray_scale

	return array

