import pandas as pd
import matplotlib.pyplot as plt
url= "/Users/LlewelynRW/Dropbox/Computation in Python/Computational-science/Computational_Science/Sport_Analytics"
df = pd.read_csv(url+"Lions-v-NZ.csv", names=['date','month','yr','datestamp','venue','NZ','Lions','Winner'])
df.loc[df['Winner'] == 'NZ', 'NZwin'] = 1
df.loc[df['Winner'] == 'Lions', 'NZwin'] = 0
df.loc[df['Winner'] == 'Draw', 'NZwin'] = 0.5
df.datestamp = pd.to_datetime(df.datestamp)
#Visualise results
plt.plot(df.datestamp,df.NZ-df.Lions,'k+')
plt.axhline()
plt.title("NZ-v-Lions results 1908 - 2005")
plt.xlabel("Date")
plt.ylabel("NZ-Lions score")
df1 = pd.DataFrame({'NZ':df.NZ,'Lions':df.Lions})
df1.plot.hist(alpha=.3)
df1.plot.kde(alpha=.3)
