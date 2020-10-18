import pandas as pd
import matplotlib.pyplot as plt

intvoto = [5,8,9,15,12,14,20,60,53,40,39,55]
mes = list(range(1,13))
data_dict = {'mes': mes, 'int': intvoto}

data = pd.DataFrame.from_dict(data_dict)
X = data['mes']
Y = data['int']

plt.scatter(X,Y)
plt.show()
