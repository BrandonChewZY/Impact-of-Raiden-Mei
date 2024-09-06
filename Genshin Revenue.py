#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read Data
df = pd.read_csv("Genshin.csv")

#Insert Headers
headers = ['Month','Revenue']
df.columns = headers
df["Revenue"] = df["Revenue"].astype("int")
df["Month"] = pd.to_datetime(df["Month"])

#Filter for Month
df_filtered = df[df["Month"].dt.year <= 2022]

#Plot Line Graph
plt.figure(figsize=(10,5))
plt.plot(df_filtered["Month"], df_filtered["Revenue"])


#Create Trend Line
x_values=np.arange(len(df_filtered))
coefficients = np.polyfit(x_values, df_filtered["Revenue"],1)
Trend_line = np.polyval(coefficients, x_values)
plt.plot(df_filtered["Month"],Trend_line, label = "Trend", linewidth = 2, linestyle = '--')

#Annotate Raiden Shogun's Release
Raiden = "Raiden Shogun Release"
RaidenDate = '2021-09-01'
RaidenDate = pd.to_datetime(RaidenDate)

#Annotate Shenhe's Release
Shenhe = "Shenhe Release Date"
ShenheDate = '2022-01-05'
ShenheDate = pd.to_datetime(ShenheDate)

release_dates = {Shenhe:ShenheDate, Raiden:RaidenDate}

for char, date in release_dates.items():
    if date in df_filtered['Month']:
        y_value = df_filtered.loc[df_filtered['Month'] == date, "Revenue"].values[0]
    else:
        y_value = np.interp(date.toordinal(), df['Month'].map(pd.Timestamp.toordinal), df['Revenue'])
    
    plt.plot(date, y_value, marker = 'o', markersize = 8, label = char)

#Formatting the graph
plt.xlabel("Time")
plt.ylabel("Revenue in Millions")
plt.title("Genshin Impact IAP")
plt.xticks( rotation=45)
plt.legend()
plt.grid()

#Show Monthly growth
df_filtered['Monthly Growth'] = df_filtered['Revenue'].diff()
df_filtered['Monthly Growth'] = df_filtered['Monthly Growth'].fillna(0)

print(df_filtered)
# %%
