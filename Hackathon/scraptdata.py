import subprocess

# specify the path to the .pem file, the username, and the IP address
pem_path = "E:\Cloud\OneDrive\Coding\Python\Hackathon\2~UML+LDyA'PfR$4ErF78PM^yWMrl!MkqH#.txt"
username = "username"
ip_address = "ip.address"

# construct the command
command = f"ssh -i {pem_path} {username}@{ip_address}"

# execute the command
subprocess.run(command, shell=True)