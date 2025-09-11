import matplotlib.pyplot as plt
import numpy as np

xs = np.array(['Janeiro', 'Fevereiro', 'Marco', 'Abril'])

time1 = np.array([5, 10, 15, 10])
time2 = np.array([2, 15, 12, 13])
time3 = np.array([1, 11, 12, 13])
time4 = np.array([6, 121, 11, 12])

plt.bar(xs, time1, color='g', width=0.5)
plt.bar(xs, time2, bottom=time1, color='blue', width=0.5)
plt.bar(xs, time3, bottom=time2+time1, color='yellow', width=0.5)
plt.bar(xs, time4, bottom=time1+time2+time3, color='red', width=0.5)

plt.title('Rendimento no Esporte')
plt.xlabel('Meses')
plt.ylabel('Gols')
plt.legend(['Time1', 'Time2', 'Time3', 'Time4'])
plt.show()