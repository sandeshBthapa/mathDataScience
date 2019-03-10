import matplotlib.pyplot as plt
import numpy as np

data1 = np.linspace(0,5,5)
data2 = data1**2

frame = plt.figure()
axis = frame.add_axes([0.1,0.1,0.5,0.5])
axis.plot(data1,label='data1',marker='o',color='red')
axis.plot(data2,label='data2',marker='o')
plt.legend()
plt.tight_layout()
plt.xlabel('X')
plt.title('data compare')
plt.ylabel('Y')
plt.show()