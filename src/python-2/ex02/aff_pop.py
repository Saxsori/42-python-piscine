from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def main () :
	try:
		df = load("../csv/population_total.csv")
		print(df.head())
		
		df = df.set_index("country").T
		print(df)
		
		# get Two columns , United Arab Emirates and France
		ae_fr_df = df[["United Arab Emirates", "France"]]
		
  		# rows from 1800 to 2050
		ae_fr_df = ae_fr_df.loc["1800":"2050"]
		ae_fr_df = ae_fr_df.replace({'[kK]': '*1e3', '[mM]': '*1e6', '[bB]': '*1e9', },regex=True).map(pd.eval)
		print(ae_fr_df)

		ae_fr_df.plot()
		plt.xlabel("Year")
		plt.ylabel("Population")
		plt.title("Population Projections")
		plt.show()

	except Exception as e:
		print("Error: ", e)
	
 
 
if __name__ == "__main__" :
	main()