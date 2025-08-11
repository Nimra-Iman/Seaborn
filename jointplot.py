import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = sns.load_dataset('tips')
print(data.head())

sns.jointplot(x = data['total_bill'], y = data['size'], kind = 'hex')
plt.show()