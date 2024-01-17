import pandas as pd

def load(path: str) -> pd.DataFrame:
	"""Load a csv file and return a pandas DataFrame"""
	try :
		df = pd.read_csv(path)
		print("The Shape of the DataFrame is : ", df.shape)
		return df.dropna()

	except :
		print("Error while loading the csv file")
		return pd.DataFrame()
