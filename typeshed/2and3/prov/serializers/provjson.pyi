# Stubs for prov.serializers.provjson (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from prov.constants import *
import json
from prov.serializers import Error, Serializer
from typing import Any

logger: Any
__email__: str

class ProvJSONException(Error): ...

class AnonymousIDGenerator:
    def __init__(self) -> None: ...
    def get_anon_id(self, obj, local_prefix: str = ...): ...

LITERAL_XSDTYPE_MAP: Any

class ProvJSONSerializer(Serializer):
    def serialize(self, stream, **kwargs): ...
    def deserialize(self, stream, **kwargs): ...

class ProvJSONEncoder(json.JSONEncoder):
    def default(self, o): ...

class ProvJSONDecoder(json.JSONDecoder):
    def decode(self, s, *args, **kwargs): ...

def valid_qualified_name(bundle, value): ...
def encode_json_document(document): ...
def encode_json_container(bundle): ...
def decode_json_document(content, document): ...
def decode_json_container(jc, bundle): ...
def encode_json_representation(value): ...
def decode_json_representation(literal, bundle): ...
def literal_json_representation(literal): ...