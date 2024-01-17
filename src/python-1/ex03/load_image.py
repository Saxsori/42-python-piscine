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


# ValueError: 'gtk3airo' is not a valid value for backend; supported values are ['GTK3Agg', 'GTK3Cairo', 'GTK4Agg', 'GTK4Cairo', 'MacOSX', 'nbAgg', 'QtAgg', 'QtCairo', 'Qt5Agg', 'Qt5Cairo', 'TkAgg', 'TkCairo', 'WebAgg', 'WX', 'WXAgg', 'WXCairo', 'agg', 'cairo', 'pdf', 'pgf', 'ps', 'svg', 'template']