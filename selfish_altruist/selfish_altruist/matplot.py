import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


df = pd.read_csv('test1.csv')

df.plot.scatter(x = 'disease', y = '%Altruist')
df.plot('disease', '%Altruist')

plt.show()