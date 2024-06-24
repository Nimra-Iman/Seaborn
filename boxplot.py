import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("tips")

sns.boxplot(x="day" , y="total_bill", hue="smoker",data=df, palette="plasma",
            order=["Sun","Sat","Fri","Thur"], hue_order=["No","Yes"], width=0.2,
            showmeans=True,
             meanprops={"markerfacecolor":"r", "marker":"*", "markeredgecolor":"g"},
             linewidth=2, linecolor="g")
# plt.show()


# ---->  showmeans=True krny s ap ko mean show ho ga poory data ka including data in
#    whisker plot and the outliers jab k straight line in box-plot shows the median of all
#    the data including data in whisker plot and the outliers.

# ---->   orient="h" krny k liye dono axis pr data numeric ho, but horizontal esy bhi
        # kr skty hn k x_axis m catagory ki jga quantity daal do and y-axis m catagory daal 
        # do:
sns.boxplot(data=df, orient="h")
# plt.show()


# single boxplot:
sns.boxplot(y="tip", data=df)   #vertical boxplot
sns.boxplot(x="tip", data=df)   #horizontal boxplot
plt.show()