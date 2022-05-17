"""Yaml serializer"""
from Src.Serializers.serializer import Serializer
import Src.Serializers.serialiazer_process as process
from yaml import safe_load, dump


class YamlSerializer(Serializer):
    """Class for YAml serialization"""

    def dumps(self, obj: any):
        """Serialize object, class or function to yaml."""
        ser_obj = process.serialize(obj)
        return dump(ser_obj)

    def loads(self, string: str):
        """Deserialize object, class or function from yaml."""
        ser_obj = safe_load(string)
        return process.deserialize(ser_obj)
