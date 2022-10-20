from Code.config import *
from statistics_reader import StatisticsReader

"""
The sd_inter_plots script, create the plots of the correlation between the 
SSC SD and IQR value, and the parameters (sensor data and sampling data.)
"""

# Calling the data from the class "StatisticsReader".
data_statistic = StatisticsReader()
df = data_statistic.data_statist

campaign_1 = ["KAA-HW1", "KAA-MW", "BR-HW", "BR-MW", "EM-HW", "EM-MW"]

color_1 = {"KAA-HW1": "firebrick",
           "KAA-MW": "orangered",
           "BR-HW": "green",
           "BR-MW": "yellowgreen",
           "EM-HW": "blue",
           "EM-MW": "steelblue"}

campaign_2 = ["KAA-HW1", "KAA-HW2", "KAA-MW", "KAA-LW", "BR-HW", "BR-MW",
              "BR-LW", "EM-HW", "EM-MW", "EM-LW"]

color_2 = {"KAA-HW1": "firebrick",
           "KAA-HW2": "red",
           "KAA-MW": "orangered",
           "KAA-LW": "lightcoral",
           "BR-HW": "green",
           "BR-MW": "yellowgreen",
           "BR-LW": "springgreen",
           "EM-HW": "blue",
           "EM-MW": "steelblue",
           "EM-LW": "aqua"}

# Environmental parameters correlations functions.

# SD ENV

