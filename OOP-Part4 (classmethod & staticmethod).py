class Office:
    number_of_people = -1    # Var for the whole class
    def __init__(self,name):
        self.name = name
     #   Office.number_of_people +=1 # thats how you access var defined in for the whole class
        Office.number_of_people_()  # Thats how you can access methods made for he whole class

    @classmethod
    def number_of_people_(cls): # notice that you don't have to pass self for this function instead just pass cls for class
        cls.number_of_people +=1
        return cls.number_of_people

    @staticmethod
    def add5(x):    # static methods require no arguments unless ofc you want to give some
        # Office.number_of_people +=1
        return x + 5

s1 = Office("Trim")
s2 = Office("Shave")
print(Office.number_of_people_())
print(Office.add5(3))
print(Office.number_of_people_())