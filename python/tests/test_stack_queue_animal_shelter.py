from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter,Animal



def test_enqueue():
    animalShelter = AnimalShelter()
    cat = Animal("cat","BSBS")
    actual=animalShelter.enqueue(cat)
    expected="BSBS"
    assert expected == actual

def test_dequeue():
    animalShelter = AnimalShelter()
    cat = Animal("cat","BSBS")
    ctual=animalShelter.enqueue(cat)
    actual=animalShelter.dequeue("cat")
    expected="BSBS"
    assert expected == actual




