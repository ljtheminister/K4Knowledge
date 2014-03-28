import numpy as np
import pandas as pd
import os
from collections import defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas.tools.rplot as rplot


base_dir = os.getcwd() + '/'
data = pd.read_csv(base_dir + 'astudentData.csv')
grouped = data.groupby('question_id')

Q_counts = defaultdict(int)
Q_correct = defaultdict(int)
Q = data['question_id'].unique()

for row_idx in xrange(len(data)):
    x = data.ix[row_idx,:]
    id = x['question_id']
    Q_counts[id] += 1
    Q_correct[id] += x['correct']

Q_correct_pct = dict()
for q in Q:
     Q_correct_pct[q] = Q_correct[q]/float(Q_counts[q])

for q in Q:
    print Q_counts[q]


#mpl.style.use('ggplot') #only works for matplotlib >= 1.4
plt.scatter(Q_correct_pct.keys(), Q_correct_pct.values())
plot = rplot.RPlot(Q_correct_pct.values())
plot.render(plt.gcf())
plt.show()

pandas.tools.plotting.scatter_matrix(Q_correct.pct.values())

plot = rplot.RPlot(Q_correct_pct.values())
plot.render(plt.gcf())
plt.show()


plt.plot(Q_correct_pct.keys(), Q_correct_pct.values())

plt.plot(Q_counts.keys(), Q_counts.values())

plt.hist

