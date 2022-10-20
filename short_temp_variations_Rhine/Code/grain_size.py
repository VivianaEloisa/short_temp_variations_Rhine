from Code.config import *
from Code.chemicals_reader import ChemLogReader
from Code.env_reader import EnvLogReader

# Calling the class that imports the Chemical log-transformed data set.
data = ChemLogReader()
df = data.chemical_log_data
df = df.drop(labels=140, axis=0)
df = df.dropna()

# Calling the class that imports the Sensor log-transformed data set.
data = EnvLogReader()
df_e = data.log_data
df_e = df_e.drop(labels=140, axis=0)
df_e = df_e.dropna()

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

fig, axis = plt.subplots(3, 4)

# Plotting the correlations between grain size and the chemical data.

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[0, 0].scatter(df1["Grain Size"], df1["Na - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[0, 0].set_xlabel("Log Grain Size")
    axis[0, 0].set_ylabel("Log Na (mg/l)")
    axis[0, 0].set_title("Sodium")
    # plt.legend(campaign_1)
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[0, 1].scatter(df1["Grain Size"], df1["Mg - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[0, 1].set_xlabel("Log Grain Size")
    axis[0, 1].set_ylabel("Log Mg (mg/l)")
    axis[0, 1].set_title("Magnesium")
    # plt.legend(campaign_1)
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[0, 2].scatter(df1["Grain Size"], df1["Al - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[0, 2].set_xlabel("Log Grain Size")
    axis[0, 2].set_ylabel("Log Al (mg/l)")
    axis[0, 2].set_title("Aluminium")
    # plt.legend(campaign_1)
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[0, 3].scatter(df1["Grain Size"], df1["Si2 - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[0, 3].set_xlabel("Log Grain Size")
    axis[0, 3].set_ylabel("Log Si2 (mg/l)")
    axis[0, 3].set_title("Disiliane")
    # plt.legend(campaign_1)
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[1, 0].scatter(df1["Grain Size"], df1["P - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[1, 0].set_xlabel("Log Grain Size")
    axis[1, 0].set_ylabel("Log P (mg/l)")
    axis[1, 0].set_title("Phosphorus")
    # plt.legend(campaign_1)
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[1, 1].scatter(df1["Grain Size"], df1["S - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[1, 1].set_xlabel("Log Grain Size")
    axis[1, 1].set_ylabel("Log S (mg/l)")
    axis[1, 1].set_title("Sulfur")
    # plt.legend(campaign_1)
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[1, 2].scatter(df1["Grain Size"], df1["K - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[1, 2].set_xlabel("Log Grain Size")
    axis[1, 2].set_ylabel("Log K (mg/l)")
    axis[1, 2].set_title("Potassium")
    # plt.legend(campaign_1)
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[1, 3].scatter(df1["Grain Size"], df1["Mn - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[1, 3].set_xlabel("Log Grain Size")
    axis[1, 3].set_ylabel("Log Mn (mg/l)")
    axis[1, 3].set_title("Manganese")
    # plt.legend(campaign_1)
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[2, 0].scatter(df1["Grain Size"], df1["Fe - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[2, 0].set_xlabel("Log Grain Size")
    axis[2, 0].set_ylabel("Log Fe (mg/l)")
    axis[2, 0].set_title("Iron")
    # plt.legend(campaign_1)
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[2, 1].scatter(df1["Grain Size"], df1["Pb - mg/l"],
                       c=df1["Campaign"].map(color))
    axis[2, 1].set_xlabel("Log Grain Size")
    axis[2, 1].set_ylabel("Log Pb (mg/l)")
    axis[2, 1].set_title("Lead")
    # plt.legend(campaign_1)
# plt.show()

for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[2, 2].scatter(df1["Grain Size"], df1["Q - m3/s"],
                       c=df1["Campaign"].map(color))
    axis[2, 2].set_xlabel("Log SSC(15s) - mg/l")
    axis[2, 2].set_ylabel("Log Discharge (m3/s)")
    axis[2, 2].set_title("Discharge")
    # plt.legend(campaign_1)
# plt.show()


for i in campaign_1:
    df1 = df.loc[(df["Campaign"] == i)]
    axis[2, 3].scatter(df1["Grain Size"], df1["V - m/s"],
                       c=df1["Campaign"].map(color))
    axis[2, 3].set_xlabel("Log Grain Size")
    axis[2, 3].set_ylabel("Log Velocity (m/s)")
    axis[2, 3].set_title("Velocity")
    # plt.legend(campaign_1)
# plt.show()
fig.legend(campaign_1, loc="center right")
plt.show()

"""
Sampling campaigns.
"""

campaign_2 = ["KAA-HW", "KAA-MW", "BR-HW", "BR-MW", "EM-HW", "EM-MW"]

"""
Plot colors.
"""

color = {"KAA-HW": "firebrick",
         "KAA-MW": "orangered",
         "BR-HW": "green",
         "BR-MW": "yellowgreen",
         "EM-HW": "blue",
         "EM-MW": "steelblue"}

fig, axis = plt.subplots(3, 3)

for i in campaign_1:
    df1 = df_e.loc[(df["Campaign"] == i)]
    axis[0, 0].scatter(df1["Grain Size"], df_e["Conductivity"],
                       c=df1["Campaign"].map(color))
    axis[0, 0].set_xlabel("Log SSC (1s) - mg/l")
    axis[0, 0].set_ylabel("Log Conductivity")
    axis[0, 0].set_title("Conductivity")
    # plt.legend(campaign_1)
plt.show()

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

# Since all the plots are located in an axis all of them are plotted in the
# same figure with a single legend.

fig.legend(campaign_1, loc="center right")
plt.show()
