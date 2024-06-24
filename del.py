import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("tips")

# sns.scatterplot(x="tip",y="total_bill", data=df, hue="sex", style="day")
# plt.show()

x=sns.FacetGrid(df, col="sex", hue="day", palette="cool", edgecolor="g")
x.map(plt.scatter, "tip","total_bill")
plt.show()

