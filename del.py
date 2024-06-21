import matplotlib.pyplot as plt
import seaborn as sns
data_set=sns.load_dataset("penguins")
# sns.displot(data_set["species"] )
sns.displot(data_set["bill_length_mm"], kde=True, rug=True,
            color="g")
plt.show()