import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r"C:\Users\subak\OneDrive - Saveeth School of Engineering\Documents\Qurey Processing\CSV files\fdata.csv", sep=',', parse_dates=True,index_col=0)
df.plot()
plt.show()
