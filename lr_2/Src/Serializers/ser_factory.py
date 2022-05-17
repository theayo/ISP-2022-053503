"""Serializer factory"""
from Src import Serializers


class SerializerFactory:
    """Serializer factory"""

    def __int__(self):
        pass

    @staticmethod
    def create_serializer(serializer_type: str) -> Src.Serializers.serializer:
        """Return serializer when got extension"""
        if serializer_type == 'json':
            return Serializers.JsonSerializer()
        if serializer_type == 'yaml':
            return Serializers.YamlSerializer()
        if serializer_type == 'toml':
            return Serializers.TomlSerializer()

        raise ValueError(format)
