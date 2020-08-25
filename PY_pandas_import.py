#import the pandas library and aliasing as pd
#import pandas as pd
#s = pd.Series()
#print (s)

# import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data = np.array(['okno','dveře','jáma','d'])
# s = pd.Series(data)
# print (s)

#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data = np.array(['a','b','c','d'])
# s = pd.Series(data,index=[100,101,102,103])
# print (s)

#import the pandas library and aliasing as pd
#import pandas as pd
#import numpy as np
#data = {'a' : 'okno', 'b' : 1., 'c' : 2.}
#s = pd.Series(data)
#print (s)

import csv
data = ["Month", "1958", "1959", "1960"]
x = [
["JAN", 340, 360, 417],
["FEB", 318, 342, 391],
["MAR", 362, 406, 419],
["APR", 348, 396, 461],
["MAY", 363, 420, 472],
["JUN", 435, 472, 535],
["JUL", 491, 548, 622],
["AUG", 505, 559, 606],
["SEP", 404, 463, 508],
["OCT", 359, 407, 461],
["NOV", 310, 362, 390],
["DEC", 337, 405, 432],
]
y = "/Users/td/Data/O2/test.csv"
with open(y, 'w') as work:
   z = csv.writer(work)
   z.writerow(data)
   z.writerows(x)