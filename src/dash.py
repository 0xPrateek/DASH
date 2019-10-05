import time,subprocess,os,colors

def header():
    print('\n\t\t{}-{} DASH {}-{}\n'.format(colors.red,colors.white,colors.red,colors.white))


def process_display(verbose,type,message):
    if args.v is False:
        verbose = 0

    if type == 0 and verbose == 0:
        colors.success(message)
    elif type == 1 and verbose == 0:
        colors.error(message)
    elif type == 2 and verbose == 0:
        colors.process(message)
    elif type == 3 and verbose == 0:
        colors.info(message)


def local(port,path):
    local_process = subprocess.Popen(['python3 ./local.py -port {} -path {}'.format(port,path)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell = True)

    for output in local_process.stdout:
        output=output.decode('utf-8')
        if "Traceback" in output:
            process_display(0,1,"Error due to usable port")
            process_display(0,3,"Restarting with new port")
            local(int(port)+1,path)
        elif "Running" in output:
            process_display(1,0,"[2/2] Local Server is started.")
            print("\n")
        elif "ClientIP" in output:
            ClientIP = output[10:]
        elif "127.0.0.1" in output:
            out = str(output).split(' ')
            if out[6] == '/':
                process_display(0,0,"Someone Opened the page")
            elif out[-2] == '204':
                process_display(0,0,"Upload Completed")


def forward(port):
    import requests
    import json

    ngrok = subprocess.Popen(['ngrok','http',str(port)],stdout=subprocess.PIPE)
    process_display(1,0,"[1/2] Public Server is started.")
    time.sleep(3)
    tunnel_url = requests.get("http://localhost:4040/api/tunnels").text
    j = json.loads(tunnel_url)
    try:
        tunnel_url = j['tunnels'][0]['public_url']
        process_display(0,0,"The link for the page is : "+tunnel_url)
    except IndexError:
        process_display(1,2,"Rechecking the URLs in 4s :/ ")
        time.sleep(4)
        tunnel_url = requests.get("http://localhost:4040/api/tunnels").text
        j = json.loads(tunnel_url)
        tunnel_url = j['tunnels'][0]['public_url']
        process_display(0,0,"The link for the page is : "+tunnel_url)

    print("\n{}-------------------------------{} _^_ {}-------------------------------{}\n".format(colors.white,colors.red,colors.white,colors.red))


if __name__ == "__main__":

    try:

        header()  # Prints logo on console. P.S : I'm not a designer :/

        try:
            import sys,argparse
            parser = argparse.ArgumentParser()
        except:
            process_display(1,1,"Moudle not found")

        parser.add_argument('-port',help="Port address",required = False,default = 5050)
        parser.add_argument('-path',help="Path to save file",required = False,default=os.path.expanduser('~')+'/Desktop')
        parser.add_argument('-v',help="Verbose",default=False, action='store_true',required = False)

        args = parser.parse_args()

        import threading

        thread1 = threading.Thread(target=local,args=(args.port,args.path))
        thread2 = threading.Thread(target=forward,args=(args.port,))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()
    except:
        print("\nYou're Great..!\nThanks for using :)")
        sys.exit(0)
