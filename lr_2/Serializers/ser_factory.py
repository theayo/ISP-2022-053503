from json_serializer.json_serializer import Json_serilizer_
from toml_serializer.toml_serializer import Toml_serilizer_
from yaml_serializer.yaml_serializer import Yaml_serilizer_

'''FAbrica rework'''
class Fack:
    def create_serializer(self, format):
        if format == 'JSON':
            return Json_serilizer_()
        elif format == 'Yaml':
            return Yaml_serilizer_()
        elif format == 'TOml':
            return Toml_serilizer_()
        else:
            raise ValueError(format)
