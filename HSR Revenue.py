#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read Data
data = pd.read_csv("HSR.csv")

#Insert Headers for Data
df = data
Headers = ["Month", "Revenue"]
df.columns = Headers

#Change the types
df["Revenue"] = df["Revenue"].astype('int')
df["Month"] = pd.to_datetime(df["Month"])

#Plot Line Graph
plt.figure(figsize=(10,5))
plt.plot(df["Month"],df["Revenue"])
plt.xlabel("Time")
plt.ylabel("Revenue in Millions")
plt.xticks(ticks=df["Month"], labels=df["Month"].dt.strftime('%Y-%m'), rotation=45)


#Annotate Firefly's Release 
FF = "Firefly Release"
ff_release = '2024-06-19'
ff_release = pd.to_datetime(ff_release)



#Annotate Acheron's release 
acheron = "Acheron Release"
ac_release = '2024-03-27'
ac_release = pd.to_datetime(ac_release)



#Calculate and Show the trend line
x_values = np.arange(len(df))
coefficients = np.polyfit(x_values, df["Revenue"],1)
trend_line = np.polyval(coefficients, x_values)
plt.plot(df["Month"], trend_line, color ='orange', label = 'Trend', linewidth=2,linestyle = '--')

release_dates = {FF: ff_release,acheron: ac_release}

for title, date in release_dates.items():
    release_date = pd.to_datetime(date)
    
    # Calculate the y-value for the release date using interpolation
    if release_date in df['Month'].values:
        y_value = df.loc[df['Month'] == release_date, 'Revenue'].values[0]
    else:
        # Interpolating the value based on the closest dates
        y_value = np.interp(release_date.toordinal(), df['Month'].map(pd.Timestamp.toordinal), df['Revenue'])
    
    # Plot a point at the intersection on the line graph
    plt.plot(release_date, y_value, marker='o', markersize=8, label=title)

# Formatting the plot
plt.title('Honkai Star Rail IAP')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()

# Show the plot
plt.show()


#Show Monthly Growth
df['Monthly Growth'] = df['Revenue'].diff()
df['Monthly Growth'] = df['Monthly Growth'].fillna(0)

print(df)
# %%
