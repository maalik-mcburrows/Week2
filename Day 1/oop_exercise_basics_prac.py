class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
    def greet(self, other_person):
         print("Hello {}, I am {}!".format(other_person.name, self.name))
    def print_contact_info(self):
        print("{}'s email: {}, {}'s phone number: {}".format(self.name, self.email, self.name, self.phone))
    def __init__(self, friend_name):
        self.friend_name = friend_name


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456") 

sonny.greet(jordan)
jordan.greet(sonny)

# print(sonny.email, sonny.phone)
# print(jordan.email, jordan.phone)

# sonny.print_contact_info()
# jordan.print_contact_info()