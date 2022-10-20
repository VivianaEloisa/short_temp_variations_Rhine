from Code.config import *

from Code.chemicals_reader import ChemicalsReader
from Code.chemicals_reader import ChemLogReader
from env_reader import EnvReader
from env_reader import EnvLogReader

df1 = ChemicalsReader()
df_chem = df1.chemical_data

df2 = ChemLogReader()
df_log_chem = df2.chemical_log_data

df3 = EnvReader()
df_env = df3.data

df4 = EnvLogReader()
df_log_env = df4.log_data

"""
Chemical data correlation.
"""

filtered_df1 = df_chem.drop(
        columns=["Date", "Campaign"])
corr = filtered_df1.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, len(filtered_df1.columns), 1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(filtered_df1.columns)
ax.set_yticklabels(filtered_df1.columns)
plt.show()

"""
Chemical log data correlation.
"""

filtered_df1 = df_log_chem.drop(
        columns=["Date", "Campaign"])
corr = filtered_df1.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, len(filtered_df1.columns), 1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(filtered_df1.columns)
ax.set_yticklabels(filtered_df1.columns)
plt.show()


"""
Environmental data correlation.
"""

filtered_df1 = df_env.drop(
        columns=["Date", "Campaign"])
corr = filtered_df1.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, len(filtered_df1.columns), 1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(filtered_df1.columns)
ax.set_yticklabels(filtered_df1.columns)
plt.show()


"""
Environmental log data correlation.
"""

filtered_df1 = df_log_env.drop(
        columns=["Date", "Campaign"])
corr = filtered_df1.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, len(filtered_df1.columns), 1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(filtered_df1.columns)
ax.set_yticklabels(filtered_df1.columns)
plt.show()
