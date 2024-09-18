linguaguens = ['python', "js", "c", "java", "csharp"]

linguaguens.sort()

print(linguaguens)

linguaguens = ['python', "js", "c", "java", "csharp"]

linguaguens.sort(reverse=True)

print(linguaguens)

linguaguens = ['python', "js", "c", "java", "csharp"]

linguaguens.sort(key=lambda x:len(x))

print(linguaguens)

linguaguens = ['python', "js", "c", "java", "csharp"]

linguaguens.sort(key=lambda x: len(x), reverse=True)

print(linguaguens)