"""Parse arg from command prompt"""

import argparse


class ArgParser:
    """Class for identify and parse args"""
    @staticmethod
    def create_parser():
        """Create console parser"""
        parser = argparse.ArgumentParser(prog="s3", description="Serializer/Deserializer",
                                         epilog="YO")

        parser.add_argument("-l", "--load", dest="load", metavar="filename", nargs="+",
                            help="Deserialize obj from file")
        parser.add_argument("-d", "--dump", dest="dump", metavar="filename$obj$format", nargs="+",
                            help="Serialize obj from file")
        parser.add_argument("-c", "--conv", dest="convert", metavar="filepath new_filetype", nargs="+",
                            help="Convert from _ to _")
        return parser

    @staticmethod
    def parse_args():
        """Start and parse args"""
        parser = ArgParser.create_parser()
        return parser.parse_args()

    @staticmethod
    def get_args():
        """Get args from console"""
        args = ArgParser.parse_args()
        return args.load, args.dump, args.convert
