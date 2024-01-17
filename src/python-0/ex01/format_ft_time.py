from datetime import date

import time

today = date.today()

time_now = time.time()


formatted_date1 = today.strftime("%B %d, %Y")

formatted_date2 = today.strftime("%b %d %Y")


formatted_time1 = "{:,.4f}".format(time_now)

formatted_time2 = "{:.2e}".format(time_now)



print("Seconds since January 1, 1970: " + formatted_time1 + " or " + formatted_time2 + " in scientific notation")
print(formatted_date2)

# print ("Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation")
# print("Oct 21 2022")