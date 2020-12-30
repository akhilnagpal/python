import complex.complex_pb2 as complex_pb2

complex_message = complex_pb2.ComplexMessage()

complex_message.one_dummy.id = 123
complex_message.one_dummy.name = "Akhil Dummy"

first_multiple_dummy = complex_message.multiple_dummy.add()
first_multiple_dummy.id = 456
first_multiple_dummy.name = "Aryan"

complex_message.multiple_dummy.add(id=789, name="Nagpal")


print(complex_message)
