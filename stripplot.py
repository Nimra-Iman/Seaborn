# it is plotted between catagory and quantity. it is a good alternative for box plot and 
# violin plot. 

# jesy box plot m whisker plot bhi hota h, whiskerplot m data poory data ki distribution 
# zra hat kr hota h , to is stripplot m bhi jab dots door hony lagty hn ek doosry s kafi
# ziada to vo bhi ek whiskerplot hi show kr rha hota h
import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("tips")
sns.stripplot(x="day",y="tip", data=df, hue="sex", palette="plasma", 
              marker="<",
              linewidth=1, edgecolor="b", order=["Sun","Sat","Fri","Thur"],
              hue_order=["Female","Male"], size=5, alpha=0.9)
# ---> jitter=5 , jitter ki value brhany s poory graph k dosts phel jayn gy bilkul jesy 
#               y koi scatter plot ho, vesy jitter ko hta kr ziada acha observation hota h



# to get stripplot of single variable:
# sns.stripplot(x="total_bill", data=df)  #this will give horizontal
# sns.stripplot(y="total_bill", data=df)  #this will give vertical

plt.show()