import matplotlib.pyplot as plt
import seaborn as sns
data_set=sns.load_dataset("penguins")
# sns.displot(data_set["species"] )
sns.displot(data_set["bill_length_mm"], bins=[0,30,40,50,60] , kde=True, rug=True,
            color="g")
# ---> kde=True (kernal density estimator) krny s ap ko uper ek line bhi show hoti h, bars 
        # k uper

# sns.displot(data_set["bill_length_mm"], kde=True, rug=True,
#             color="g", log_scale=True)  # log_scale=True krny s bill_length_mm ki values
            # ka log le ga and then x-axis pr plot kr k graph show kry ga

plt.show()
