"""Json Serializer"""

import Serializers.serialiazer_process as process
from Serializers.serializer import Serializer
from Serializers.json_packer import to_str


class JsonSerializer(Serializer):
    """Class for JSonSerializer"""

    def dumps(self, obj: any):
        """Json convert from obj to string"""
        return to_str(process.serialize(obj))

    def loads(self, string: str):
        """Json convert from string to obj"""
        null = None
        dict_obj = eval(string)
        return process.deserialize(dict_obj)
