# visualize data density and patterns espacially on large data set: e.g: 

# heatmap is mostly used in machine learning where a larger amount of data is given, 
#  us data ko heatmap k zrye groups m divide krna asan ho jata h

# heatmap m hm data ko different color s show krty hn,
# heatmap only work in 2D data, it does not work in 1D data
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

data=np.linspace(1,10,20).reshape(4,5)
x=sns.heatmap(data=data, annot=True, xticklabels=False, yticklabels=False, cbar=False, cmap="plasma", 
            linecolor="green", linewidths=2, annot_kws={"fontsize":18, "color":"r"})
x.set(xlabel="python", ylabel="seaborn")
sns.set(font_scale=6)
plt.show()

# --->  annot_kws={"fontzise":18, "color":"r"} is s annot valy text ka color or fontsize change ho ga

# ----> annot=True krny s ap k "data" valy digits bhi show hon gy, but ap chahty hn k ap k data valy digits
#                   show na ho bal k hm khud kuch pass kry or color_boxes k uper vo chees show ho, to is k liye hm  esy kry gy:
#                   x=np.array([["a1","a2","a3","a4","a5",],
#                               ["b1","b2","b3","b4","b5",],
#                               ["c1","c2","c3","c4","c5",],
#                               ["d1","d2","d3","d4","d5",]])
#                   sns.heatmap(data=data, annot=x, fmt="s") #fmt="s" is liye likha q k annot k ander jo array dali h us k format
#                                                               # string vala h
#                   plt.show()




# dat=sns.load_dataset("anagrams").head(10)
#  #ab is data k ander string vala data bhi h yani textual data bhi h, and sirf 
# # numerical data ka hi heatmap bna skty hn , is liye hm text valy data ko drop kry gy

# new_dat=dat.drop(columns="attnr", axis=1)
# # print(new_dat)

# plt.subplot(1,2,1)
# sns.heatmap(data=new_dat, vmin=0, vmax=20, annot=True)  #vmin, vmax s color m kaafi difference ay ga
# # plt.show()


# plt.subplot(1,2,2)
# sns.heatmap(data=new_dat, annot=True)

plt.show()
