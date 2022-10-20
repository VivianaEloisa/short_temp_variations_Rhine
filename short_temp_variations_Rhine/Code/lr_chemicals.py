from Code.config import *
from Code.chemicals_reader import ChemLogReader

data = ChemLogReader()
df = data.chemical_log_data
df = df.drop(labels=140, axis=0)
df = df.dropna()

""" 
Creating the training data "X" ("SSC(15s) - mg/l") and the target 
values "y1,y2,y3...y12" ("Na - mg/l",  "Mg - mg/l","Al - mg/l", "Si2 - mg/l", 
"P - mg/l", "S - mg/l", "K - mg/l", "Mn - mg/l", "Fe - mg/l", "Pb - mg/l",
"Grain Size")

"""

X = df.drop(columns=["Na - mg/l",
                     "Mg - mg/l",
                     "Al - mg/l",
                     "Si2 - mg/l",
                     "P - mg/l",
                     "S - mg/l",
                     "K - mg/l",
                     "Mn - mg/l",
                     "Fe - mg/l",
                     "Pb - mg/l",
                     "Q - m3/s",
                     "V - m/s",
                     "Grain Size",
                     "Campaign",
                     "Date"], axis=1).values
y1 = df["Na - mg/l"].values
y2 = df["Mg - mg/l"].values
y3 = df["Al - mg/l"].values
y4 = df["Si2 - mg/l"].values
y5 = df["P - mg/l"].values
y6 = df["S - mg/l"].values
y7 = df["K - mg/l"].values
y8 = df["Mn - mg/l"].values
y9 = df["Fe - mg/l"].values
y10 = df["Pb - mg/l"].values
y11 = df["Grain Size"].values
y12 = df["Q - m3/s"].values
y13 = df["V - m/s"].values
"""
Linear Regression with discharge.
"""
lr = LinearRegression()

model_y1 = lr.fit(X, y1)
r2_y1 = model_y1.score(X, y1)
a_y1 = model_y1.coef_
b_y1 = model_y1.intercept_
r_y1, p_y1 = stats.pearsonr(df["SSC(15s) - mg/l"], df["Na - mg/l"])
sd_y1 = np.std(df["Na - mg/l"])

model_y2 = lr.fit(X, y2)
r2_y2 = model_y2.score(X, y2)
a_y2 = model_y2.coef_
b_y2 = model_y2.intercept_
r_y2, p_y2 = stats.pearsonr(df["SSC(15s) - mg/l"], df["Mg - mg/l"])
sd_y2 = np.std(df["Mg - mg/l"])

model_y3 = lr.fit(X, y3)
r2_y3 = model_y3.score(X, y3)
a_y3 = model_y3.coef_
b_y3 = model_y3.intercept_
r_y3, p_y3 = stats.pearsonr(df["SSC(15s) - mg/l"], df["Al - mg/l"])
sd_y3 = np.std(df["Al - mg/l"])

model_y4 = lr.fit(X, y4)
r2_y4 = model_y4.score(X, y4)
a_y4 = model_y4.coef_
b_y4 = model_y4.intercept_
r_y4, p_y4 = stats.pearsonr(df["SSC(15s) - mg/l"], df["Si2 - mg/l"])
sd_y4 = np.std(df["Si2 - mg/l"])

model_y5 = lr.fit(X, y5)
r2_y5 = model_y5.score(X, y5)
a_y5 = model_y5.coef_
b_y5 = model_y5.intercept_
r_y5, p_y5 = stats.pearsonr(df["SSC(15s) - mg/l"], df["P - mg/l"])
sd_y5 = np.std(df["P - mg/l"])

model_y6 = lr.fit(X, y6)
r2_y6 = model_y1.score(X, y6)
a_y6 = model_y6.coef_
b_y6 = model_y6.intercept_
r_y6, p_y6 = stats.pearsonr(df["SSC(15s) - mg/l"], df["S - mg/l"])
sd_y6 = np.std(df["S - mg/l"])

model_y7 = lr.fit(X, y7)
r2_y7 = model_y7.score(X, y7)
a_y7 = model_y7.coef_
b_y7 = model_y7.intercept_
r_y7, p_y7 = stats.pearsonr(df["SSC(15s) - mg/l"], df["K - mg/l"])
sd_y7 = np.std(df["K - mg/l"])

model_y8 = lr.fit(X, y8)
r2_y8 = model_y8.score(X, y8)
a_y8 = model_y8.coef_
b_y8 = model_y8.intercept_
r_y8, p_y8 = stats.pearsonr(df["SSC(15s) - mg/l"], df["Mn - mg/l"])
sd_y8 = np.std(df["Mn - mg/l"])

model_y9 = lr.fit(X, y9)
r2_y9 = model_y9.score(X, y9)
a_y9 = model_y9.coef_
b_y9 = model_y9.intercept_
r_y9, p_y9 = stats.pearsonr(df["SSC(15s) - mg/l"], df["Fe - mg/l"])
sd_y9 = np.std(df["Fe - mg/l"])

