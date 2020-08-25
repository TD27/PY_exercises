# I/O functions


# Import of CSV file, which is in the same directory

import pandas as pd
file = pd.read_csv("temp.csv")

print (file)



# Import of data from any directory

# path="/Users/td/Data/O2/O2_wttx_metrics.csv"
# data = pd.read_csv(path, sep=',', names=['@timestamp','Count'], header=0 )
# 
# 
# print("")
# print("----------------")
# print(data["@timestamp"])





