# catplot ki help s ap different catagorical plots bna skty hn, kind parameter m ap
# ko us plot ka name dena hota h jo ap n plot krna hota h, agar kind parameter nhi
# lgao gy to by default strip plot plot ho ga

import matplotlib.pyplot as plt
import seaborn as sns
df=sns.load_dataset("tips")

# sns.catplot(x="tip",y="size", data=df)  #stripplot
# sns.catplot(x="sex",y="size", data=df, height=0.5)  #stripplot
# plt.show()

# ---->  height=0.5 s graph ki height pr affect ho ga, graph bra ya chota show ho ga based
                # on the value of height

# sns.catplot(x="tip",data=df, kind="box", hue="sex")
# plt.show()

sns.catplot(x="sex", y="total_bill", data=df, hue="smoker", kind="bar", palette="plasma",
            width=0.5, ci=95, n_boot=200, capsize=0.3, errwidth=0.1, height=10)
plt.show()