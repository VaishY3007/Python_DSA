def College(name):
    print(f'College Name: {name}')
    def Group(gName):
        print(f'You are admiitted to: {gName} Group')
        def Section(className):
            print(f'You are in {className} part of {gName}')
        return Section
    return Group
clg = College('XYZ')
group = clg('Science')
section = group('Mathematics Hons')