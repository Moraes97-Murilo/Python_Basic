#Lets practice some plots
import matplotlib.pyplot as plt

#first try
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 
y = [0,0.8,1.7,2.6,3.8,4.5,5.5,6.3,7.4,8.2,7.3,6.4,5.8,4.7,3.4,1.9]

plt.plot(x,y)
plt.show()

#second try
a = []
b = []

for i in range(16):
  a.append(i)
  b.append(input("Type the value of Y: "))  

plt.bar(a,b)
plt.show()

#third try
f = []
g = []

for i in range(13):
  f.append(i)
  g.append(float(input("Type the value of Y: "))) 

for i in g:
  i**2

plt.scatter(f,g, marker='s', color='g', label='square')
plt.plot(f,g, color='r')
plt.savefig("scatterplot.png")
