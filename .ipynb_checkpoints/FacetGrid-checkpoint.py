# agar hm chahty hn k ek hi dataset ko use krty huy hm 2 graphs bnay e.g male and female
# ka alag alag graph ho, to hm FacetGrid ko use kryn gy

import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("tips")
x = sns.FacetGrid(df, col="sex", hue="day", palette="cool")  #col="sex" krny s male and female ka graph alag
# alag show ho ga
x.map(plt.scatter, "total_bill","tip", edgecolor="g").add_legend()   #.add_legend() krna zruri h vrna legend 
                            # show nhi ho ga 
plt.show()


