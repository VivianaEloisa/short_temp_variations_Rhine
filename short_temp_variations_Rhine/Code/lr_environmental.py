from Code.config import *

from Code.env_reader import EnvLogReader

data = EnvLogReader()
df = data.log_data
df = df.drop(labels=140, axis=0)
df = df.dropna()

"""
Creating the training data "X" ("SSC (1s) - mg/l") and the target values 
"y1,y2,y3...y4" ("Conductivity", "ODO - mg/l", "pH", "Turbidity - FNU")
"""

X = df.drop(columns=["Conductivity", "ODO - mg/l", "ORP mV", "Turbidity - FNU", "pH",
                     "V - m/s", "Campaign", "Q - m3/s", "Date"],
            axis=1).values

y1 = df["Conductivity"].values
y2 = df["ODO - mg/l"].values
y3 = df["Turbidity - FNU"].values
y4 = df["pH"].values
y5 = df["ORP mV"].values
y6 = df["Q - m3/s"].values
y7 = df["V - m/s"].values

"""
Linear Regression with discharge.
"""
lr = LinearRegression()

model_y1 = lr.fit(X, y1)
r2_y1 = model_y1.score(X, y1)
a_y1 = model_y1.coef_
b_y1 = model_y1.intercept_
r_y1, p_y1 = stats.pearsonr(df["SSC (1s) - mg/l"], df["Conductivity"])
sd_y1 = np.std(df["Conductivity"])

model_y2 = lr.fit(X, y2)
r2_y2 = model_y2.score(X, y2)
a_y2 = model_y2.coef_
b_y2 = model_y2.intercept_
r_y2, p_y2 = stats.pearsonr(df["SSC (1s) - mg/l"], df["ODO - mg/l"])
sd_y2 = np.std(df["ODO - mg/l"])

model_y3 = lr.fit(X, y3)
r2_y3 = model_y3.score(X, y3)
a_y3 = model_y3.coef_
b_y3 = model_y3.intercept_
r_y3, p_y3 = stats.pearsonr(df["SSC (1s) - mg/l"], df["Turbidity - FNU"])
sd_y3 = np.std(df["Turbidity - FNU"])

model_y4 = lr.fit(X, y4)
r2_y4 = model_y4.score(X, y4)
a_y4 = model_y4.coef_
b_y4 = model_y4.intercept_
r_y4, p_y4 = stats.pearsonr(df["SSC (1s) - mg/l"], df["pH"])
sd_y4 = np.std(df["pH"])

model_y5 = lr.fit(X, y5)
r2_y5 = model_y4.score(X, y5)
a_y5 = model_y5.coef_
b_y5 = model_y5.intercept_
r_y5, p_y5 = stats.pearsonr(df["SSC (1s) - mg/l"], df["ORP mV"])
sd_y5 = np.std(df["ORP mV"])

model_y6 = lr.fit(X, y6)
r2_y6 = model_y6.score(X, y6)
a_y6 = model_y6.coef_
b_y6 = model_y6.intercept_
r_y6, p_y6 = stats.pearsonr(df["SSC (1s) - mg/l"], df["Q - m3/s"])
sd_y6 = np.std(df["Q - m3/s"])

model_y7 = lr.fit(X, y7)
r2_y7 = model_y7.score(X, y7)
a_y7 = model_y7.coef_
b_y7 = model_y7.intercept_
r_y7, p_y7 = stats.pearsonr(df["SSC (1s) - mg/l"], df["V - m/s"])
sd_y7 = np.std(df["V - m/s"])

"""
Creating a dataframe with the outputs of the linear regression.
"""
data1 = {'Parameter': ["Conductivity", "ODO - mg/l", "Turbidity - FNU", "pH",
                      "ORP mV", "Q - m3/s", "V - m/s"]}
df1 = pd.DataFrame(data1)
data2 = {'R2': [r2_y1, r2_y2, r2_y3, r2_y4, r2_y5, r2_y6, r2_y7]}
df2 = pd.DataFrame(data2)
data3 = {'a': [a_y1, a_y2, a_y3, a_y4, a_y5, a_y6, a_y7]}
df3 = pd.DataFrame(data3)
data4 = {'b': [b_y1, b_y2, b_y3, b_y4, b_y5, b_y6, b_y7]}
df4 = pd.DataFrame(data4)
data5 = {'r': [r_y1, r_y2, r_y3, r_y4, r_y5, r_y6, r_y7]}
df5 = pd.DataFrame(data5)
data6 = {'p-value': [p_y1, p_y2, p_y3, p_y4, p_y5, p_y6, p_y7]}
df6 = pd.DataFrame(data6)
data7 = {'SD': [sd_y1, sd_y2, sd_y3, sd_y4, sd_y5, sd_y6, sd_y7]}
df7 = pd.DataFrame(data7)

