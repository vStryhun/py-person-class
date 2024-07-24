class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None

        Person.people[name] = self

    def set_spouse(self, spouse_name: str) -> None:
        if spouse_name in Person.people:
            self.spouse = Person.people[spouse_name]
        raise ValueError(f"Spouse with name {spouse_name} does not exist.")


def create_person_list(people: list) -> list:
    for person in people:
        name = person["name"]
        spouse_name = person.get("wife") or person.get("husband")
        if spouse_name:
            Person.people[name].set_spouse(spouse_name)

    return list(Person.people.values())
