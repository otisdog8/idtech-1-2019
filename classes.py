class testclass:
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def test(self,toast):
        pass

class toastclass(testclass):
    otis = testclass("99","otis")

print(toastclass.otis.age)
