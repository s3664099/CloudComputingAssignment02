# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery_v2/proto/encryption_config.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/bigquery_v2/proto/encryption_config.proto",
    package="google.cloud.bigquery.v2",
    syntax="proto3",
    serialized_options=_b(
        "\n\034com.google.cloud.bigquery.v2B\025EncryptionConfigProtoZ@google.golang.org/genproto/googleapis/cloud/bigquery/v2;bigquery"
    ),
    serialized_pb=_b(
        '\n6google/cloud/bigquery_v2/proto/encryption_config.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto"R\n\x17\x45ncryptionConfiguration\x12\x37\n\x0ckms_key_name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x01\x42w\n\x1c\x63om.google.cloud.bigquery.v2B\x15\x45ncryptionConfigProtoZ@google.golang.org/genproto/googleapis/cloud/bigquery/v2;bigqueryb\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_ENCRYPTIONCONFIGURATION = _descriptor.Descriptor(
    name="EncryptionConfiguration",
    full_name="google.cloud.bigquery.v2.EncryptionConfiguration",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="kms_key_name",
            full_name="google.cloud.bigquery.v2.EncryptionConfiguration.kms_key_name",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\001"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=179,
    serialized_end=261,
)

_ENCRYPTIONCONFIGURATION.fields_by_name[
    "kms_key_name"
].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name["EncryptionConfiguration"] = _ENCRYPTIONCONFIGURATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EncryptionConfiguration = _reflection.GeneratedProtocolMessageType(
    "EncryptionConfiguration",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ENCRYPTIONCONFIGURATION,
        __module__="google.cloud.bigquery_v2.proto.encryption_config_pb2",
        __doc__="""Encryption configuration.

  Attributes:
      kms_key_name:
          Optional. Describes the Cloud KMS encryption key that will be
          used to protect destination BigQuery table. The BigQuery
          Service Account associated with your project requires access
          to this encryption key.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.v2.EncryptionConfiguration)
    ),
)
_sym_db.RegisterMessage(EncryptionConfiguration)


DESCRIPTOR._options = None
_ENCRYPTIONCONFIGURATION.fields_by_name["kms_key_name"]._options = None
# @@protoc_insertion_point(module_scope)
