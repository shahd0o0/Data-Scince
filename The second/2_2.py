from copy import d

import pandas as pd
df = pd.DataFrame(data=d)
count_column =df.shape[1]
print("Number of columns:", count_column)

count_row =df.shape[0]
print("Number of rows:", count_row);