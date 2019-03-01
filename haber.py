#status 1-lived morethan or equals to 5 years
#status 2 lived less than 5 years
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

haber=pd.read_csv("haberman.csv")



#2d scatter plot
haber.plot(kind="scatter",x="age",y="status")
haber.plot(kind="scatter",x="nodes",y="status")
haber.plot(kind="scatter",x="year",y="status")
plt.show()


#pair plots
sns.set_style("whitegrid")
sns.pairplot(haber,hue="status",size=4)
plt.show()


sns.FacetGrid(haber,hue="status",size=4)\
   .map(sns.distplot,"age")\
   .add_legend()
plt.show()
sns.FacetGrid(haber,hue="status",size=4)\
   .map(sns.distplot,"year")\
   .add_legend()
plt.show()
sns.FacetGrid(haber,hue="status",size=4)\
   .map(sns.distplot,"nodes")\
   .add_legend()
plt.show()

#pdf blue
#cdf red
#histogram,pdf,cdf
counts,bin_edges=np.histogram(haber["age"],bins=5,density=True)
pdf=counts/sum(counts)
cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)
plt.show()

counts,bin_edges=np.histogram(haber["nodes"],bins=5,density=True)
pdf=counts/sum(counts)
cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)
plt.show()

counts,bin_edges=np.histogram(haber["year"],bins=5,density=True)
pdf=counts/sum(counts)
cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)
plt.show()

print(np.percentile(haber["age"],np.arange(1,100,25)))
print(np.percentile(haber["year"],np.arange(1,100,25)))
print(np.percentile(haber["nodes"],np.arange(1,100,25)))

#box plots
sns.boxplot(x="status",y="age",data=haber)
plt.show()
sns.boxplot(x="status",y="year",data=haber)
plt.show()
sns.boxplot(x="status",y="nodes",data=haber)
plt.show()
#violin plots
sns.violinplot(x="status",y="age",data=haber,size=4)
plt.show()
sns.violinplot(x="status",y="year",data=haber,size=4)
plt.show()
sns.violinplot(x="status",y="nodes",data=haber,size=4)
plt.show()

########################Obeservation######################
#####graph################333
"""box plots and cdf pdf were more useful and accurate,scatter plots were not much clear"""
#####Analysis#####################
"""
there is 80% chance of having positive nodes(pdf,cdf)
if nodes are more than 8 than chances of not living 5 years are very high(violin plots)
year people did treatment before 1962 have more chances of not living more than 5 years(box plots)
age people having age less than 35 have almost 100% chance of living morethan 5 years(box plots)
"""
