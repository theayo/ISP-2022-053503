"""Abstract class for serializers"""

from abc import ABC, abstractmethod


class Serializer(ABC):
    """Abstract class for serializers"""

    def dump(self, obj: any, filepath: str):
        """Serialize object to file"""
        with open(filepath, 'w', encoding='utf8') as file:
            file.write(self.dumps(obj))

    @abstractmethod
    def dumps(self, obj: any):
        """Serialize object to string"""
        pass

    def load(self, filepath: str):
        """Deserialize object from file"""
        with open(filepath, 'r', encoding='utf8') as file:
            string = file.read()
        return self.loads(string)

    @abstractmethod
    def loads(self, string: str):
        """Deserialize object from string"""
        pass

