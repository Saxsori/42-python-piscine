from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def main () :
	try:
		df = load("../csv/life_expectancy_years.csv")
		print(df.head())
		
		df = df.set_index("country").T
		print(df)
		
		# df["United Arab Emirates"] returns the column with the name "United Arab Emirates"
		df["United Arab Emirates"].plot()
		plt.xlabel("Year")
		plt.ylabel("Life Expectancy")
		plt.title("United Arab Emirates Life expectancy Projections")
		plt.show()
	except Exception as e:
		print("Error: ", e)
	
 
 
if __name__ == "__main__" :
	main()