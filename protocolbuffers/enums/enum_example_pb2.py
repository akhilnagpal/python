# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enum_example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='enum_example.proto',
  package='enumeration',
  syntax='proto3',
  serialized_pb=_b('\n\x12\x65num_example.proto\x12\x0b\x65numeration\"\xd0\x01\n\x0b\x45numMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12:\n\x0b\x64\x61y_of_week\x18\x02 \x01(\x0e\x32%.enumeration.EnumMessage.DayOfTheWeek\"y\n\x0c\x44\x61yOfTheWeek\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06MONDAY\x10\x01\x12\x0b\n\x07TUESDAY\x10\x02\x12\r\n\tWEDNESDAY\x10\x03\x12\x0c\n\x08THURSDAY\x10\x04\x12\n\n\x06\x46RIDAY\x10\x05\x12\x0c\n\x08SATURDAY\x10\x06\x12\n\n\x06SUNDAY\x10\x07\x62\x06proto3')
)



_ENUMMESSAGE_DAYOFTHEWEEK = _descriptor.EnumDescriptor(
  name='DayOfTheWeek',
  full_name='enumeration.EnumMessage.DayOfTheWeek',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONDAY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TUESDAY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEDNESDAY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THURSDAY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIDAY', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SATURDAY', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUNDAY', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=123,
  serialized_end=244,
)
_sym_db.RegisterEnumDescriptor(_ENUMMESSAGE_DAYOFTHEWEEK)


_ENUMMESSAGE = _descriptor.Descriptor(
  name='EnumMessage',
  full_name='enumeration.EnumMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='enumeration.EnumMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_of_week', full_name='enumeration.EnumMessage.day_of_week', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENUMMESSAGE_DAYOFTHEWEEK,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=244,
)

_ENUMMESSAGE.fields_by_name['day_of_week'].enum_type = _ENUMMESSAGE_DAYOFTHEWEEK
_ENUMMESSAGE_DAYOFTHEWEEK.containing_type = _ENUMMESSAGE
DESCRIPTOR.message_types_by_name['EnumMessage'] = _ENUMMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnumMessage = _reflection.GeneratedProtocolMessageType('EnumMessage', (_message.Message,), dict(
  DESCRIPTOR = _ENUMMESSAGE,
  __module__ = 'enum_example_pb2'
  # @@protoc_insertion_point(class_scope:enumeration.EnumMessage)
  ))
_sym_db.RegisterMessage(EnumMessage)


# @@protoc_insertion_point(module_scope)
