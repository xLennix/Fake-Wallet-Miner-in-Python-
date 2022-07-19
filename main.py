import random
import string
import colorama
import os
import time
from keyauth import api
import sys
from colorama import Fore, Style, Back
import platform
import hashlib
from time import sleep
from datetime import datetime


os.system("cls")
os.system("title Python Example")
print("Initializing")
def getchecksum():
	path = os.path.basename(__file__)
	if not os.path.exists(path):
		path = path[:-2] + "exe"
	md5_hash = hashlib.md5()
	a_file = open(path,"rb")
	content = a_file.read()
	md5_hash.update(content)
	digest = md5_hash.hexdigest()
	return digest

keyauthapp = api(
	name = "",
	ownerid = "",
	secret = "",
	version = "1.0",
	hash_to_check = getchecksum()
)
print(f"Current Session Validation Status: {keyauthapp.check()}")
print(f"Blacklisted? : {keyauthapp.checkblacklist()}") # check if blacklisted, you can edit this and make it exit the program if blacklisted
print (colorama.Fore.GREEN +"""
1.Login
2.Register
3.Upgrade
4.License Key Only
""")
ans=input("Select Option: ") 
if ans=="1": 
	user = input('Provide username: ')
	password = input('Provide password: ')
	keyauthapp.login(user,password)
elif ans=="2":
	user = input('Provide username: ')
	password = input('Provide password: ')
	license = input('Provide License: ')
	keyauthapp.register(user,password,license) 
elif ans=="3":
	user = input('Provide username: ')
	license = input('Provide License: ')
	keyauthapp.upgrade(user,license)
    
elif ans=="4":
	key = input('Enter your license: ')
	keyauthapp.license(key)
else:
	print("\nNot Valid Option") 
	sys.exit()


#region Extra Functions

#* Download Files form the server to your computer using the download function in the api class
#bytes = keyauthapp.download("FILEID")
#f = open("example.exe", "wb")
#f.write(bytes)
#f.close()


#* Set up user variable
#keyauthapp.setvar("varName", "varValue")

#* Get user variable and print it
#data = keyauthapp.getvar("varName")
#print(data)

#* Get normal variable and print it
#data = keyauthapp.var("varName")
#print(data)

#* Log message to the server and then to your webhook what is set on app settings
#keyauthapp.log("Message")

#* Get if the user pc have been blacklisted
#print(f"Blacklisted? : {keyauthapp.checkblacklist()}")

#* See if the current session is validated
#print(f"Session Validated?: {keyauthapp.check()}")


#* example to send normal request with no POST data
#data = keyauthapp.webhook("WebhookID", "?type=resetuser&user=username")

#endregion

print("\nUser data: ") 
print("Username: " + keyauthapp.user_data.username)
print("IP address: " + keyauthapp.user_data.ip)
print("Hardware-Id: " + keyauthapp.user_data.hwid)
#print("Subcription: " + keyauthapp.user_data.subscription) ## Print Subscription "ONE" name

subs = keyauthapp.user_data.subscriptions ## Get all Subscription names, expiry, and timeleft
for i in range(len(subs)):
  sub = subs[i]["subscription"] # Subscription from every Sub
  expiry = datetime.utcfromtimestamp(int(subs[i]["expiry"])).strftime('%Y-%m-%d %H:%M:%S') ## Expiry date from every Sub
  timeleft = subs[i]["timeleft"] ## Timeleft from every Sub

  print(f"[{i + 1} / {len(subs)}] | Subscription: {sub} - Expiry: {expiry} - Timeleft: {timeleft}")


