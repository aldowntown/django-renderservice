# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: render_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='render_service.proto',
  package='render_service',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14render_service.proto\x12\x0erender_service\",\n\rRenderRequest\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05props\x18\x03 \x01(\t\"!\n\x0eRenderResponse\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t2Z\n\rRenderService\x12I\n\x06Render\x12\x1d.render_service.RenderRequest\x1a\x1e.render_service.RenderResponse\"\x00\x62\x06proto3')
)




_RENDERREQUEST = _descriptor.Descriptor(
  name='RenderRequest',
  full_name='render_service.RenderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='render_service.RenderRequest.name', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='props', full_name='render_service.RenderRequest.props', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=84,
)


_RENDERRESPONSE = _descriptor.Descriptor(
  name='RenderResponse',
  full_name='render_service.RenderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='render_service.RenderResponse.content', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['RenderRequest'] = _RENDERREQUEST
DESCRIPTOR.message_types_by_name['RenderResponse'] = _RENDERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RenderRequest = _reflection.GeneratedProtocolMessageType('RenderRequest', (_message.Message,), dict(
  DESCRIPTOR = _RENDERREQUEST,
  __module__ = 'render_service_pb2'
  # @@protoc_insertion_point(class_scope:render_service.RenderRequest)
  ))
_sym_db.RegisterMessage(RenderRequest)

RenderResponse = _reflection.GeneratedProtocolMessageType('RenderResponse', (_message.Message,), dict(
  DESCRIPTOR = _RENDERRESPONSE,
  __module__ = 'render_service_pb2'
  # @@protoc_insertion_point(class_scope:render_service.RenderResponse)
  ))
_sym_db.RegisterMessage(RenderResponse)



_RENDERSERVICE = _descriptor.ServiceDescriptor(
  name='RenderService',
  full_name='render_service.RenderService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=121,
  serialized_end=211,
  methods=[
  _descriptor.MethodDescriptor(
    name='Render',
    full_name='render_service.RenderService.Render',
    index=0,
    containing_service=None,
    input_type=_RENDERREQUEST,
    output_type=_RENDERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RENDERSERVICE)

DESCRIPTOR.services_by_name['RenderService'] = _RENDERSERVICE

# @@protoc_insertion_point(module_scope)
