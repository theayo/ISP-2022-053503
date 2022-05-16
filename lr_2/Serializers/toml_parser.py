"""Toml Serializer"""
import qtoml
from Serializers.serializer import Serializer
import Serializers.serialiazer_process as process


class TomlSerializer(Serializer):
    """Class for Toml serialization"""

    def dumps(self, obj: any):
        """Dump object to string"""
        ser_obj = process.serialize(obj)
        return qtoml.dumps(ser_obj, encode_none=())

    def loads(self, string: str):
        """Load object from string"""
        ser_obj = qtoml.loads(string)

        return process.deserialize(ser_obj)
