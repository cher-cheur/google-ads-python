# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/product_bidding_category_constant.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.enums import product_bidding_category_level_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_product__bidding__category__level__pb2
from google.ads.google_ads.v3.proto.enums import product_bidding_category_status_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_product__bidding__category__status__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/product_bidding_category_constant.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB#ProductBiddingCategoryConstantProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\nOgoogle/ads/googleads_v3/proto/resources/product_bidding_category_constant.proto\x12!google.ads.googleads.v3.resources\x1aHgoogle/ads/googleads_v3/proto/enums/product_bidding_category_level.proto\x1aIgoogle/ads/googleads_v3/proto/enums/product_bidding_category_status.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xac\x05\n\x1eProductBiddingCategoryConstant\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x32\n\x0c\x63ountry_code\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12N\n(product_bidding_category_constant_parent\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12i\n\x05level\x18\x05 \x01(\x0e\x32Z.google.ads.googleads.v3.enums.ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel\x12l\n\x06status\x18\x06 \x01(\x0e\x32\\.google.ads.googleads.v3.enums.ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus\x12\x33\n\rlanguage_code\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0elocalized_name\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x81\x01\xea\x41~\n7googleads.googleapis.com/ProductBiddingCategoryConstant\x12\x43productBiddingCategoryConstants/{product_bidding_category_constant}B\x90\x02\n%com.google.ads.googleads.v3.resourcesB#ProductBiddingCategoryConstantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_product__bidding__category__level__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_product__bidding__category__status__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_PRODUCTBIDDINGCATEGORYCONSTANT = _descriptor.Descriptor(
  name='ProductBiddingCategoryConstant',
  full_name='google.ads.googleads.v3.resources.ProductBiddingCategoryConstant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.ProductBiddingCategoryConstant.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v3.resources.ProductBiddingCategoryConstant.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='google.ads.googleads.v3.resources.ProductBiddingCategoryConstant.country_code', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product_bidding_category_constant_parent', full_name='google.ads.googleads.v3.resources.ProductBiddingCategoryConstant.product_bidding_category_constant_parent', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='google.ads.googleads.v3.resources.ProductBiddingCategoryConstant.level', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v3.resources.ProductBiddingCategoryConstant.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.ads.googleads.v3.resources.ProductBiddingCategoryConstant.language_code', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localized_name', full_name='google.ads.googleads.v3.resources.ProductBiddingCategoryConstant.localized_name', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352A~\n7googleads.googleapis.com/ProductBiddingCategoryConstant\022CproductBiddingCategoryConstants/{product_bidding_category_constant}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=1041,
)

_PRODUCTBIDDINGCATEGORYCONSTANT.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_PRODUCTBIDDINGCATEGORYCONSTANT.fields_by_name['country_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PRODUCTBIDDINGCATEGORYCONSTANT.fields_by_name['product_bidding_category_constant_parent'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PRODUCTBIDDINGCATEGORYCONSTANT.fields_by_name['level'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_product__bidding__category__level__pb2._PRODUCTBIDDINGCATEGORYLEVELENUM_PRODUCTBIDDINGCATEGORYLEVEL
_PRODUCTBIDDINGCATEGORYCONSTANT.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_product__bidding__category__status__pb2._PRODUCTBIDDINGCATEGORYSTATUSENUM_PRODUCTBIDDINGCATEGORYSTATUS
_PRODUCTBIDDINGCATEGORYCONSTANT.fields_by_name['language_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PRODUCTBIDDINGCATEGORYCONSTANT.fields_by_name['localized_name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['ProductBiddingCategoryConstant'] = _PRODUCTBIDDINGCATEGORYCONSTANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductBiddingCategoryConstant = _reflection.GeneratedProtocolMessageType('ProductBiddingCategoryConstant', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTBIDDINGCATEGORYCONSTANT,
  __module__ = 'google.ads.googleads_v3.proto.resources.product_bidding_category_constant_pb2'
  ,
  __doc__ = """A Product Bidding Category.
  
  
  Attributes:
      resource_name:
          The resource name of the product bidding category. Product
          bidding category resource names have the form:  ``productBiddi
          ngCategoryConstants/{country_code}~{level}~{id}``
      id:
          ID of the product bidding category.  This ID is equivalent to
          the google\_product\_category ID as described in this article:
          https://support.google.com/merchants/answer/6324436.
      country_code:
          Two-letter upper-case country code of the product bidding
          category.
      product_bidding_category_constant_parent:
          Resource name of the parent product bidding category.
      level:
          Level of the product bidding category.
      status:
          Status of the product bidding category.
      language_code:
          Language code of the product bidding category.
      localized_name:
          Display value of the product bidding category localized
          according to language\_code.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.ProductBiddingCategoryConstant)
  ))
_sym_db.RegisterMessage(ProductBiddingCategoryConstant)


DESCRIPTOR._options = None
_PRODUCTBIDDINGCATEGORYCONSTANT._options = None
# @@protoc_insertion_point(module_scope)
