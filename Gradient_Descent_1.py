import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('data.csv')
x=data.iloc[:,0:1]
y=data.iloc[:,1:2]
y=np.array(y)
x=np.array(x)
#converting array into numpy array so that iterations become easy and fast
alp=0.0001
iter=9000  #in this case only 10 iterations are enough to get minimum point
n=len(x)
#y=m_curr*x+b_curr
#slope=m_curr  slope gives directin
#intercept=b_curr  intercept gives position on Y-axis
m_curr=b_curr=0
#setting initial values
m_1=[]
b_1=[]
cost_1=[]

z=[i for i in range(iter)]
for i in range(iter):
    y_pred=m_curr*x+b_curr
    cost=1/n*(sum([val**2 for val in y-y_pred]))
    m_next=-2/n*sum(x*(y-y_pred))
    b_next=-2/n*sum(y-y_pred)
    m_curr=m_curr-alp*m_next
    b_curr=b_curr-alp*b_next
    #print("Cost>>{}\t\tm_1>>{}\t\tb_1>>{}".format(cost,m_curr,b_curr))
    #appending all data to list so that we can plot graph
    m_1.append(float(m_curr))
    b_1.append(float(b_curr))
    cost_1.append(float(cost))
   


plt.figure(1)
#plot between Cost and Slope
plt.grid()
plt.ylabel('Cost')
plt.xlabel('Slope')
plt.plot(cost_1,m_1)

plt.figure(2)
#plot between cost and intecept
plt.grid()
plt.ylabel('Cost')
plt.xlabel('intercept')
plt.plot(cost_1,b_1)

plt.figure(3)
#plot betwen cost and number of iteration
plt.grid()
plt.ylabel('Cost')
plt.xlabel('iteration')
plt.scatter(cost_1,z)

plt.figure(4)
#plot between x and y datapoinst
plt.grid()
plt.ylabel('X')
plt.xlabel('Y')
plt.scatter(x,y)


plt.show()
print(min(cost_1)) #minimum value of Cost(mean squared error)


