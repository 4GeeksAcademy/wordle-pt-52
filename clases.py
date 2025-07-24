class Animal:
    def __init__(self, name, gender, age=0,):
        self.name = name
        self.age = age
        self.gender = gender

    def sleep(self):
        print(f"{self.name} esta mimiendo. 💤")

class Felino:
    pass

class Gato(Animal, Felino):

    lista_de_gatos = []

    def __init__(self, name, gender, color_pelaje, age=0):
        super().__init__(name, gender, age)
        self.color_pelaje = color_pelaje

        self.lista_de_gatos.append(self)
    
    def purr(self): # Metodos
        print(f"{self.name} ha maullado. 🐱")

    def __repr__(self):
        sustantive = 'gatito' if self.gender != "femenino" else 'gatita'
        return f"un {sustantive} llamado {self.name}"

    @classmethod # decorador
    def say_hello(cls):
        print(cls.lista_de_gatos)
        print("Hey this is the class Cat.")

    @staticmethod
    def say_bye():
        print("Hey im a static method.")


# key - arguments o kargs
#michi = Gato(name="KaiSa", age=6, color_pelaje="naranja", gender="femenino")

# print(michi)
# print(michi.age)
# print(michi.color_pelaje)

# michi.purr()
# michi.sleep()

Gato.say_bye()