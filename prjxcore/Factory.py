import pickle
from abc import ABC, abstractmethod
from importlib import import_module
from pathlib import Path
from typing import List, Optional, Any

class Factory(ABC):
    store_path = None

    @classmethod
    def set_path(cls, path: str) -> None:
        """
        Set the path to the store directory
        :param path:
        :return: none
        """
        cls.store_path = path

    @classmethod
    def set_default_path(cls, project: str) -> None:
        """Set the path to the store directory for the given project.

        :param project: the name of the project
        :return: None
        """
        cls.store_path = str(Path(__file__).parent.parent) + "/store/"


    @classmethod
    def toClass(cls, class_path : str) -> Any:
        """
        Dynamically instantiate a class
        :param class_path:
        :return: class as an object
        """
        package, class_name = class_path.rsplit('.', 1)
        module = import_module(package)
        klass = getattr(module, class_name)
        return klass

    @classmethod
    def toFunction(cls, class_path, func_name):
        """
        Returns a function an object, so that it ran dynamically
        :param class_path:
        :param func_name:
        :return: function as object
        """
        class_obj = cls.toClass(class_path)
        function_result = getattr(class_obj, func_name)
        return function_result

    @classmethod
    def get_path(cls, filename: str) -> str:
        """
        Return the path to the pickle file.
        :param filename:
        :return: str
        """
        if cls.store_path is None:
            raise Exception("Store path not set")

        return cls.store_path + filename


    @classmethod
    def save(cls, filename, data) -> str:
        """Save data to a pickle file in the 'store' directory.

        :param filename: the name of the pickle file
        :param data: the data to be pickled and saved
        :return: None
        """
        with open(cls.get_path(filename), 'wb') as filehandle:
            pickle.dump(data, filehandle)

    @classmethod
    def load(cls, filename: str) -> Any:
        """Load data from a pickle file in the 'store' directory.

        :param filename: the name of the pickle file
        :return: the data that was unpickled from the file
        """
        with open(cls.get_path(filename), 'rb') as filehandle:
            return pickle.load(filehandle)
