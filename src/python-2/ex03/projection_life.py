from load_csv import load
import pandas as pd
import matplotlib as mpl
mpl.use("GTK3Agg") # or mpl.use("GTK3Cairo")
mpl.get_backend()
import matplotlib.pyplot as plt # --> this will throw the error 'Namespace Gtk not available'


def main () :
	try:
		ipp_df = load("../csv/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
		ley_df = load("../csv/life_expectancy_years.csv")

  
		# get Column year 1900 and country
		ley_df = ley_df.loc[:, ['country', '1900']]
		ipp_df = ipp_df.loc[:, ['country', '1900']]

  		
    	# merge the two dataframes
		new_df = pd.merge(ipp_df, ley_df, on="country")


		print(new_df)

		# 1900_x is the Gross domestic product, 1900_y is the life expectancy
		new_df.plot.scatter(x="1900_x", y="1900_y")

		# xscale('log') means that the x axis is in logarithmic scale, so the values are 300, 1000, 10000
		plt.xscale('log')
		# xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k']) 
  		# means that the x axis has the values 300, 1000, 10000 
    	# and the labels are 300, 1k, 10k		
		plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
		
		plt.xlabel("Gross domestic product")
		plt.ylabel("Life Expectancy")
		plt.title("1900")

		plt.show()
  
	except Exception as e:
		print("Error: ", e)



if __name__ == "__main__" :
	main()