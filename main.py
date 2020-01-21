import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

# %%
loc = "dataTable.csv"
data = pd.read_csv(loc)

# Filter acceptable entries
data = data.loc[(data["isHrValid"] == 1) & (data["isScValid"] == 1)]

data = data.loc[(data["Condition"] != "Pre") & (data["Condition"] != "Post")]
# data = data.loc[(data["Condition"] != "Low") & (data["Condition"] != "Post")]

X = data.iloc[:, 15:]
# y = (data["Condition"] == "Low").astype(int) + (data["Condition"] == "High").astype(int) * 2
y = (data["Condition"] == "High").astype(int)
hashes = pd.unique(data["hash"])

# %%
def cv_generator():
    for hash in hashes:
        cond = data["hash"] == hash
        yield np.where(~cond)[0], np.where(cond)[0]

parameters = {"kernel": ["linear", "rbf"],
              "gamma": [10 ** i for i in np.linspace(-1, 1, 3)],
              "C": [10 ** i for i in np.linspace(-1, 1, 3)]}

# parameters = {"kernel": ["linear", "rbf"],
#               "gamma": [10 ** i for i in np.linspace(-5, 5, 11)],
#               "C": [10 ** i for i in np.linspace(-5, 2, 8)]}

grid_search = GridSearchCV(SVC(), parameters, cv=cv_generator())

grid_search.fit(X, y)
