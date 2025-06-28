# Factor Plot is used to draw a different types of categorical plot . The default plot
#  that is shown is a point plot, but we can plot other seaborn categorical plots by using 
# of kind parameter, like box plots, violin plots, bar plots, or strip plots.

import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("tips")
sns.factorplot(x="tip", kind="box", data=df)
plt.show()
# -->IT IS REMOVED FROM SEABORN LIBRARY AND IS REPLACED BY CATPLOT