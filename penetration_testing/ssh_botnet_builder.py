# ssh_botnet_builder.py

import paramiko
import sys

def ssh_command(hostname, port, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        print(f"Output from {hostname}:")
        for line in stdout:
            print(line.strip('\n'))
    except paramiko.AuthenticationException:
        print(f"Failed to authenticate with {hostname}")
    except paramiko.SSHException as e:
        print(f"SSH error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python ssh_botnet_builder.py <hostname> <port> <username> <password> <command>")
        sys.exit(1)
    
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    username = sys.argv[3]
    password = sys.argv[4]
    command = sys.argv[5]

    ssh_command(hostname, port, username, password, command)
