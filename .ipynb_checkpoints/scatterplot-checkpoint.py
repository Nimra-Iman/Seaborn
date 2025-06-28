import matplotlib.pyplot as plt
import seaborn as sns

data_set=sns.load_dataset("penguins")

m={"Male":"D", "Female":"o"}
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm", data=data_set, hue="island",
                style="sex", size="sex",sizes=(90,40), palette="plasma", alpha=1,
                  markers=m)

# markers=["D","^"]
# style="sex"  ---> yani sex k mutabik marker ka size different kr do, yani male ka alag and 
              # female ka alag
# size="sex"   --> yani sex k mutabik makrders k size bhi different kr do yani male and
                # female ki marker ka size different ho ga
# sizes=(90,40)  ---> size="sex" krny s us n apny mutabik size adjust kia, hm chahty hn
                    # k hmary mutabik size set ho, female k marker ka size 90 ho and
                    # male ka 40 ho, sizes will only work when size is given


# sns.scatterplot(x="bill_length_mm",y="bill_depth_mm", data=data_set, hue="island",
#                   palette="plasma", alpha=1,
#                   markers=["D","o","*"])  #yhan y work ni kry ga, marker=["D"] work kry ga
                    # sirf, agar ap chahty ho k teeno islands ka marker different show ho to
                    # is k liye style m "island" de do

plt.show()