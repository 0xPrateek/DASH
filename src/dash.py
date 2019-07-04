from subprocess import Popen,PIPE
import threading
import os

def process_display(type,message):

    if type == 0:
        print("[OK] ~",message)
    elif type == 1:
        print("[NO] ~",message)
    elif type == 2:
        print("[!] ~",message)


def local():

    local_process = Popen(['python3 ./local.py'],stderr = PIPE,stdout = PIPE,shell = True)
    for output in local_process.stderr:
        output=output.decode('utf-8')
        if "Traceback" in output:
            process_display(1,"Error due to usable port.")

        elif "Running" in output:
            process_display(0,"[1/2] Local Server is started.")

        elif "127.0.0.1" in output:
            http_code = int(output[-6:-2])
            if http_code == 200:
                process_display(0,"Someone Opened the page.")
            elif http_code == 204:
                process_display(0,"Upload Completed.")

def forward():
    forward_process = Popen(['ssh -R 80:localhost:5050 serveo.net'],stdout = PIPE, stderr = PIPE,shell = True)
    print(forward_process.stderr.readline())
    print("Koi scene hai kya  .. :/")
    for output in forward_process.stdout:
        print(output.decode('utf-8'))

if __name__ == "__main__":
    print("\t\t  DASh \n\t Fucking logo lies here\n")


    thread1 = threading.Thread(target=local)
    thread2 = threading.Thread(target=forward)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
