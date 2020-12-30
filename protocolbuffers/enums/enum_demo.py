from protocolbuffers import enums as enum_example_pb2

enum_message = enum_example_pb2.EnumMessage()

enum_message.id = 232
enum_message.day_of_week = enum_message.THURSDAY

print(enum_message)