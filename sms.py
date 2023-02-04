import requests
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style

class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"
            
    
         #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")
