spy={
    'name': 'Bond',
    'salutation': 'Mr.',
    'age': 23,
    'rating': 4.7
}
class Spy:
    def __init__(self,name,age,salutation,rating):
        self.name = name
        self.age = age
        self.salutation = salutation
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

spy = Spy('Bond',23,'Mr.',4.7)