#!/usr/bin/python3

ports = {
    20:"FTP",
    21:"FTP",
    22:"SSH",
    80:"HTTP",
    8080:"HTTP",
    443:"HTTPS",
    3306:"MySQL"
}

for key in ports.keys():
    print(f"Opend {key}")

while True:
    choose = input("Choose Port (Enter 'q' To Exit) : ")
    if choose == 'q':
        break

    if choose.isnumeric():
        choose = int(choose)
    else:
        print("Invalid Port!!")

    if choose in ports:
        print (f"{choose} : {ports[choose]}")
    else:
        print("[-] Port Not Found")