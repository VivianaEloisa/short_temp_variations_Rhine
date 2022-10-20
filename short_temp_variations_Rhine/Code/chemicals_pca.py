from config import *
from chemicals_reader import ChemicalsReader

"""
This script is for executing the Principal Component Analysis (PCA), based on 
the original data.

"""
# Calling the information from the class "ChemLogReader" that has the log trans
# formed data of the chemical elements.

data_alles = ChemicalsReader()
df = data_alles.chemical_data
df = df.dropna()

# X are the variables for which the principal components are found. In this
# case the X corresponds to all the chemical elements:Na, Mg, Al, Si2, P, S, K,
# Mn, Fe and Pb.

X = df.drop(columns=["Date", "Campaign", "Q - m3/s", "V - m/s",
                     "SSC(15s) - mg/l", "Grain Size"],
            axis=1).values
# y are the parameters that are correlated to the principal components found.
# In this case are the sampling campaigns.

y = df["Campaign"].values

# Scaler is scaling the data frame, thus the differences in the units will not
# affect the results.

scaler = StandardScaler()

# Settling the number of principal components.
pca = decomposition.PCA(n_components=6)

# The scores localize the parameters on a plane in correlation with the PC.
# This section of the code create a table with the scores value and save it
# automatically in the settled path in the "config" script.

scores = pca.fit_transform(scaler.fit_transform(X))
scores_df = pd.DataFrame(scores, columns=["PC1", "PC2", "PC3", "PC4", "PC5",
                                          "PC6"])
scores_df = pd.concat([scores_df, df["Campaign"], df["Date"]], axis=1)
scores_df = scores_df.dropna()
writer = pd.ExcelWriter(df_path + '/scores_chem_pca.xlsx')
scores_df.to_excel(writer)
writer.save()

# The loading's describe the correlation between the PC and the parameters.

# This section of the code create a table with the loading's value and save it
# automatically in the settled path in the "config" script.

loadings = pca.components_.T
df_loadings = pd.DataFrame(loadings, columns=["PC1", "PC2", "PC3", "PC4",
                                              "PC5", "PC6"],
                           index=["Na - mg/l",
                                  "Mg - mg/l",
                                  "Al - mg/l",
                                  "Si2 - mg/l",
                                  "P - mg/l",
                                  "S - mg/l",
                                  "K - mg/l",
                                  "Mn - mg/l",
                                  "Fe - mg/l",
                                  "Pb - mg/l"])

writer = pd.ExcelWriter(df_path + '/loadings_chemicals_pca.xlsx')
df_loadings.to_excel(writer)
writer.save()

# The explained variance is the cumulative sum of the PC.
explained_variance = pca.explained_variance_ratio_

explained_variance = np.insert(explained_variance, 0, 0)
cumulative_variance = np.cumsum(np.round(explained_variance, decimals=3))

# This section of the code create a table with the cumulative values and save
# it automatically in the settled path in the "config" script.
pc_df = pd.DataFrame(["", "PC1", "PC2", "PC3", "PC4", "PC5", "PC6"],
                     columns=["PC"])
explained_variance_df = pd.DataFrame(explained_variance, columns=["Explained"
                                                                  "Variance"])
cumulative_variance_df = pd.DataFrame(cumulative_variance, columns=["Cumulati"
                                                                    "ve Varian"
                                                                    "ce"])
df_explained_variance = pd.concat([pc_df, explained_variance_df,
                                   cumulative_variance_df], axis=1)

writer = pd.ExcelWriter(df_path + '/expla-var_chemicals_pca.xlsx')
df_explained_variance.to_excel(writer)
writer.save()
print(df_explained_variance)

# This section of the code creates a plot with the cumulative explained
# variance.

fig = px.bar(df_explained_variance, x="PC", y="ExplainedVariance",
             text="ExplainedVariance", width=800)
fig.update_traces(texttemplate="%{text:.3f}", textposition="outside")
fig.show()

fig = go.Figure()
fig.add_trace(
    go.Scatter(x=df_explained_variance["PC"],
               y=df_explained_variance["Cumulative Variance"],
               marker=dict(size=15, color="LightSeaGreen")))
fig.add_trace(
    go.Bar(x=df_explained_variance["PC"],
           y=df_explained_variance["ExplainedVariance"],
           marker=dict(color="RoyalBlue")))
fig.show()

# Plot with the localization of the parameters regarding the PC on a plane.
# For creating this plot is used the scores df.
fig = px.scatter_3d(scores_df, x="PC1", y="PC2", z="PC3", color="Campaign")
fig.show()

fig = px.scatter_3d(df_loadings, x="PC1", y="PC2", z="PC3",
                    text=df_loadings.index)
fig.show()

fig = px.scatter_3d(df_loadings, x="PC4", y="PC5", z="PC6",
                    text=df_loadings.index)
fig.show()

labels = {
    str(i): f"PC {i+1} ({var:.1f}%)"
    for i, var in enumerate(explained_variance*100)
}

# Plot with the localization of the campaigns regarding the PC on a plane.
# For creating this plot is used the loadings df.

fig = px.scatter_matrix(
    scores,
    labels=labels,
    dimensions=range(6),
    color=df["Campaign"]
)
fig.update_traces(diagonal_visible=False)
fig.show()