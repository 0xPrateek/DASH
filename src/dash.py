import random,sys
import time,subprocess

def header():
    print("\n\t\tDaSh")
    print("\tFuckin logo lies here...!\n")

def display(status,message,verbose):
    if verbose:
        if status == 0:
            print(message)  # For success green color
        else:
            print(message) # For failure red color

def process_local(output):
    if "Running on" in output:
        address = output[15:37]
        print("LoL you just got the address :: "+address)
    elif "active" in output:
        status = "Running"
        print("It can be bad or good but the status is :: "+status)
    elif "127.0.0.1" in output:
        print("-> "+output[37:])


def local(port,path):
    print("Local is started ..\n")
    local_process = subprocess.Popen(['python3 ./local.py'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell = True)
    for line in iter(local_process.stdout.readline, b''):
        #print("-->"+str(line.rstrip()))
        process_local(str(line.rstrip()))
    print("\n-----------------------Local End ------------------------------\n")

def forward():
    import requests
    import json
    print("Forward starts......\n")
    ngrok = subprocess.Popen(['ngrok','http','5050'],stdout=subprocess.PIPE)
    time.sleep(3)
    tunnel_url = requests.get("http://localhost:4040/api/tunnels").text
    j = json.loads(tunnel_url)
    try:
        tunnel_url = j['tunnels'][0]['public_url']
        print(tunnel_url)
    except IndexError:
        print(j)
    print("\n-------------------- Forward end-------------------------------\n")


if __name__ == "__main__":

    # Prints logo on console.
    header()

    try:
        import sys,argparse
        parser = argparse.ArgumentParser()
    except:
        print("Moudle not found")

    parser.add_argument('-port',help="Port address",required = False,default = 5050)
    parser.add_argument('-path',help="Path to save file",required = False,default='/home/usr/Desktop/My')
    parser.add_argument('-v',help="Verbose",default=False, action='store_true',required = False)

    args = parser.parse_args()
    verbose = args.v

    import threading

    thread1 = threading.Thread(target=local,args=(args.port,args.path))
    thread2 = threading.Thread(target=forward)

    print("[+] Thread is starting")
    thread1.start()
    thread2.start()
    print("[~] You decide the correct ending. :<")
    thread1.join()
    thread2.join()
    print("Finaly fuck all this...")
