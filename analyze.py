import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

# print(type(data.head()))
a = "Mortality rate, infant (per 1,000 live births)"
b = "GDP per capita (constant 2010 US$)"
c = "Country Name"

print(data.loc[:, [a, b, c]])

data.plot(kind="scatter", x=b, y=a)

plt.show()
