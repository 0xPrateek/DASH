import time,subprocess,os

def header():
    print("\n\t\tDaSh")
    print("\tFuckin logo lies here...!\n")


def process_display(type,message):
    if type == 0:
        print("[OK] ~",message)
    elif type == 1:
        print("[NO] ~",message)
    elif type == 2:
        print("[!] ~",message)

def local(port,path):

    local_process = subprocess.Popen(['python3 ./local.py -port {} -path {}'.format(port,path)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell = True)

    for output in local_process.stdout:
        output=output.decode('utf-8')
        if "Traceback" in output:
            process_display(1,"Error due to usable port.")
        elif "Running" in output:
            process_display(0,"[1/2] Local Server is started.")
        elif "ClientIP" in output:
            ClientIP = output[10:]
        elif "127.0.0.1" in output:
            out = str(output).split(' ')
            if out[6] == '/':
                process_display(0,"Someone Opened the page at ")
            elif out[-2] == '204':
                process_display(0,"Upload Completed by ")

def forward(port):
    import requests
    import json

    ngrok = subprocess.Popen(['ngrok','http',str(port)],stdout=subprocess.PIPE)
    process_display(0,"[2/2] Public Server is started.")
    time.sleep(3)
    tunnel_url = requests.get("http://localhost:4040/api/tunnels").text
    j = json.loads(tunnel_url)
    try:
        tunnel_url = j['tunnels'][0]['public_url']
        process_display(0,"The link for the page is : "+tunnel_url)
    except IndexError:
        process_display(2,"Rechecking the URLs in 4s :/ ")
        time.sleep(4)
        tunnel_url = requests.get("http://localhost:4040/api/tunnels").text
        j = json.loads(tunnel_url)
        tunnel_url = j['tunnels'][0]['public_url']
        process_display(0,"The link for the page is : "+tunnel_url)

    print("\n------------------------------- _^_ -------------------------------\n")


if __name__ == "__main__":

    # Prints logo on console.
    header()

    try:
        import sys,argparse
        parser = argparse.ArgumentParser()
    except:
        print("Moudle not found")

    parser.add_argument('-port',help="Port address",required = False,default = 5050)
    parser.add_argument('-path',help="Path to save file",required = False,default=os.path.expanduser('~')+'/Desktop')

    args = parser.parse_args()

    import threading

    thread1 = threading.Thread(target=local,args=(args.port,args.path))
    thread2 = threading.Thread(target=forward,args=(args.port,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
