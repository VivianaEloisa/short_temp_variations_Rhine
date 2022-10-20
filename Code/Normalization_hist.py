from Code.config import *
from Code.chemicals_reader import ChemicalsReader
from Code.env_reader import EnvReader

"""

The "Normalization_hist.py" file, creates histograms that illustrate the 
distribution of the environmental and chemical parameters in two separated 
plots. 

In this case, due to the not normalized distribution of the data set, the data
was log-transformed. Finally, plotting the log-transformed data as histograms.

"""
data_chem = ChemicalsReader()
data_env = EnvReader()
df_chem = data_chem.chemical_data
df_env = data_env.data
df_chem = df_chem.dropna()
df_env = df_env.dropna()

"""
Plotting the histograms for the chemicals data set.  
"""


figure_chem, axis = plt.subplots(4, 3)

axis[0, 0].hist(df_chem["Na - mg/l"])
axis[0, 0].set_title("Na (mg/l)")

axis[0, 1].hist(df_chem["Mg - mg/l"])
axis[0, 1].set_title("Mg (mg/l)")

axis[0, 2].hist(df_chem["Al - mg/l"])
axis[0, 2].set_title("Al (mg/l)")

axis[1, 0].hist(df_chem["Si2 - mg/l"])
axis[1, 0].set_title("Si2 (mg/l)")

axis[1, 1].hist(df_chem["P - mg/l"])
axis[1, 1].set_title("P (mg/l)")

axis[1, 2].hist(df_chem["S - mg/l"])
axis[1, 2].set_title("S (mg/l)")

axis[2, 0].hist(df_chem["K - mg/l"])
axis[2, 0].set_title("K (mg/l)")

axis[2, 1].hist(df_chem["Mn - mg/l"])
axis[2, 1].set_title("Mn (mg/l)")

axis[2, 2].hist(df_chem["Fe - mg/l"])
axis[2, 2].set_title("Fe (mg/l)")

axis[3, 0].hist(df_chem["Pb - mg/l"])
axis[3, 0].set_title("Pb (mg/l)")

axis[3, 1].hist(df_chem["SSC(15s) - mg/l"])
axis[3, 1].set_title("SSC(15s) - mg/l")

axis[3, 2].hist(df_chem["Grain Size"])
axis[3, 2].set_title("Grain Size")


# plt.savefig(plots_path  + '/chem_hist', bbox_inches='tight')
plt.show()

"""
Plotting the histograms for the environmental data set.
"""

figure_env, axis = plt.subplots(4, 2)

axis[0, 0].hist(df_env["Conductivity"])
axis[0, 0].set_title("Conductivity")

axis[0, 1].hist(df_env["ODO - mg/l"])
axis[0, 1].set_title("Dissolved Oxygen (mg/l)")

axis[1, 0].hist(df_env["Turbidity - FNU"])
axis[1, 0].set_title("Turbidity - FNU")

axis[1, 1].hist(df_env["pH"])
axis[1, 1].set_title("pH")

axis[2, 0].hist(df_env["SSC (1s) - mg/l"])
axis[2, 0].set_title("SSC (1s) - mg/l")

axis[2, 1].hist(df_env["Q - m3/s"])
axis[2, 1].set_title("Q - m3/s")

axis[3, 0].hist(df_env["V - m/s"])
axis[3, 0].set_title("V - m/s")

axis[3, 1].hist(df_env["ORP mV"])
axis[3, 1].set_title("ORP mV")

# plt.savefig(plots_path  + '/env_hist', bbox_inches='tight')
plt.show()

"""
Normalizing through a Scikit learn in built function. However, there are not 
important changes in data distribution.
"""

# norm_data = preprocessing.normalize(df, axis=0)
# norm_df = pd.DataFrame(norm_data, columns=[df.columns])
# print(norm_df)

"""
Normalizing through log-transform base10. Achieving a better distribution of 
the data set. Thus, using this transformed data in the linear regression. 

"""

"""
Log-transformed chemical data.
"""

