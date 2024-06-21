import matplotlib.pyplot as plt
import seaborn as sns
data_set=sns.load_dataset("penguins")
sns.set_theme(style="darkgrid")
# sns.barplot(x=data_set.island, y=data_set.bill_length_mm) # -- OR --
# sns.barplot(x="island", y="bill_length_mm", data=data_set , hue="sex",
#             order=["Dream", "Biscoe", "Torgersen"], hue_order=["Female","Male"],
#             errorbar=('ci', 95), n_boot=500, palette='icefire', saturation=0.6,
#             errcolor="y", errwidth=12, capsize=0.5)

# ---->  hue="sex"  yani hr island k male and female ka alag alag dikhao
# ---->  order=["Dream", "Biscoe", "Torgersen"]  s graph k bars isi order m show hn
            # gy jo order dia h
# ---->  hue_order=["Female","Male"]  , hm chahty hn k males ki bijay graph m females phly
            # show hn, to hm order dety huy hue ko saath rkhy gy q k hue ki vja s hi to "sex"
            # show hua h
# ---->  ci=__ , ci range from 0 to 100 and it stands for confidence interval, BUT: :::
            # FutureWarning: The `ci` parameter is deprecated. Use `errorbar=('ci', 0)`
            #  for the same effect.
# ---->  n_boot=__ , controls how many times the data is re-sampled to estimate the
            #  confidence intervals. Ap n y check krna h k ap k sample ki avaerage kia h?
            # to ap baar baar sample lety ho ta k confirm ho sky k accurate rsukt yani accurately
            # bta sko k average itni h, n_boot=500 s muraad y h k ap n 500 dfa samples liye
            # or baar baar mean lia, More repetitions (n_boot value) generally give a more 
            # accurate estimate of how much the average can vary. 
# ---->  color="g" but y future m khatam hony vala h feature, so it is better to use: 
            # palette="dark:g", y palette vhi h jo cmap m names hn
# ---->  saturation=0.6 
# ---->  errcolor="y" to change the color of ci line.
# ---->  errwidth=12 to increase the width of ci line, FutureWarning:The `errwidth` 
            # parameter is deprecated. And will be removed in v0.15.0. Pass
            #  `err_kws={'linewidth': 12}` instead.
# ---->  dodge=False krny s male and female k graph ek doosry k uper show hony lgy gy

# ---->  orient="h" , yani graph ko horrizontally show krvana h, but horizontally show 
            # krvany k liye dono parameters intger hona zruri h, catagorical variables
            # allowed nhi hn
# ---->  capsize=0.5

# sns.barplot(x="bill_length_mm", y="bill_length_mm", data=data_set ,
#             orient="h" )

sns.barplot(x="sex", y="bill_length_mm", data=data_set ,
             capsize=0.5, dodge=False, saturation=100, alpha=0.5)


plt.show()