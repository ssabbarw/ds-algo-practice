class Language:
    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            print("making instance")
            cls._instance = super().__new__(cls)

        print("returning  instance")
        return cls._instance

    def __init__(self, a,b):
        self.a = a
        self.b = b


print()
l1 = Language(1,2)
print(l1.a, l1.b, "\n")
l2 = Language(3,4)
print(l2.a, l2.b)
print(l1.a, l1.b)
