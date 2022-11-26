class Product:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __call__(self, name, age):
        self.name=name
        print(self.name)
    

p=Product('Emu', 22)
p('Samiul',33)