# countplot is used to show the count of observations in each categorical bin using bars.

# both countplot and histplot give count of values but histplot is suitable to get data distribution for 
# numerivcal data and use countplot for categorical data 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data=sns.load_dataset("tips")
print(data.head(10))
# sns.countplot(x="time", data=data, hue="sex",palette="plasma", saturation=100,
#               alpha=1 )
# sns.countplot(x="day", data=data, hue="time",palette="plasma", saturation=100,
#               alpha=1 )
sns.countplot(x="sex", data=data, hue="smoker",color="g", saturation=100,
              alpha=1 )
# sns.countplot(y="sex", data=data, hue="smoker",palette="plasma", saturation=100,
#               alpha=1 )   # HORIZONTAL COUNT PLOT
plt.show()