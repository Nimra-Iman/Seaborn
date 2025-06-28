# HOW TO STYLE YOUR PLOT?
import matplotlib.pyplot as plt
import seaborn as sns

# sns.set_style("dark")  #is s mujy bg dark show ho ga
# sns.set_style("darkgrid")  #is s mujy grid dark show ho ga
# sns.set_style("whitegrid")  #is s mujy grid white show ho ga


sns.set_theme("poster", font_scale=0.5,palette="cool")

# sns.set_context("poster", font_scale=0.5)
plt.figure(figsize=(3,12))   #is s ap apny graph ka size change kr skty ho, comma s phly
        # horizontal and then comma k baad vertical ka size show hota h

df=sns.load_dataset("tips")
sns.barplot(x=df["day"],y=df["total_bill"])
sns.despine()   # The sns.despine() function in Seaborn is used to remove the top and
        # right spines (axes) from a plot, making the plot look cleaner. However, it must be 
        # called after the plot has been created and before plt.show()
plt.show()