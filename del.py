import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=sns.load_dataset("tips").head(100)

sns.violinplot(x="sex", y="total_bill",data=df,hue="day", 
               order=["Female","Male"], palette="plasma" , inner="box" )
plt.show()