print("Created at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S'))
print("Last login at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S'))
print("Expires at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))
print(f"Current Session Validation Status: {keyauthapp.check()}")
print("Exiting in 10 secs....")
sleep(10)
sys.exit(0)






colorama.init()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
os.system('cls')
print(f"""
{Fore.LIGHTGREEN_EX}logo here{Fore.CYAN}logo here
{Fore.LIGHTGREEN_EX}logo here{Fore.CYAN}logo here    {Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Devved By @xLennix On Github{Fore.LIGHTGREEN_EX}
{Fore.LIGHTGREEN_EX}logo here{Fore.CYAN}logo here
{Fore.LIGHTGREEN_EX}logo here{Fore.CYAN}logo here
            [ Random, Wallet Mining Service. ]
        {Fore.WHITE}[ {Fore.CYAN}1 {Fore.WHITE}] : {Fore.CYAN}Start BTC Wallet Mining
        {Fore.WHITE}[ {Fore.CYAN}2{Fore.WHITE} ] : {Fore.CYAN}Quit
""")

print(f'{Fore.WHITE}[ {Fore.RED}?{Fore.WHITE} ] : {Fore.GREEN}', end="")
option = input('')
if option == '1':
    print(f'{Fore.WHITE}[ {Fore.RED}Bitcoin Wallet Address{Fore.WHITE} ] : {Fore.GREEN}', end="")
    wallet = input('')
    os.system('cls')

if option == '2':
    print(f'{Fore.RED} Closing CLAWZ Bitcoin Wallet Miner..')
    exit(0)

print(f'{Fore.WHITE}[{Fore.RED}Confirm This Is YOUR Bitcoin Wallet (Y/N) {Fore.WHITE}] :{Fore.GREEN} [{wallet}]', end="\n")
print(f'{Fore.WHITE}[ {Fore.RED}?{Fore.WHITE} ] : {Fore.GREEN}', end="")
confirmation = input('')
if confirmation == 'Y':
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet.')
    time.sleep(0.5)
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet..')
    time.sleep(0.5)
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet...')
    time.sleep(0.5)
    os.system('cls')
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet.')
    time.sleep(0.5)
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet..')
    time.sleep(0.5)
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet...')
    time.sleep(0.5)
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.GREEN}Successfull, Wallet Address Is VALID!')
    time.sleep(1.5)
    os.system('cls')
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.GREEN}Wallet Mining Begins In 3 Seconds.')
    time.sleep(3)
else:
    print(f'{Fore.WHITE} [{Fore.RED}ERROR{Fore.WHITE}] {Fore.GREEN}Please use capital Y, or N. If still not working, contact SUPPORT or check your Wallet Address. [Quiting]')
    time.sleep(1.2)

for line in range(3000):
    result = print(f'{Fore.WHITE}({Fore.GREEN}BTC : {Fore.RED}0{Fore.WHITE}) {Fore.WHITE}[ {Fore.RED}!{Fore.WHITE} ] : {Fore.LIGHTCYAN_EX}1 {Fore.GREEN}', "".join(random.choice(letters) for i in range(42)))
    print(result)
print(f'{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] : {Fore.LIGHTMAGENTA_EX} Found Hit! Press ENTER To Continue.\n')
input()
btc_amount = "1.00 BTC"
btc_usd_amount = "37,869.60 USD"
print(f'{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] : {Fore.RED}HIT DETAILS:\n BTC ADDRESS: {Fore.LIGHTCYAN_EX} 1 {Fore.LIGHTGREEN_EX}', ''.join(random.choice(letters) for i in range(42)), f'\n {Fore.RED}BTC AMOUNT: {Fore.CYAN}{btc_amount} {Fore.WHITE}, {Fore.WHITE}( {Fore.GREEN}{btc_usd_amount} {Fore.LIGHTYELLOW_EX}${Fore.WHITE} )\n{Fore.LIGHTRED_EX} Press {Fore.GREEN}Enter{Fore.LIGHTRED_EX} To Transact The Funds Into YOUR, BTC Wallet.')
input()
print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Transferring Funds Into BTC Address: [{Fore.RED}{wallet}{Fore.LIGHTMAGENTA_EX}]..')
time.sleep(1)
print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.GREEN}SUCCESFULLY{Fore.WHITE} TRANSFERRED {Fore.RED}{btc_amount}{Fore.WHITE} , ( {Fore.LIGHTMAGENTA_EX}{btc_usd_amount} {Fore.LIGHTYELLOW_EX}$ {Fore.WHITE}) INTO BTC ADDRESS {Fore.WHITE}[{Fore.RED}{wallet}{Fore.WHITE}]!')
print(f'{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Closing CLAWZ Wallet Miner.')
exit(0)
