from .SMBClient import SMBClient
from .OtherSubClient import OtherSubClient


class FileClient:
    def __init__(self, config):
        self.smb_client = SMBClient(
            config.SMB_SERVER_USER_ID,
            config.SMB_SERVER_PASSWORD,
            config.SMB_SERVER_IP,
            config.SMB_SERVER_NAME,
            config.SMB_DEST_DIRPATH
            )

    def connect(self):
        self.smb_client.get_connection()

    def close(self):
        self.smb_client.close_connection()

    def save(self, src_dirpath, new_filename):
        return self.smb_client.fetch(
            src_dirpath,
            new_filename
            )


class OtherClient:
    def __init__(self):
        ## implement factory if pattern for further various subclients
        self.client = OtherSubClient

    def connect(self, *args):
        self.client.connect(*args)

    def close(self):
        self.client.close()

    def retieve(self, *args):
        self.client.retrieve(*args)