df_regression_chem = pd.concat([df1, df2, df3, df4, df5, df6, df7], axis=1)
writer = pd.ExcelWriter(df_path + '/df_env_regression.xlsx')
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
n6 = X * a_y6 + b_y6
n7 = X * a_y7 + b_y7

"""
Sampling campaigns.
"""

campaign_1 = ["KAA-HW", "KAA-MW", "BR-HW", "BR-MW", "EM-HW", "EM-MW"]

"""
Plot colors.
"""

color = {"KAA-HW": "firebrick",
         "KAA-MW": "orangered",
         "BR-HW": "green",
         "BR-MW": "yellowgreen",
         "EM-HW": "blue",
         "EM-MW": "steelblue"}

# Plotting all the correlations on the same figure, at different axis.
# The correlation includes the curve that resulted from the linear regression.

fig, axis = plt.subplots(3, 3)

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[0, 0].scatter(df1["SSC (1s) - mg/l"], df1["Conductivity"],
                       c=df1["Campaign"].map(color))
    axis[0, 0].set_xlabel("Log SSC (1s) - mg/l")
    axis[0, 0].set_ylabel("Log Conductivity")
    axis[0, 0].set_title("Conductivity")
    # plt.legend(campaign_1)
axis[0, 0].plot(X, n1, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[0, 1].scatter(df1["SSC (1s) - mg/l"], df1["ODO - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[0, 1].set_xlabel("Log SSC (1s) - mg/l")
    axis[0, 1].set_ylabel("Log ODO (mg/l)")
    axis[0, 1].set_title("Dissolved Oxygen")
    # plt.legend(campaign_1)
axis[0, 1].plot(X, n2, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[0, 2].scatter(df1["SSC (1s) - mg/l"], df1["Turbidity - FNU"],
                       c=df1["Campaign"].map(color))
    axis[0, 2].set_xlabel("Log SSC (1s) - mg/l")
    axis[0, 2].set_ylabel("Log Turbidity (FNU)")
    axis[0, 2].set_title("Turbidity")
    # plt.legend(campaign_1)
axis[0, 2].plot(X, n3, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[1, 0].scatter(df1["SSC (1s) - mg/l"], df1["pH"],
                       c=df1["Campaign"].map(color))
    axis[1, 0].set_xlabel("Log SSC (1s) - mg/l")
    axis[1, 0].set_ylabel("Log pH")
    axis[1, 0].set_title("pH")
    # plt.legend(campaign_1)
axis[1, 0].plot(X, n4, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[1, 1].scatter(df1["SSC (1s) - mg/l"], df1["ORP mV"],
                       c=df1["Campaign"].map(color))
    axis[1, 1].set_xlabel("Log SSC (1s) - mg/l")
    axis[1, 1].set_ylabel("Log ORP mV")
    axis[1, 1].set_title("ORP")
    # plt.legend(campaign_1)
axis[1, 1].plot(X, n5, color="red")
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[1, 2].scatter(df1["SSC (1s) - mg/l"], df1["Q - m3/s"],
                       c=df1["Campaign"].map(color))
    axis[1, 2].set_xlabel("Log SSC (1s) - mg/l")
    axis[1, 2].set_ylabel("Log Discharge (m3/s)")
    axis[1, 2].set_title("Discharge")
    # plt.legend(campaign_1)
axis[1, 2].plot(X, n6, color="red")
# plt.show()


for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[2, 0].scatter(df1["SSC (1s) - mg/l"], df1["V - m/s"],
                       c=df1["Campaign"].map(color))
    axis[2, 0].set_xlabel("Log SSC (1s) - mg/l")
    axis[2, 0].set_ylabel("Log Velocity - m/s")
    axis[2, 0].set_title("Velocity")
    # plt.legend(campaign_1)
axis[2, 0].plot(X, n7, color="red")
# plt.show()

fig.legend(campaign_1, loc="center right")
plt.show()
