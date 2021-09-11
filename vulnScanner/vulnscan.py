import portScanner

target_ip = input("[+] *Enter Target Ip To Scan Vulnerable Ports: ")
port_number = int(input("[+] *Enter The Number Of Ports You Want To Scan: "))
vuln_file = input("[+] *Enter Path To File With Vulnerable Software: ")

target = portScanner.PortScan(target_ip, port_number)
target.scan()

with open(vuln_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] Vulnerable Banner: "' + banner +
                      '" On Port: ' + str(target.open_ports[count]))
        count += 1
