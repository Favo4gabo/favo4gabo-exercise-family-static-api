
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"first_name":  "John",
             "last_name": last_name,
             "age": 33,
            "lucky_numbers": [7, 13, 22],
            "id": self._generateId()},

            {"first_name":  "Jane",
             "last_name": last_name,
             "age": 35,
            "lucky_numbers": [10, 14, 3],
            "id": self._generateId()},

            {"first_name":  "Jimmy",
             "last_name": last_name,
             "age": 5,
            "lucky_numbers": 1,
            "id": self._generateId()}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
    # LISTO

    def add_member(self, member):
        # fill this method and update the return
                    # append para agregar
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        count=0
        for member in self._members:
            if member["id"]==id:
                count+=1
                self._members.remove(member)
        if (count>=1):
            return None
        return {"done":True}

    def get_member(self, id):
        # fill this method and update the return
        member_needed=next((member for member in self._members if member["id"]==id),None)
        return member_needed if member_needed else {}

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    # LISTO
