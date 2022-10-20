from Code.config import *
from Code.chemicals_reader import ChemPCReader
from Code.chemicals_reader import ChemicalsReader
from Code.chemicals_reader import SSCReader

"""
The multiple_lr script is used to develop a MLR using the 6 PC obtained from 
the PCA as the explanatory variables, thus testing if the controlling factors
and its association to the sampled data, can predict the SSC. 
"""


data_pc = ChemPCReader()
df1 = data_pc.chemical_pca_data

data_ssc = ChemicalsReader()
df_ssc = data_ssc.chemical_data
df2 = df_ssc.dropna()

data_ssc1 = SSCReader()
df_ssc1 = data_ssc1.ssc_data
df3 = df_ssc1.dropna()

"""
Creating the training data "X" (PC1, PC2, PC3, PC4, PC5, PC6) and the target 
values "y" ("SSC(15s) - mg/l",)

"""

X = df1.drop(columns=["Campaign", "Date"], axis=1).values

y = df2["SSC(15s) - mg/l"].values

"""
Multiple Linear Regression with discharge.
"""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=0)
lr = LinearRegression()

lr.fit(X_train, y_train)
ytest = pd.DataFrame(y_test)
writer = pd.ExcelWriter(df_path + '/ssc_test.xlsx')
ytest.to_excel(writer)
writer.save()

# Multiple linear regression coefficient and intercept.

(a1, a2, a3, a4, a5, a6) = lr.coef_
b = lr.intercept_

# print(a1, a2, a3, a4, a5, a6)
# print(b)

# Training the algorithm for the prediction.
y_pred_train = lr.predict(X_train)

# print(y_pred)

# Plotting the training values.
plt.scatter(x=y_train, y=y_pred_train)
plt.legend(["Predicted"], loc="lower right")
# plt.show()

# Calculating the coefficient of determination for the prediction using the
# training values.
r_train = r2_score(y_train, y_pred_train)

# print(r_train)

# Introducing the values for testing the algorithm.
y_pred_test = lr.predict(X_test)
# ypred = pd.DataFrame(y_pred_test)
# writer = pd.ExcelWriter(df_path + '/ssc_test.xlsx')
# ytest.to_excel(writer)
# writer.save()

# Plotting the predicted values using the test.

campaign_1 = ["KAA-HW1", "KAA-HW2", "KAA-MW", "KAA-LW", "BR-HW", "BR-MW",
              "BR-LW", "EM-HW", "EM-MW", "EM-LW"]

color = {"KAA-HW1": "firebrick",
         "KAA-HW2": "red",
         "KAA-MW": "orangered",
         "KAA-LW": "lightcoral",
         "BR-HW": "green",
         "BR-MW": "yellowgreen",
         "BR-LW": "springgreen",
         "EM-HW": "deepskyblue",
         "EM-MW": "cyan",
         "EM-LW": "skyblue"}

for i in campaign_1:
    df1 = df3.loc[(df3["Campaign"] == i)]
    plt.scatter(df1["test"], df1["pred"],
                c=df1["Campaign"].map(color))
    plt.xlabel("SSC-mg/l (Sampled)")
    plt.ylabel("SSC-mg/l (Predicted)")
    plt.legend(campaign_1, loc="lower center")
plt.show()

# plt.scatter(y_test, y_pred_test, marker = "o")
# plt.scatter(y_test, y_pred_test, marker = "^")
# plt.xlabel("Time - Minutes")
# plt.ylabel("SSC-mg/l")
# plt.legend(["Predicted", "Measured"], loc="lower right")
# plt.show()

# Calculating the coefficient of determination for the predicted values.
r_test = r2_score(y_test, y_pred_test)
# print(y_pred_test)

x = pd.DataFrame(y_test, columns=["SSC"])
y = pd.DataFrame(y_pred_test, columns=["SSC Predicted"])
z = pd.concat([x, y], axis=1)
# writer = pd.ExcelWriter(df_path + '/multiple_lr.xlsx')
# z.to_excel(writer)
# writer.save()
# print(z)


# plt.scatter(y_test, y_pred_test, marker= "o")
# plt.scatter(y_test, y_pred_test, marker= "*")
# plt.xlabel("Time - Minutes")
# plt.ylabel("SSC-mg/l")
# plt.legend(campaign_1)
# plt.plot(n, y_test, color="red")
# plt.show()
#
# print(r_test)