model_y10 = lr.fit(X, y10)
r2_y10 = model_y10.score(X, y10)
a_y10 = model_y10.coef_
b_y10 = model_y10.intercept_
r_y10, p_y10 = stats.pearsonr(df["SSC(15s) - mg/l"], df["Pb - mg/l"])
sd_y10 = np.std(df["Pb - mg/l"])

model_y11 = lr.fit(X, y11)
r2_y11 = model_y11.score(X, y11)
a_y11 = model_y11.coef_
b_y11 = model_y11.intercept_
r_y11, p_y11 = stats.pearsonr(df["SSC(15s) - mg/l"], df["Grain Size"])
sd_y11 = np.std(df["Grain Size"])

model_y12 = lr.fit(X, y12)
r2_y12 = model_y11.score(X, y12)
a_y12 = model_y11.coef_
b_y12 = model_y11.intercept_
r_y12, p_y12 = stats.pearsonr(df["SSC(15s) - mg/l"], df["Q - m3/s"])
sd_y12 = np.std(df["Grain Size"])

model_y13 = lr.fit(X, y13)
r2_y13 = model_y13.score(X, y13)
a_y13 = model_y13.coef_
b_y13 = model_y13.intercept_
r_y13, p_y13 = stats.pearsonr(df["SSC(15s) - mg/l"], df["V - m/s"])
sd_y13 = np.std(df["Grain Size"])

"""
Creating a dataframe with the outputs of the linear regression.
"""
data1 = {'Parameter': ["Na - mg/l",
                       "Mg - mg/l",
                       "Al - mg/l",
                       "Si2 - mg/l",
                       "P - mg/l",
                       "S - mg/l",
                       "K - mg/l",
                       "Mn - mg/l",
                       "Fe - mg/l",
                       "Pb - mg/l",
                       "Q - m3/s",
                       "V - m/s",
                       "Grain Size"
                       ]}
df1 = pd.DataFrame(data1)
data2 = {'R2': [r2_y1, r2_y2, r2_y3, r2_y4, r2_y5, r2_y6, r2_y7, r2_y8,
                r2_y9, r2_y10, r2_y11, r2_y12, r2_y13 ]}
df2 = pd.DataFrame(data2)
data3 = {'a': [a_y1, a_y2, a_y3, a_y4, a_y5, a_y6, a_y7, a_y8, a_y9, a_y10,
               a_y11, a_y12, a_y13]}
df3 = pd.DataFrame(data3)
data4 = {'b': [b_y1, b_y2, b_y3, b_y4, b_y5, b_y6, b_y7, b_y8, b_y9, b_y10,
               b_y11, b_y12, b_y13]}
df4 = pd.DataFrame(data4)
data5 = {'r': [r_y1, r_y2, r_y3, r_y4, r_y5, r_y6, r_y7, r_y8, r_y9, r_y10,
               r_y11, r_y12, r_y13]}
df5 = pd.DataFrame(data5)
data6 = {'p-value': [p_y1, p_y2, p_y3, p_y4, p_y5, p_y6, p_y7, p_y8, p_y9,
                     p_y10, p_y11, p_y12, p_y13]}
df6 = pd.DataFrame(data6)
data7 = {'SD': [sd_y1, sd_y2, sd_y3, sd_y4, sd_y5, sd_y6, sd_y7, sd_y8, sd_y9,
                sd_y10, sd_y11, sd_y12, sd_y13]}
df7 = pd.DataFrame(data7)

df_regression_chem = pd.concat([df1, df2, df3, df4, df5, df6, df7], axis=1)
writer = pd.ExcelWriter(df_path + '/df_chem_regression.xlsx')
df_regression_chem.to_excel(writer)
writer.save()
print(df_regression_chem)

"""
Linear Regression Equation.

"""
n1 = X * a_y1 + b_y1
n2 = X * a_y2 + b_y2
n3 = X * a_y3 + b_y3
n4 = X * a_y4 + b_y4
n5 = X * a_y5 + b_y5
n6 = X * a_y6 + b_y1
n7 = X * a_y7 + b_y2
n8 = X * a_y8 + b_y3
n9 = X * a_y9 + b_y4
n10 = X * a_y10 + b_y10
n11 = X * a_y11 + b_y11
n12 = X * a_y12 + b_y12
n13 = X * a_y13 + b_y13
"""
Sampling campaigns.
"""

campaign_1 = ["KAA-HW1", "KAA-HW2", "KAA-MW", "KAA-LW", "BR-HW", "BR-MW",
              "BR-LW", "EM-HW", "EM-MW", "EM-LW"]

"""
Plot colors.
"""

color = {"KAA-HW1": "firebrick",
         "KAA-HW2": "red",
         "KAA-MW": "orangered",
         "KAA-LW": "lightcoral",
         "BR-HW": "green",
         "BR-MW": "yellowgreen",
         "BR-LW": "springgreen",
         "EM-HW": "blue",
         "EM-MW": "steelblue",
         "EM-LW": "aqua"}

# Plotting all the correlations on the same figure, at different axis.
# The correlation includes the curve that resulted from the linear regression.

