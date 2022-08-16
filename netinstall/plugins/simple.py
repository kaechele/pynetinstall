import os
from io import BufferedReader
from configparser import ConfigParser


class Plugin:
    def __init__(self, config: ConfigParser):
        self.config = config
        print(self.config)

    def get_files(self, *args, **kwargs) -> tuple[tuple[BufferedReader, str, int], tuple[BufferedReader, str, int]]:
        """
        Searches for the path of the .npk and .rsc files in the config

        Returns:
         - (BufferedReader, str, int) (BufferedReader, str, int): 
           Tuple including the path to the .npk and the .rsc file
           (ROUTEROS.npk, CONFIG.rsc)
        """
        firmw = self.config["pynetinstall"]["firmware"]
        conf = self.config["pynetinstall"]["config"]
        if firmw:
            if not os.path.exists(firmw):
                raise FileExistsError(f"File '{firmw}' doesn't exist")
        else:
            raise MissingArgument("RouterOS not defined")
        if conf:
            if not os.path.exists(conf):
                raise FileExistsError(f"File '{conf}' doesn't exist")
        else:
            raise MissingArgument("Configuration not defined")
        return open(firmw, "rb"), open(conf, "rb")


class MissingArgument(Exception):
    """
    Error raised when Plugin is missing an Configuration Argument
    """
    pass
