import pysftp as sftp


def push_file_to_server():
    s = sftp.Connection(host='104.131.54.242', username='root', password='Wtwe1641!')

    local_path = ""
    remote_path = "/home/testme.txt"

    s.put(local_path, remote_path)
    s.close()