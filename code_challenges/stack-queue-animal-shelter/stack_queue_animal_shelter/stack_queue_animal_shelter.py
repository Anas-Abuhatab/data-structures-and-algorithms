from stack_queue_animal_shelter.queue import Queue

class Animal:
  def __init__(self, type,name):
      self.type = type
      self.name = name

class AnimalShelter:
  def __init__(self):
      self.cat = Queue()
      self.dogs = Queue()

  def enqueue(self,animal):
    if animal.type == "cat" :
      self.cat.enqueue(animal)
      return self.cat.front.value.name
    elif animal.type == "dog":
      self.dogs.enqueue(animal)
      return self.cat.front.value.name
    else:
      raise Exception("Error type")


  def dequeue(self,preference):
    if preference == "cat":
      self.cat.dequeue()
      return self.cat.front.value.name 
    elif preference == "dog":
      self.dogs.dequeue()
      return self.cat.front.value.name 
    else:
      raise Exception("Error type")

