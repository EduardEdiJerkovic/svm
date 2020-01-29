from scipy.io import loadmat
import matplotlib.pyplot as plt

mat = loadmat("sc_batch_data_cvxEDA/sc_0efd4.mat")

# %%
plt.figure()
plt.plot(mat["data"])
plt.plot(mat["p"])
plt.plot(mat["r"])
plt.plot(mat["t"])
plt.grid()
plt.legend(["data", "p", "r", "t"])
plt.show()

# %%