fig, axis = plt.subplots(4, 4)

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[0, 0].scatter(df1["SSC(15s) - mg/l"], df1["Na - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[0, 0].set_xlabel("Log SSC(15s) - mg/l")
    axis[0, 0].set_ylabel("Log Na (mg/l)")
    axis[0, 0].set_title("Sodium")
    # plt.legend(campaign_1)
axis[0, 0].plot(X, n1, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[0, 1].scatter(df1["SSC(15s) - mg/l"], df1["Mg - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[0, 1].set_xlabel("Log SSC(15s) - mg/l")
    axis[0, 1].set_ylabel("Log Mg (mg/l)")
    axis[0, 1].set_title("Magnesium")
    # plt.legend(campaign_1)
axis[0, 1].plot(X, n2, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[0, 2].scatter(df1["SSC(15s) - mg/l"], df1["Al - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[0, 2].set_xlabel("Log SSC(15s) - mg/l")
    axis[0, 2].set_ylabel("Log Al (mg/l)")
    axis[0, 2].set_title("Aluminium")
    # plt.legend(campaign_1)
axis[0, 2].plot(X, n3, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[0, 3].scatter(df1["SSC(15s) - mg/l"], df1["Si2 - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[0, 3].set_xlabel("Log SSC(15s) - mg/l")
    axis[0, 3].set_ylabel("Log Si2 (mg/l)")
    axis[0, 3].set_title("Disiliane")
    # plt.legend(campaign_1)
axis[0, 3].plot(X, n4, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[1, 0].scatter(df1["SSC(15s) - mg/l"], df1["P - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[1, 0].set_xlabel("Log SSC(15s) - mg/l")
    axis[1, 0].set_ylabel("Log P (mg/l)")
    axis[1, 0].set_title("Phosphorus")
    # plt.legend(campaign_1)
axis[1, 0].plot(X, n5, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[1, 1].scatter(df1["SSC(15s) - mg/l"], df1["S - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[1, 1].set_xlabel("Log SSC(15s) - mg/l")
    axis[1, 1].set_ylabel("Log S (mg/l)")
    axis[1, 1].set_title("Sulfur")
    # plt.legend(campaign_1)
axis[1, 1].plot(X, n6, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[1, 2].scatter(df1["SSC(15s) - mg/l"], df1["K - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[1, 2].set_xlabel("Log SSC(15s) - mg/l")
    axis[1, 2].set_ylabel("Log K (mg/l)")
    axis[1, 2].set_title("Potassium")
    # plt.legend(campaign_1)
axis[1, 2].plot(X, n7, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[1, 3].scatter(df1["SSC(15s) - mg/l"], df1["Mn - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[1, 3].set_xlabel("Log SSC(15s) - mg/l")
    axis[1, 3].set_ylabel("Log Mn (mg/l)")
    axis[1, 3].set_title("Manganese")
    # plt.legend(campaign_1)
axis[1, 3].plot(X, n8, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[2, 0].scatter(df1["SSC(15s) - mg/l"], df1["Fe - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[2, 0].set_xlabel("Log SSC(15s) - mg/l")
    axis[2, 0].set_ylabel("Log Fe (mg/l)")
    axis[2, 0].set_title("Iron")
    # plt.legend(campaign_1)
axis[2, 0].plot(X, n9, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[2, 1].scatter(df1["SSC(15s) - mg/l"], df1["Pb - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[2, 1].set_xlabel("Log SSC(15s) - mg/l")
    axis[2, 1].set_ylabel("Log Pb (mg/l)")
    axis[2, 1].set_title("Lead")
    # plt.legend(campaign_1)
axis[2, 1].plot(X, n10, color="red")
# plt.show()


for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[2, 2].scatter(df1["SSC(15s) - mg/l"], df1["Grain Size"],
                       c=df1["Campaign"].map(color))
    axis[2, 2].set_xlabel("Log SSC(15s) - mg/l")
    axis[2, 2].set_ylabel("Log Grain Size")
    axis[2, 2].set_title("Grain Size")
    # plt.legend(campaign_1)
axis[2, 2].plot(X, n11, color="red")
# plt.show()


for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[2, 3].scatter(df1["SSC(15s) - mg/l"], df1["Q - m3/s"],
                       c=df1["Campaign"].map(color))
    axis[2, 3].set_xlabel("Log SSC(15s) - mg/l")
    axis[2, 3].set_ylabel("Log Discharge (m3/s)")
    axis[2, 3].set_title("Discharge")
    # plt.legend(campaign_1)
axis[2, 3].plot(X, n12, color="red")
# plt.show()


for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[3, 0].scatter(df1["SSC(15s) - mg/l"], df1["V - m/s"],
                       c=df1["Campaign"].map(color))
    axis[3, 0].set_xlabel("Log SSC(15s) - mg/l")
    axis[3, 0].set_ylabel("Log Velocity (m/s)")
    axis[3, 0].set_title("Velocity")
    # plt.legend(campaign_1)
axis[3, 0].plot(X, n13, color="red")
# plt.show()
fig.legend(campaign_1, loc="center right")
plt.show()
