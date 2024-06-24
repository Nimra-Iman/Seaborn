# it is used in machiene learning algorithms. 

# It combines both histogram and scatter plots, providing a unique overview of the dataset's distributions and correlations.

# A pair plot, also known as a scatterplot matrix, is a matrix of graphs that enables the visualization of the relationship between each pair of variables in a dataset.
 
# Seaborn's pairplot is primarily designed for visualizing relationships between pairs of quantitative (numerical) variables in a dataset. 

import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("tips")



# sns.pairplot(df)  #pairplot just quatitative data ka show hota h but hm is ko mazeed
                    # catogorical m bhi show krva skty hn but using "hue"


sns.pairplot(df, hue="sex", hue_order=["Female","Male"], palette="plasma",
              markers=["*","D"]) #phly male uper tha label m or us ka color blue tha , ab female ka color blue ho ga via hue order q k hm n basically order change kr dia.

# pairplot saaarrroo ka sow hota h, ham chahty hn k kuch quatitaive variables ka show ho to is k liye hm "vars = " ka use krty hn
# sns.pairplot(df, vars=["total_bill","tip"])

#, x_vars=["total_bill","tip"]: agar ap chaty hn k x-axis pr kon kon c parameters how hon to esy likhna h but khial rhy k y tab hi use ho ga jab vars= nhi dia ho ga , and same for y-axis k liye de skty : y_vars=["total_bill","tip"]

# sns.pairplot(df, x_vars=["total_bill","tip"], kind="reg")  #ab x_axis pr sirf y hon gy and y-axis pr sab hon gy
# kind="kde" or "reg" or "hist" or "scatter", ,,,,,, diag_kind parameter also used
plt.show()




