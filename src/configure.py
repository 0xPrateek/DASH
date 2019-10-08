try:
    import platform,subprocess,colors
except:
    print(1,1,"Module not found\n    Make sure you have installed 'requirements.txt' and configured DASH")
    import sys
    sys.exit(0)

def header():
    print('\n\t\t{}-{} DASH {}Configration -{}\n'.format(colors.red,colors.white,colors.red,colors.white))
    print('    [ Only if Ngrok is not configured on your Device. ]{}\n'.format(colors.red,colors.white,colors.white))


if __name__ == '__main__':

    header()

    os = platform.system()

    if os == 'Linux' or 'Darwin':

        ngrok_download = {'Linux':'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip',
                          'Darwin':'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip'}

        ngrok = subprocess.Popen(['wget {}'.format(ngrok_download[os])],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell = True)
        for output in ngrok.stdout:
            if "OK" in output.decode('utf-8'):
                print("{}[1/3]{} Download Started".format(colors.green,colors.white))
            if "%" in output.decode('utf-8') and len(output.decode('utf-8').split(" ")[-3])>0:
                print("   Downloaded..... : ",colors.green,output.decode('utf-8').split(" ")[-3],colors.white)

        print("\n{}[2/3]{} Unziping & moving ngrok to bin".format(colors.green,colors.white))
        unzip = subprocess.Popen(['unzip {}'.format(ngrok_download[os].split('/')[-1])],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell = True)
        for output in unzip.stdout:
            print("  ",output.decode('utf-8'))
            break

        move = subprocess.Popen(['mv ngrok /usr/local/bin'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell = True)

        print("\n{}[3/3]{} Genrating Authentication token :: \n   1- Go to https://ngrok.com \n   2- Login to your account. \n   3- Copy your Authentication Token (ex: 3YtQYT4je1Uj5zAnTJE4B_PzABTaXWowsWgpisdfed) and Paste here.".format(colors.green,colors.white))
        token = input("\nEnter Ngrok Authentication token : {}".format(colors.green))


        ng_auth = subprocess.Popen(['ngrok authtoken {}'.format(token)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell = True)
        for output in ng_auth.stdout:
            print(colors.white," ",output.decode('utf-8'))

        print("-",colors.blue,"DASH is successfully configured.")

    elif os == 'Windows':

        print("Sorry.! we don't do that here xD..!")
