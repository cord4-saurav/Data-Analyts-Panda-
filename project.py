import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime

# covid_df = pd.read_csv("~/Downloads/cheat sheets/archive/covid_19_india.csv")
# covid_df.head(10)
# covid_df.info()

# covid_df.describe()
# covid_df['Date'] = pd.to_datetime(covid_df['Date'], format='%y-%m-%d')
# covid_df.head()

# top_10_active_cases = covid_df.groupby(by='State/UnionTerritory').max()[['Deaths', 'Date']]
# fig = plt.figure(figsize=(16, 9))
# plt.title('Top 10 states with most Deaths in india', size=25)
# ax = sns.barplot(data=top_10_active_cases.iloc[:10], y='Active_Cases', x='State/UnionTerritory', linewidth=2, edgecolor='red')
# plt.xlabel("States")
# plt.ylabel("Total Active Cases")
# plt.show()
#
# # from matplotlib import pyplot as plt
# # import numpy as np
#
# # Generate 100 random data points along 3 dimensions
# x, y, scale = np.random.randn(3, 100)
# fig, ax = plt.subplots()
#
# # Map each onto a scatterplot we'll create with Matplotlib
# ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)
# ax.set(title="Some random data, created with JupyterLab!")
# plt.show()


