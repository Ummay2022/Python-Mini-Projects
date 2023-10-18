import Person


class FamilyTree:
    def __init__(self, root: Person):
        self.persons = {0: root}  
        self.next_id = 1  
        self.root_id = 0  

    def get_root(self) -> int:
        return self.root_id

    def insert_as_child_for_id(self, person: Person, parent: int):
        person_id = self.next_id
        self.persons[person_id] = person
        self.persons[parent].get_children().append(person_id)
        self.persons[person_id].parent = parent  # Set the parent ID for the person
        self.next_id += 1
        return person_id

    def get_parent_of(self, person_id: int) -> int:
        if person_id in self.persons:
            return self.persons[person_id].parent_id
        return -1  

    def get_siblings_of(self, person_id: int) -> [int]:
        parent_id = self.get_parent_of(person_id)
        if parent_id != -1:
            siblings = []
            for child_id in self.persons[parent_id].get_children():
                if child_id != person_id:
                    siblings.append(child_id)
            return siblings
        return []


    def get_children_of(self, person_id: int) -> [int]:
        if person_id in self.persons:
            return self.persons[person_id].get_children()
        return []


    def get_nieces_nephews_of(self, person_id: int) -> [int]:
        parent_id = self.get_parent_of(person_id)
        if parent_id != -1:
            nieces_nephews = []
            for child_id in self.get_siblings_of(person_id):
                nieces_nephews.extend(self.get_children_of(child_id))
            return nieces_nephews
        return []


    def get_cousins_of(self, person_id: int) -> [int]:
        parent_id = self.get_parent_of(person_id)
        if parent_id != -1:
            cousins = []
            parent_siblings = self.get_siblings_of(parent_id)
            for sibling_id in parent_siblings:
                cousins.extend(self.get_children_of(sibling_id))
            return cousins
        return []

    def get_person_by_id(self, person_id: int) -> Person:
        return self.persons.get(person_id, None)

