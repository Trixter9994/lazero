from storeADill import storeAList
from testR import jokeMeUp
class Person:
  def __init__(self, name):
    self.name = name
#    self.age = age

joke=Person(jokeMeUp)
#print("--","sample:",joke.name(5),joke.age(4),"--")
joke.name()
storeAList(joke)
