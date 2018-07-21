plt.rcParams['axes.facecolor'] = (0.9176470588235294, 0.9176470588235294,
                                  0.9490196078431372, 1.0)
plt.grid(c='white')
plt.tick_params(axis='both', which='both', bottom=False, top=False,
                right=False, left=False, length=0)

plt.plot(dat1[:, 0], dat1[:, 3]/max(dat1[:, 3]), 'r')
sns.despine(top=True, right=True, left=True, bottom=True)

plt.show()
