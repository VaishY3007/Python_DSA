def Substr(Str):
    print(Str)
    indexes = [i for i in range(len(Str)) if Str.startswith("is", i)]
    print("Indexes where 'is' is present:", indexes)

Substr("This is a sample. jist trying it")
