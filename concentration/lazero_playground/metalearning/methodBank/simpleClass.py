from storeADill import storeAList
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

joke=Person((lambda x: x*2),(lambda y: y-1))
print("--","sample:",joke.name(5),joke.age(4),"--")
storeAList(joke)
