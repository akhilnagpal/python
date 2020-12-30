import addressbook.addressbook_pb2 as addressbook_pb2

addressBook = addressbook_pb2.AddressBook()

person1 = addressbook_pb2.Person()
person1.name = "Akhil"
person1.id = 555
person1.email = "fgfg"
person1.phones.add(number="455555", type=addressbook_pb2.Person.HOME)

person2 = addressBook.people.add()
person2.name = "Deeya"
person2.id = 888
person2.email = "fgffgdfgg"
person2.phones.add(number="6767676", type=addressbook_pb2.Person.WORK)

addressBook.people.extend([person1])

print(addressBook)
