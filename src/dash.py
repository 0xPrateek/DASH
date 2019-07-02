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
        print("[1/2] Local server is ready...")
    else:
        print("~~> ",output)
    '''
    elif '"GET / HTTP/1.1" 200 ' in output:
        print("[~] Someone opened your Uploader... :)")

    else:
        http_code = output[-5:-2]
        if http_code == 204:
            print("\n------- Congrats ------")
            print("File uploaded successfully :< ")
    '''

def local(port,path):
    local_process = subprocess.Popen(['python3 ./local.py'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell = True)
    for line in iter(local_process.stdout.readline, b''):
        process_local(str(line.decode('utf-8')))

# packet_write_wait: Connection to 159.89.214.31 port 22: Broken pipe

def forward():
    serveo = subprocess.Popen(['ssh','-R','80:localhost:5050','serveo.net'],stdout=subprocess.PIPE)
    line = serveo.stdout.readline()
    print(str(line.decode('utf-8')),end="")

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

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
