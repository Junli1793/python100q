#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""

"""

import socket
import paramiko
import yaml
import os

print()
print("==============Example 1==============")

# Connect to the remote server
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='10.79.59.19', username='lynn', password='Cisc0!23', port=22)

# Execute a command
stdin, stdout, stderr = ssh.exec_command('ls -l')

# Print the output of the command
print(stdout.read())

# Close the connection
ssh.close()

print()
print("==============Example 2==============")

class SshHelper(object):
    def __init__(self, host, port, ssh_username, ssh_password):
        self.host = host
        self.port = port
        self.ssh_username = ssh_username
        self.ssh_password = ssh_password

    def executeremotecommand(self, command):
        ssh = None
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(
                self.host, self.port, self.ssh_username, self.ssh_password, allow_agent=False, look_for_keys=False
            )

            stdin, stdout, stderr = client.exec_command(command)
            stdout = stdout.readlines()
            stderr = stderr.readlines()
            output = ""
            error = ""
            for line in stdout:
                output = output + line.strip()
            for errorline in stderr:
                error = error + errorline.strip()
            if output.strip() and error.strip():
                return (output, error)
            if output.strip() and not error.strip():
                return output
            elif error.strip() and not output.strip():
                return error
        except paramiko.SSHException as e:
            print("Password is invalid:", e)
        except socket.error as e:
            print("Socket connection failed:", e)
        finally:
            if ssh:
                ssh.close()

def read_cluster_yaml():
    with open("../testdata/cluster.yaml", "r") as json_file:
        config = yaml.safe_load(json_file)
        print(config)
        return config

config = read_cluster_yaml()
ssh_helper = SshHelper(
    host=config["cluster"]["hostname"],
    port="2222",
    ssh_username=config["cluster"]["ssh_user"],
    ssh_password=config["cluster"]["ssh_pass"],
)

# p = os.popen("ssh-keygen -R 10.79.59.25")
# print(p.read())
# p.close()

get_qa_pods = ssh_helper.executeremotecommand("kubectl get pods -n qa-assurance-common").split("qa-assurance-common")
inter_list = [each for each in get_qa_pods if "Running" in each]
full_list = []
for every in inter_list:
    full_list = full_list + every.split("  ")
list_of_pods = ["qa-assurance-common" + each for each in full_list if "-" in each]
print(list_of_pods)