df_chem1 = df_chem.drop(columns=["Campaign", "Date"])
log_df_chem = pd.DataFrame(np.log10(df_chem1), columns=df_chem1.columns)
log_df_chem = pd.concat([log_df_chem, df_chem["Campaign"], df_chem["Date"]],
                        axis=1)
# log_df_chem.to_csv("df_chem_log_10.csv")
# writer = pd.ExcelWriter(df_path + '/df_chem_log_10.xlsx')
# log_df_chem.to_excel(writer)
# writer.save()
# print(log_df_chem)

"""
Log-transformed environmental data.
"""

df_env1 = df_env.drop(columns=["Campaign", "Date"])
log_df_env = pd.DataFrame(np.log10(df_env1), columns=df_env1.columns)
log_df_env = pd.concat([log_df_env, df_env["Campaign"], df_env["Date"]],
                       axis=1)
log_df_env.to_csv("df_env_log_10.csv")
writer = pd.ExcelWriter(df_path + '/df_env_log_10.xlsx')
log_df_env.to_excel(writer)
writer.save()
print(log_df_env)

"""
Histograms of the log-transformed data.
"""

"""
Chemical data.
"""
figure_chem_log, axis = plt.subplots(4, 3)

axis[0, 0].hist(log_df_chem["Na - mg/l"])
axis[0, 0].set_title("Log Na (mg/l)")

axis[0, 1].hist(log_df_chem["Mg - mg/l"])
axis[0, 1].set_title("Log Mg (mg/l)")

axis[0, 2].hist(log_df_chem["Al - mg/l"])
axis[0, 2].set_title("Log Al (mg/l)")

axis[1, 0].hist(log_df_chem["Si2 - mg/l"])
axis[1, 0].set_title("Log Si2 (mg/l)")

axis[1, 1].hist(log_df_chem["P - mg/l"])
axis[1, 1].set_title("Log P(mg/l)")

axis[1, 2].hist(log_df_chem["S - mg/l"])
axis[1, 2].set_title("Log S (mg/l)")

axis[2, 0].hist(log_df_chem["K - mg/l"])
axis[2, 0].set_title("Log K (mg/l)")

axis[2, 1].hist(log_df_chem["Mn - mg/l"])
axis[2, 1].set_title("Log Mn (mg/l)")

axis[2, 2].hist(log_df_chem["Fe - mg/l"])
axis[2, 2].set_title("Log Fe(mg/l)")

axis[3, 0].hist(log_df_chem["Pb - mg/l"])
axis[3, 0].set_title("Log Pb(mg/l)")

axis[3, 1].hist(log_df_chem["SSC(15s) - mg/l"])
axis[3, 1].set_title("Log SSC(15s) mg/l")

axis[3, 2].hist(log_df_chem["Grain Size"])
axis[3, 2].set_title("Log Grain Size")

# plt.savefig(plots_path  + '/chem_log_hist', bbox_inches='tight')
# plt.show()

"""
Environmental data. 
"""

figure_env_log, axis = plt.subplots(4, 2)

axis[0, 0].hist(log_df_env["Conductivity"])
axis[0, 0].set_title("Log Conductivity")

axis[0, 1].hist(log_df_env["ODO - mg/l"])
axis[0, 1].set_title("Log ODO (mg/l)")

axis[1, 0].hist(log_df_env["Turbidity - FNU"])
axis[1, 0].set_title("Log Turbidity (FNU)")

axis[1, 1].hist(log_df_env["pH"])
axis[1, 1].set_title("Log pH")

axis[2, 0].hist(log_df_env["SSC (1s) - mg/l"])
axis[2, 0].set_title("Log SSC (1s) mg/l")

axis[2, 1].hist(log_df_env["Q - m3/s"])
axis[2, 1].set_title("Log Discharge(m3/s)")

axis[3, 0].hist(log_df_env["V - m/s"])
axis[3, 0].set_title("Log Velocity (m/s)")

axis[3, 1].hist(log_df_env["ORP mV"])
axis[3, 1].set_title("Log ORP mV")


# plt.savefig(plots_path  + '/env_log_hist', bbox_inches='tight')
plt.show()
