import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray:
	"""Load an image and return a numpy array"""
	try :
		img = Image.open(path)
		print("The Shape of the image is : ", np.array(img).shape)
		return np.array(img)

	except :
		return []