fig, axis = plt.subplots(3, 3)

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 0].scatter(filtered_df["SSC(1s)-mg/l SD"],
                       filtered_df["Turbidity-FNU SD"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[0, 0].set_xlabel("SSC(1s) - mg/l")
    axis[0, 0].set_ylabel("Turbidity - FNU")
    axis[0, 0].set_title("Turbidity (FNU) SD")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 1].scatter(filtered_df["SSC(1s)-mg/l SD"],
                       filtered_df["ODO-mg/l SD"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[0, 1].set_xlabel("SSC(1s) - mg/l SD")
    axis[0, 1].set_ylabel("ODO - mg/l SD")
    axis[0, 1].set_title("ODO (mg/l) SD")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 2].scatter(filtered_df["SSC(1s)-mg/l SD"],
                       filtered_df["ORP-mV SD"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[0, 2].set_xlabel("SSC(1s) - mg/l SD")
    axis[0, 2].set_ylabel("ORP-mV SD")
    axis[0, 2].set_title("ORP mV SD")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 0].scatter(filtered_df["SSC(1s)-mg/l SD"],
                       filtered_df["Conductivity SD"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[1, 0].set_xlabel("SSC(1s) - mg/l SD")
    axis[1, 0].set_ylabel("Conductivity - mS/cm SD")
    axis[1, 0].set_title("Conductivity SD")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 1].scatter(filtered_df["SSC(1s)-mg/l SD"],
                       filtered_df["pH SD"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[1, 1].set_xlabel("SSC(1s) - mg/l SD")
    axis[1, 1].set_ylabel("pH SD")
    axis[1, 1].set_title("pH SD")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 2].scatter(filtered_df["SSC(1s)-mg/l SD"],
                       filtered_df["Grain size"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[1, 2].set_xlabel("SSC(1s) - mg/l SD")
    axis[1, 2].set_ylabel("Grain size SD")
    axis[1, 2].set_title("Grain Size SD")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[2, 0].scatter(filtered_df["SSC(1s)-mg/l SD"],
                       filtered_df["Q - m3/s"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[2, 0].set_xlabel("SSC(1s) - mg/l SD")
    axis[2, 0].set_ylabel("Q - m3/s SD")
    axis[2, 0].set_title("Discharge (m3/s) SD")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[2, 1].scatter(filtered_df["SSC(1s)-mg/l SD"],
                       filtered_df["V - m/s"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[2, 1].set_xlabel("SSC(1s) - mg/l SD")
    axis[2, 1].set_ylabel("V - m/s SD")
    axis[2, 1].set_title("Velocity (m/s) SD")

fig.legend(campaign_1, loc="center right")
plt.show()

# Interquartile ENV

fig, axis = plt.subplots(3, 3)

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 0].scatter(filtered_df["SSC(1s)-mg/l Inter"],
                       filtered_df["Turbidity-FNU Inter"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[0, 0].set_xlabel("SSC(1s) - mg/l IQR")
    axis[0, 0].set_ylabel("Turbidity - FNU IQR")
    axis[0, 0].set_title("Turbidity (FNU) IQR")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 1].scatter(filtered_df["SSC(1s)-mg/l Inter"],
                       filtered_df["ODO-mg/l Inter"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[0, 1].set_xlabel("SSC(1s) - mg/l IQR")
    axis[0, 1].set_ylabel("ODO - mg/l IQR")
    axis[0, 1].set_title("ODO (mg/l) IQR")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 2].scatter(filtered_df["SSC(1s)-mg/l Inter"],
                       filtered_df["ORP-mV Inter"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[0, 2].set_xlabel("SSC(1s) - mg/l IQR")
    axis[0, 2].set_ylabel("ORP-mV IQR")
    axis[0, 2].set_title("ORP (mV) IQR")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 0].scatter(filtered_df["SSC(1s)-mg/l Inter"],
                       filtered_df["Conductivity Inter"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[1, 0].set_xlabel("SSC(1s) - mg/l IQR")
    axis[1, 0].set_ylabel("Conductivity - mS/cm IQR")
    axis[1, 0].set_title("Conductivity IQR")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 1].scatter(filtered_df["SSC(1s)-mg/l Inter"],
                       filtered_df["pH Inter"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[1, 1].set_xlabel("SSC(1s) - mg/l IQR")
    axis[1, 1].set_ylabel("pH IQR")
    axis[1, 1].set_title("pH IQR")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 2].scatter(filtered_df["SSC(1s)-mg/l Inter"],
                       filtered_df["Grain size"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[1, 2].set_xlabel("SSC(1s) - mg/l IQR")
    axis[1, 2].set_ylabel("Grain size")
    axis[1, 2].set_title("Grain Size")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[2, 0].scatter(filtered_df["SSC(1s)-mg/l Inter"],
                       filtered_df["Q - m3/s"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[2, 0].set_xlabel("SSC(1s) - mg/l IQR")
    axis[2, 0].set_ylabel("Q - m3/s")
    axis[2, 0].set_title("Discharge (m3/s)")

for i in campaign_1:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[2, 1].scatter(filtered_df["SSC(1s)-mg/l Inter"],
                       filtered_df["V - m/s"],
                       c=filtered_df["Campaign"].map(color_1))
    axis[2, 1].set_xlabel("SSC(1s) - mg/l IQR")
    axis[2, 1].set_ylabel("V - m/s")
    axis[2, 1].set_title("Velocity (m/s)")

fig.legend(campaign_1, loc="center right")
plt.show()

# SD CHEMICALS

fig, axis = plt.subplots(4, 3)

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 0].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["Na-mg/l SD"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[0, 0].set_xlabel("SSC(15s) - mg/l SD")
    axis[0, 0].set_ylabel("Na-mg/l SD")
    axis[0, 0].set_title("Na-mg/l SD")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 1].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["Mg-mg/l SD"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[0, 1].set_xlabel("SSC(15s) - mg/l SD")
    axis[0, 1].set_ylabel("Mg-mg/l SD")
    axis[0, 1].set_title("Mg-mg/l SD")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 2].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["Al-mg/l SD"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[0, 2].set_xlabel("SSC(15s) - mg/l SD")
    axis[0, 2].set_ylabel("Al-mg/l SD")
    axis[0, 2].set_title("Al-mg/l SD")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 0].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["Si_2-mg/l SD"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[1, 0].set_xlabel("SSC(15s) - mg/l SD")
    axis[1, 0].set_ylabel("Si_2-mg/l SD")
    axis[1, 0].set_title("Si_2-mg/l SD")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 1].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["P-mg/l SD"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[1, 1].set_xlabel("SSC(15s) - mg/l SD")
    axis[1, 1].set_ylabel("P-mg/l SD")
    axis[1, 1].set_title("P-mg/l SD")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 2].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["S-mg/l SD"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[1, 2].set_xlabel("SSC(15s) - mg/l SD")
    axis[1, 2].set_ylabel("S-mg/l")
    axis[1, 2].set_title("S-mg/l SD")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[2, 0].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["K-mg/l SD"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[2, 0].set_xlabel("SSC(15s) - mg/l SD")
    axis[2, 0].set_ylabel("K-mg/l SD")
    axis[2, 0].set_title("K-mg/l SD")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[2, 1].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["Mn-mg/l SD"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[2, 1].set_xlabel("SSC(15s) - mg/l SD")
    axis[2, 1].set_ylabel("Mn-mg/l SD")
    axis[2, 1].set_title("Mn-mg/l SD")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[2, 2].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["Fe-mg/l SD"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[2, 2].set_xlabel("SSC(15s) - mg/l SD")
    axis[2, 2].set_ylabel("Fe-mg/l SD")
    axis[2, 2].set_title("Fe-mg/l SD")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[3, 0].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["Pb-mg/l SD"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[3, 0].set_xlabel("SSC(15s) - mg/l SD")
    axis[3, 0].set_ylabel("Pb-mg/l SD")
    axis[3, 0].set_title("Pb-mg/l SD")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[3, 1].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["Q - m3/s"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[3, 1].set_xlabel("SSC(15s) - mg/l SD")
    axis[3, 1].set_ylabel("Q - m3/s")
    axis[3, 1].set_title("Discharge (m3/s)")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[3, 2].scatter(filtered_df["SSC(15s)-mg/l SD"],
                       filtered_df["V - m/s"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[3, 2].set_xlabel("SSC(15s) - mg/l SD")
    axis[3, 2].set_ylabel("V - m/s")
    axis[3, 2].set_title("Velocity (m/s)")

fig.legend(campaign_2, loc="center right")
plt.show()

# INTER CHEMICALS
fig, axis = plt.subplots(4, 3)

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 0].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["Na-mg/l Inter"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[0, 0].set_xlabel("SSC(15s) - mg/l IQR")
    axis[0, 0].set_ylabel("Na-mg/l IQR")
    axis[0, 0].set_title("Na(mg/l) IQR")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 1].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["Mg-mg/l Inter"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[0, 1].set_xlabel("SSC(15s) - mg/l IQR")
    axis[0, 1].set_ylabel("Mg-mg/l IQR")
    axis[0, 1].set_title("Mg(mg/l) IQR")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[0, 2].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["Al-mg/l Inter"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[0, 2].set_xlabel("SSC(15s) - mg/l IQR")
    axis[0, 2].set_ylabel("Al-mg/l IQR")
    axis[0, 2].set_title("Al(mg/l) IQR")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 0].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["Si_2-mg/l Inter"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[1, 0].set_xlabel("SSC(15s) - mg/l IQR")
    axis[1, 0].set_ylabel("Si_2-mg/l IQR")
    axis[1, 0].set_title("Si_2(mg/l) IQR")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 1].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["P-mg/l Inter"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[1, 1].set_xlabel("SSC(15s) - mg/l IQR")
    axis[1, 1].set_ylabel("P-mg/l IQR")
    axis[1, 1].set_title("P(mg/l) IQR")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[1, 2].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["S-mg/l Inter"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[1, 2].set_xlabel("SSC(15s) - mg/l IQR")
    axis[1, 2].set_ylabel("S-mg/l IQR")
    axis[1, 2].set_title("S(mg/l) IQR")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[2, 0].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["K-mg/l Inter"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[2, 0].set_xlabel("SSC(15s) - mg/l IQR")
    axis[2, 0].set_ylabel("K-mg/l IQR")
    axis[2, 0].set_title("K(mg/l) IQR")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[2, 1].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["Mn-mg/l Inter"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[2, 1].set_xlabel("SSC(15s) - mg/l IQR")
    axis[2, 1].set_ylabel("Mn-mg/l IQR")
    axis[2, 1].set_title("Mn(mg/l) IQR")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[2, 2].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["Fe-mg/l Inter"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[2, 2].set_xlabel("SSC(15s) - mg/l IQR")
    axis[2, 2].set_ylabel("Fe-mg/l IQR")
    axis[2, 2].set_title("Fe(mg/l) IQR")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[3, 0].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["Pb-mg/l Inter"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[3, 0].set_xlabel("SSC(15s) - mg/l IQR")
    axis[3, 0].set_ylabel("Pb-mg/l IQR")
    axis[3, 0].set_title("Pb(mg/l) IQR")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[3, 1].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["Q - m3/s"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[3, 1].set_xlabel("SSC(15s) - mg/l IQR")
    axis[3, 1].set_ylabel("Q - m3/s")
    axis[3, 1].set_title("Discharge (m3/s)")

for i in campaign_2:
    filtered_df = df.loc[(df["Campaign"] == i)]
    axis[3, 2].scatter(filtered_df["SSC(15s)-mg/l Inter"],
                       filtered_df["V - m/s"],
                       c=filtered_df["Campaign"].map(color_2))
    axis[3, 2].set_xlabel("SSC(15s) - mg/l IQR")
    axis[3, 2].set_ylabel("V - m/s")
    axis[3, 2].set_title("Velocity (m/s)")

fig.legend(campaign_2, loc="center right")
plt.show()
