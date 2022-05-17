"""Control serializer process"""
import code
import sys
import importlib

from arg_parse import ArgParser
from Serializers import Serializer
import Serializers as fabric

load_obj, dump_obj, convert_info = ArgParser.get_args()


def get_serializer(filetype: str) -> Serializer:
    """Call fabric method and create instance of Serializer(json/toml/yaml)"""
    factory = fabric.SerializerFactory()
    serializer = factory.create_serializer(filetype)
    return serializer


def dump_obj_to_string(input_objs: str):
    """Dump object from string which parsed from Console"""

    def parse_fileinfo(input_str: str):
        """Get part of inputed string (filepath, object for dump and filetype)"""
        path_file, obj_for_dump, file_format = input_str.split(':')
        return path_file, obj_for_dump, file_format

    def get_object(file_pth: str, obj_n: str):
        """Got object from module"""
        module_name = file_pth.replace('.py', '').split('/')[-1]
        module_path = file_pth.replace(f'{module_name}.py', '')
        sys.path.append(module_path)

        module = importlib.import_module(module_name)

        item = module.__dict__.get(obj_n, None)
        return item

    def dump_object(obj_ser: any, ob_name, filetype: str):
        """Get serializer instance after call abstract method dump to file"""
        serializer = get_serializer(filetype)
        serializer.dump(obj_ser, ob_name + '.' + filetype)

    for input_obj in input_objs:
        file_path, obj_name, file_type = parse_fileinfo(input_obj)
        obj = get_object(file_path, obj_name)
        if obj is None:
            print(f"No such object named {obj_name} in module {file_path}")
            return

        dump_object(obj, obj_name, file_type)
        print(f"The object: {obj_name}({obj}) dumped into {obj_name}.{file_type}")


def load_obj_from_file(input_files: str):
    """Loads from file string parse this and convert to objects"""

    def load(file_path: str) -> any:
        """Get instance of serializer and call abstract method load"""
        filetype = file_path.split('.')[-1]

        serializer = get_serializer(filetype)
        obj = serializer.load(file_path)

        return obj

    for file_name in input_files:
        obj_name = file_name.split('.')[-2]
        locals().update({obj_name: load(file_name)})
        print(f'{obj_name} successfully loaded from {file_name}')
    code.interact(local=locals(), banner="Real human being", exitmsg='End of life')


def convert_obj(convert_str: str):
    """Convert from one extension to second"""

    def convert(file_name: str, file_type: str):
        old_type = file_name.split('.')[-1]
        serializer = get_serializer(old_type)
        obj = serializer.load(file_name)
        name = file_name.split('.')[0]

        new_serializer = get_serializer(file_type)
        new_serializer.dump(obj, name + '.' + file_type)
        print(f"{file_name} converted to {name}.{file_type}")

    filetypes = list(
        filter(lambda file: file.find('.') == -1, convert_str))
    start = 0
    end = 0

    for filetype in filetypes:
        end = convert_str.index(filetype, start)
        for i in range(start, end):
            convert(convert_str[i], filetype)
        start = end + 1


if load_obj is not None:
    load_obj_from_file(load_obj)

if dump_obj is not None:
    dump_obj_to_string(dump_obj)

if convert_info is not None:
    convert_obj(convert_info)
