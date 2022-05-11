import argparse

parser = argparse.ArgumentParser(prog="s3", description="Serializer/Deserializer", epilog= "YO")
parser.add_argument("-l", "--load", dest="load", metavar="filename", nargs="+", help="Deserialize obj from file")
parser.add_argument("-d", "--dump", dest="dump", metavar="filename$obj$format", nargs="+",
                    help="Serialize obj from file")
