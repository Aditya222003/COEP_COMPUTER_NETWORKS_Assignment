import ipaddress
 
def calculate_subnet_info(ip_address, subnet_mask):
    network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
    num_subnets = 2 ** (32 - subnet_mask)
    num_hosts_per_subnet = 2 ** (32 - subnet_mask) - 2
    network_id = network.network_address
    broadcast_address = network.broadcast_address
    valid_host_range = (network.network_address + 1, network.broadcast_address - 1)

    return num_subnets, num_hosts_per_subnet, network_id, broadcast_address, valid_host_range

ip_class = input("Enter the IP class (A, B, C): ").upper()

if ip_class == "A":
    subnet_mask = 8
    ip_range = "0.0.0.0 - 127.255.255.255"
elif ip_class == "B":
    subnet_mask = 16
    ip_range = "128.0.0.0 - 191.255.255.255"
elif ip_class == "C":
    subnet_mask = 24
    ip_range = "192.0.0.0 - 223.255.255.255"
else:
    print("Invalid IP class. Please enter A, B, or C.")
    exit()

print(f"IP Range for Class {ip_class}: {ip_range}")
print(f"Subnet Mask for Class {ip_class}: /{subnet_mask}")

ip_address = input("Enter an IP address from the selected class: ")

num_subnets, num_hosts_per_subnet, network_id, broadcast_address, valid_host_range = calculate_subnet_info(ip_address, subnet_mask)

print(f"Number of Subnets: {num_subnets}")
print(f"Number of Hosts per Subnet: {num_hosts_per_subnet}")
print(f"Network ID: {network_id}")
print(f"Broadcast Address: {broadcast_address}")
print(f"Valid Host Range: {valid_host_range[0]} - {valid_host_range[1]}")