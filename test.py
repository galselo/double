import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
from random import random as rand

now = datetime.datetime.now()

w = 1e0

xdata_old = [now]
ydata_old = [0.5]
doubling_time = 7
plet = 2.36e-2 * doubling_time / 30.
ptin = 1e-1 * doubling_time / 30.
print(1e0 / plet, plet)

fig = plt.figure()

nlet = 0
ntot = 0

for i in range(10):
    dy = w / (2**i + 1)
    ydata = np.array([dy * (j + 1) for j in range(2**i)])
    xdata = np.array([now + datetime.timedelta(days=i * doubling_time) for _ in ydata])
    ldata = np.array([rand() < plet for _ in xdata])
    tdata = np.array([rand() < ptin for _ in xdata])

    plt.scatter(xdata, ydata, color="tab:blue", s=2)
    plt.scatter(xdata[ldata], ydata[ldata], color="tab:red", s=30, zorder=999)
    # plt.scatter(xdata[tdata], ydata[tdata], color="tab:green", s=30, zorder=998)

    nlet += np.sum(ldata)
    ntot += len(ldata)
    
    for j in range(2**i):
        plt.plot([xdata[j], xdata_old[j // 2]], [ydata[j], ydata_old[j // 2]], color="tab:blue", lw=.5, alpha=.5)
    ydata_old = np.copy(ydata)
    xdata_old = np.copy(xdata)
    plt.text(xdata[0], ydata[-1]*1.03,  2**i, ha="center")

print(nlet, ntot, float(nlet) / ntot)

ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.get_yaxis().set_visible(False)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%-d %b'))

plt.grid(ls="--", alpha=0.3)
fig.autofmt_xdate()
plt.show()


