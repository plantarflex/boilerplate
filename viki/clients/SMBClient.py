import socket
import os
from io import BytesIO
from datetime import datetime, timedelta


from smb.SMBConnection import SMBConnection
from smb import smb_structs


class SMBClient:
    def __init__(
        self,
        user_id,
        password,
        server_ip,
        server_name,
        dest_dirpath
        ):
        self.user_id = user_id
        self.password = password
        self.server_ip = server_ip
        self.client_name = socket.gethostname()
        self.server_name = server_name
        self.dest_dirpath = dest_dirpath

    def get_connection(self):
        conn = SMBConnection(
            self.user_id,
            self.password,
            self.client_name,
            self.server_name,
            use_ntlm_v2=True,
            is_direct_tcp=True
            )
        try:
            conn.connect(self.server_ip, 445)
            print(conn.echo('SMB CONNECTED'))
            self.conn = conn
        except Exception as e:
            print(e)

    def close_connection(self):
        if self.conn is None:
            print('SMB NOT CONNECTED')
            return
        self.conn.close()
        print('SMB CLOSED GRACEFULLY')

    def get_file_obj(self, src_filepath):
        file_obj = BytesIO()
        try:
            file_attributes, file_size = self.conn.retrieveFile(
                self.server_name,
                src_filepath,
                file_obj)
            file_obj.seek(0)
            return file_obj, file_size
        except Exception as e:
            print(e)
            return None, 0

    def fetch(self, src_dirpath, new_filename):
        if not os.path.exists(self.dest_dirpath):
            os.makedirs(self.dest_dirpath)
        src_filepath = os.path.join(src_dirpath, new_filename)
        dest_filepath = os.path.join(self.dest_dirpath, new_filename)

        file_obj, file_size = self.get_file_obj(src_filepath)
        if file_obj is None or file_size <= 0:
            return dest_dirpath, False
        with open(dest_filepath, 'wb') as fp:
            fp.write(file_obj.read())
        return dest_filepath, True


