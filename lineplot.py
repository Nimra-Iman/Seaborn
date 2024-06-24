# show trends over time, e.g display the growth of website traffic over a year.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

var=  [1,2,3,4,5,6,7]
var_1=[2,3,4,1,5,6,7]

# x=pd.DataFrame({"var":var, "var_1":var_1})
# sns.lineplot(x="var", y="var_1", data=x)  # The line plot will have points 
            # plotted at coordinates:
            # (1, 2)
            # (2, 3)
            # (3, 4)
            # (4, 1)
            # (5, 5)
            # (6, 6)
            # (7, 7)



# x = pd.DataFrame({"var":[12,56,32], "var_1":[78,92,12]})
# sns.lineplot(x="var",y="var_1", data=x)  # var and var_1 are lists that are not used 
                                # in the plot. These lists might be misleading.


# x=pd.DataFrame({"var":var, "var_1":var_1})
# print(x)
# sns.lineplot( data=x)


# --------------   IT IS DIFFICULT TO UNDERSTAND SEABORN LINEPLOT FROM ABOVE GRAPHS,
#  SO IT IS GOOD TO LOAD SOME ORIGINAL DATA-SET AND PLOT GRAPH


x=sns.load_dataset("iris")
# x=sns.load_dataset("iris").head(20) krny s jo dataset yhan load ho ga vo just phly 20
# rows ka ho ga

# sns.lineplot(x="sepal_length", y="sepal_width", data=x)  #yani "iris" k datset m hmy y
# btao k jab sepal_length itni ho gi to sepal_width kitni ho gi




sns.lineplot(x="sepal_length", y="sepal_width", data=x, hue="species", style="species",
             palette="Accent", markers=["o","D",">"], dashes=False, legend=False) 
 # ----> hue= yani "species" column m jitni bhi species hn un sab k according alag alag btao k 
 # jab sepal_length itni thi to sepal_width kitni ho gi

#  ----> style="species", yani ab total three species given hn iris data set m to hr specie 
# k according jo graph ki line show ho gi us ka line style different ho ga

# markers=["o","D",">"], y hm style k mutabik de rhy hn, yani style m species pas h or total
# 3 species hn to markers m bhi 3 parameters pas hon gy, agar hm 2 parameters pass krty hn to
#  teesri specie ka marker phly vali ki marker jesa ho ga

#  ---->  palette="Greens"  , palettes m vhi saary colormap ki list valy names ay gy jo hm
# n matplotlib k scatter plot m prhy th

# ---->  dashes=False krny s style k zrye jo dotted lines ai thi, vo khatam ho kr vapis 
# solid lines a jay gi

# ----> legend=False krny s label hat jay ga

# it uses the markers parameter to determine the marker style for each level of the hue 
# variable, but only when the style parameter is used in conjunction with hue.

# sns.lineplot(x="bill_length_mm", y="flipper_length_mm", data=x, hue="species",
#              palette="plasma", marker="o")  #is case m marker kaam kry ga but 
                # ap chahty ho k hue m jo species pas hn, un species ka hr ek ka marker
                # different ho to vo nhi chaly ga jab tak ap n style nhi dala hua

plt.grid()
plt.title("this is an iris dataset")
plt.show()