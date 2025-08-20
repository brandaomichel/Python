import pandas as pd, numpy
series = pd.Series([1, 2, 3, 4, 5], dtype='i4', name='Numeros', index=["Um", "Dois", "Tres", "Quatro", "Cinco"])
print(series["Cinco"])
print(series.shape)
series2 = pd.Series([1, 2, 3, 4, 5], dtype='i4', name='Numeros', index=["Um", "Dois", "Tres", "Quatro", "Cinco"])

series2["Seis"] = 6
print(series2)

array = numpy.array([45.2, 4.50, 65.7, 98.7])
pesos = pd.Series(array, index=['Carlos', 'Jose', 'Maria', 'Fernanda'])
print(pesos)
print(type(pesos))