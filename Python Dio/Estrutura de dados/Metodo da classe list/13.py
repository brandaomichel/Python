linguaguens = ['python', "js", "c", "java", "csharp"]

print(sorted(linguaguens, key=lambda x : len(x)))

print(sorted(linguaguens, key=lambda x : len(x), reverse=True))