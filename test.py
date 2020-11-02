import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
from random import random as rand

now = datetime.datetime.now()


doubling_time = 7  # PARAMETER
plet = 2.36e-2 * doubling_time / 30.  # PARAMETER, % morti in 30 gg di contagiati
ptin = 1e-1 * doubling_time / 30.  # PARAMETER, % TI in 30 gg di contagiati
print(1e0 / plet, plet)

xdata_old = [now]
ydata_old = [0.5]
w = 1e0

fig = plt.figure()

nlet = 0
ntot = 0

for i in range(10):
    dy = w / (2**i + 1)
    ydata = np.array([dy * (j + 1) for j in range(2**i)])
    # add doubling time to date
    xdata = np.array([now + datetime.timedelta(days=i * doubling_time) for _ in ydata])
    # randomize letality
    ldata = np.array([rand() < plet for _ in xdata])
    # randomize TI
    tdata = np.array([rand() < ptin for _ in xdata])

    # blue dots
    plt.scatter(xdata, ydata, color="tab:blue", s=2)
    # red dots
    plt.scatter(xdata[ldata], ydata[ldata], color="tab:red", s=30, zorder=999)
    # plt.scatter(xdata[tdata], ydata[tdata], color="tab:green", s=30, zorder=998)

    # total death
    nlet += np.sum(ldata)
    # total infected
    ntot += len(ldata)
    
    # connection lines
    for j in range(2**i):
        plt.plot([xdata[j], xdata_old[j // 2]], [ydata[j], ydata_old[j // 2]], color="tab:blue", lw=.5, alpha=.5)
    ydata_old = np.copy(ydata)
    xdata_old = np.copy(xdata)

    # text number of total infected
    plt.text(xdata[0], ydata[-1]*1.03,  ntot, ha="center")

# check if letality is fine
print(nlet, ntot, float(nlet) / ntot)

# remove some axis and do some style
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.get_yaxis().set_visible(False)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%-d %b'))
fig.autofmt_xdate()

plt.grid(ls="--", alpha=0.3)
plt.show()


