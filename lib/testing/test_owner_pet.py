import pytest

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner")
        self.owner = owner
        Pet.all.append(self)

def test_owner_init():
    """Test Owner class initialization"""
    owner = Owner("John")
    assert owner.name == "John"

def test_pet_init():
    """Test Pet class initialization"""
    pet = Pet("Fido", "dog")
    assert pet.name == "Fido"
    assert pet.pet_type == "dog"

    owner = Owner("Jim")
    pet = Pet("Clifford", "dog", owner)
    assert pet.owner == owner

    Pet.all = []

def test_has_pet_types():
    """Test Pet class has variable PET_TYPES"""
    assert Pet.PET_TYPES == ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    Pet.all = []

def test_checks_pet_type():
    """Test Pet class validates pet_type"""
    with pytest.raises(Exception):
        Pet("Jim Jr.", "panda")

    Pet.all = []

def test_pet_has_all():
    """Test Pet class has variable all, storing all instances of Pet"""
    pet1 = Pet("Whiskers", "cat")
    pet2 = Pet("Jerry", "reptile")

    assert pet1 in Pet.all
    assert pet2 in Pet.all
    assert len(Pet.all) == 2

    Pet.all = []

def test_owner_has_pets():
    """Test Owner class has method pets(), returning all related pets"""
    owner = Owner("Ben")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)

    assert owner.pets() == [pet1, pet2]

    Pet.all = []

def test_owner_adds_pets():
    """Test Owner class has method add_pet(), validating and adding a pet"""
    owner = Owner("Ben")
    pet = Pet("Whiskers", "cat")
    owner.add_pet(pet)

    assert pet.owner == owner
    assert owner.pets() == [pet]

    Pet.all = []

def test_add_pet_checks_isinstance():
    """Test Owner class instance method add_pet() validates Pet type"""
    owner = Owner("Jim")
    with pytest.raises(Exception):
        owner.add_pet("Lucky")

    Pet.all = []

def test_get_sorted_pets():
    """Test Owner class has method get_sorted_pets, sorting related pets by name"""
    owner = Owner("John")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    pet3 = Pet("Whiskers", "cat", owner)
    pet4 = Pet("Jerry", "reptile", owner)
    
    assert owner.get_sorted_pets() == [pet2, pet1, pet4, pet3]