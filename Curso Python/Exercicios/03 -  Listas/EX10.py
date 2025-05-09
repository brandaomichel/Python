array = ['0' if len(str(x)) > 1 and str(x)[1] == '0' else '-' for x in range(0, 100)]
print(array)