# A violin plot plays a similar role as a box and wisker plot. It shows the distribution of 
# quantitative data across several levels of one (or more) catagorical variables such that
# those distributionds can be compared. 

#  You should use a violin plot when you want to visualize the distribution of numeric 
# data across different categories or groups.

# KDE boundary

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=sns.load_dataset("tips")
x=[1,2,3,4,5,6,7,8,9,10,11,12]

# sns.violinplot(x="sex",y="time", data=df, color="g",split=True)

# sns.violinplot(x="sex",y="tip",hue="day", data=df, palette="plasma", saturation=100,
#                linewidth=1, linecolor="r", hue_order=["Sun","Sat","Fri","Thur"],
#                 order=["Female","Male"] )
# plt.yticks(x)

# sns.violinplot(x="day",y="total_bill", data=df)  #ab is m thursday vala violin dekho, vo
        # hissa violin vala h yani jo hissa bht mota hua hua h us ka matlab y h k ziada
        # tar bill 10-20 (rupee may be the currency) k drmian tha, or bhtt kam bills 
        # thursday ko vo valy pay huy jin k 30 s 50 rupee th

# horizontal violine plot bnany k liye x-axis pr quantity and y-axis pr catogory rkh do:
# sns.violinplot(y="sex",x="total_bill", data=df, color="g", inner="quartile")

# --->inner="box" by default h , yani violin k ander box_plot show ho ga, you can
#               inner="Quartile" or "stick" or "point" 


# SINGLE VIOLINE PLOT (ONLY FOR QUANTITATIVE DATA)
sns.violinplot(x=df["total_bill"])

plt.grid()
plt.show()

# ------>  hue, palette(work only when hue is given), color, split, saturation, hue_order,
        # order, linewidth, linecolor, inner