import paramiko
import config
from scp import SCPClient

hostname = config.HOSTNAME
username = config.USERNAME
password = config.PASSWORD
private_key_path = config.PRIVATE_KEY_PATH


def init_ssh_client():
    print("Creating ssh client...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    my_key = paramiko.RSAKey.from_private_key_file(private_key_path)
    client.connect(hostname, username=username, pkey=my_key)
    return client


def scp_files_to_server(client):
    print("Scp config files to server...")
    files = [config.V2RAY_CONFIG_FILE_PATH, config.DOCKER_COMPOSE_FILE_PATH]
    remote_path = "/root/"
    with SCPClient(client.get_transport()) as scp:
        for file in files:
            scp.put(file, remote_path)


def install_docker_compose(client):
    print("Install docker-compose on server...")
    try:
        stdin, stdout, stderr = client.exec_command('apt install docker-compose -y')
        output = stdout.read()
        print(output.decode('utf-8'))
    except:
        print("error while installing docker-compose")


def up_docker_compose(client):
    print("Run v2ray docker-compose file...")
    try:
        stdin, stdout, stderr = client.exec_command('docker-compose up -d')
        output = stdout.read()
        print(output.decode('utf-8'))
    except:
        print("error while installing docker-compose")


if __name__ == "__main__":
    client = init_ssh_client()
    scp_files_to_server(client)
    install_docker_compose(client)
    up_docker_compose(client)
    client.close()
