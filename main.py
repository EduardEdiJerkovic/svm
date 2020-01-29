import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC

# %%
loc = "znacajke.csv"
# loc = "dataTable.csv"
data = pd.read_csv(loc)

# Filter acceptable entries
data = data.loc[(data["isHrValid"] == 1) & (data["isScValid"] == 1)]

# LOW vs HIGH
data = data.loc[(data["Condition"] != "Pre") & (data["Condition"] != "Post")]

# PRE vs LOW
# data = data.loc[(data["Condition"] != "High") & (data["Condition"] != "Post")]

# PRE vs HIGH
# data = data.loc[(data["Condition"] != "Low") & (data["Condition"] != "Post")]

X = data.iloc[:, 15:]

# PRE & POST vs LOW vs HIGH
# y = (data["Condition"] == "Low").astype(int) + (data["Condition"] == "High").astype(int) * 2

# LOW vs HIGH or PRE vs HIGH
y = (data["Condition"] == "High").astype(int)

# PRE vs LOW
# y = (data["Condition"] == "Low").astype(int)

hashes = pd.unique(data["hash"])

# %%
def cv_generator():
    for hash in hashes:
        cond = data["hash"] == hash
        yield np.where(~cond)[0], np.where(cond)[0]

parameters = {"svc__kernel": ["rbf"],
              "svc__gamma": [1000 ** i for i in np.linspace(-1, 1, 1000)],
              "svc__C": [1000 ** i for i in np.linspace(-1, 1, 1000)]}

# parameters = {"kernel": ["linear", "rbf"],
#               "gamma": [10 ** i for i in np.linspace(-5, 5, 11)],
#               "C": [10 ** i for i in np.linspace(-5, 2, 8)]}

grid_search = GridSearchCV(make_pipeline(StandardScaler(), SVC()), parameters, cv=cv_generator())

grid_search.fit(X, y)
