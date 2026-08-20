port_list = [21, 22, 80, 443, 8080, 80]
port_set = set(port_list)
print(port_set)
server_info = ("192.168.1.1", 8080)
print(f"{server_info[0], {server_info[1]}}")
hasil_scan = {"target" : (server_info[0]), "status" : "up", "open_ports" : [22, 88],  "total_ports_scanned" : len(port_set)}
for key, value in hasil_scan.items():
    print(f"{key} : {value}")
