class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self._pet_type = value

    @property
    def owner(self):
        return self._owner
    
    # @owner.setter
    # def owner(self, owner):
    #     self._owner = owner

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet._owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Must be a pet")
        pet._owner = self

    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda pet: pet.name)