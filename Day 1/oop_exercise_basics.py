class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.greeting_count = 0
    def add_friend(self, other_person):
        self.friends.append(other_person)
        print("{} added to {}'s friends.".format(other_person.name, self.name))
    def num_friends(self):
        print("{} has {} friends.".format(self.name, len(self.friends)))
    def greet(self, other_person):
         print("Hello {}, I am {}!".format(other_person.name, self.name))
         print(" ")
         self.greeting_count += 1
         print("{}'s greet count: {}.".format(self.name, self.greeting_count))
    def print_contact_info(self):
        print("{}'s email: {}, {}'s phone number: {}".format(self.name, self.email, self.name, self.phone))
    def string(self):
        print("Person: {}, {}, {}".format(self.name, self.email, self.phone))
    

        

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456") 

print(" ")
sonny.greet(jordan)
print(" ")
jordan.greet(sonny)





# print(sonny.email, sonny.phone)
# print(jordan.email, jordan.phone)
print(" ")
sonny.print_contact_info()
print(" ")
jordan.print_contact_info()

# sonny.friends.append("jordan")
# print(len(sonny.friends))
print(" ")
sonny.add_friend(jordan)
# print(len(sonny.friends))
print(" ")
sonny.num_friends()
print(" ")
jordan.string()
print(" ")
# sonny.friends[0].greet(sonny)