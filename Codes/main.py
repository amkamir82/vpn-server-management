import paramiko
import config
from scp import SCPClient

hostname = config.HOSTNAME
username = config.USERNAME
password = config.PASSWORD
private_key_path = config.PRIVATE_KEY_PATH


def init_ssh_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    my_key = paramiko.RSAKey.from_private_key_file(private_key_path)
    client.connect(hostname, username=username, pkey=my_key)
    return client

