<h1 align="center">
  <br>
  <a href="https://github.com/0xprateek"><img src="https://i.imgur.com/EwsepV8.png" alt="DaSh"></a>
</h1>

<p align="center">  
  <a href="https://docs.python.org/3/download.html">
    <img src="https://img.shields.io/badge/Python-3.x-green.svg">
  </a>
  <a href="https://github.com/0xprateek/DaSh">
    <img src="https://img.shields.io/badge/Version-v1.0.0%20(beta)-blue.svg">
  </a>
  <a href="https://github.com/0xPrateek/DaSh/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-GPLv3-orange.svg">
  </a> 
  <a href="https://github.com/0xprateek/Dash">
    <img src="https://img.shields.io/badge/OS-Linux-black.svg">
    <img src="https://img.shields.io/badge/OS-Mac-Red.svg">
  </a>
  <a href="https://gitter.im/DASH_github/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge"><img src="https://badges.gitter.im/DASH_github/community.svg" alt="DaSh"></a>

</p>

## About [DASH](https://github.com/0xprateek/Dash)

DASH is a CLI tool for faster, safer and Smarter way to transfer files between two users.</br>

### Features 
- Share file of any size.
- Secured file transfer.
- A geeky way to transfer files.
- Direct transfer with a link (No need to share your email, whatsapp no. for transfer).
- Recieve file only when you want (Till DASH is running).

### Getting Started

#### How it works 

- The **Reciever** has to start DASH first on his device.
- It will give you a web link which you have to share with the person **Sender**.
- Then **Sender** need to open that web link in a web browser which has a file uploader and upload the file.
- At **Reciever** end, the file gets recived at Desktop(Default Location).

<h1 align="center">
<a href="https://github.com/0xprateek/DASH"><img src="https://github.com/0xPrateek/DASH/blob/master/Logo/DASH.gif" alt="DaSh"></a>
</h1>

#### Steps to setup :

1. `git clone https://github.com/0xprateek/dash`
2. `cd dash`
3. `pip install -r requirements.txt`
4. `sudo python3 ./configure.py`

#### Getting ngrok authtoken :

1. Go to `https://ngrok.com/`
2. Login/Signup to your account.
3. Copy your authentication token from `Auth` section.
4. Paste it in the terminal.

#### Starting DASH :

1. `cd dash/src`<br/>
2.  a)  **Using Command line arguments**<br/>
          `python3 ./dash.py -path /home/user/Documents`<br/>
          `python3 ./dash.py -port 7000`<br/>
    b)  **Without Command line arguments**<br/>
          `python3 ./dash.py`

  #### Usage :
     python3 ./dash.py [-h] [-port PORT] [-path PATH] [-v]

  ##### optional arguments:
     -h, --help  show this help message and exit
     -port PORT  Port address
     -path PATH  Path to save file
     -v          Verbose


### Contributing
Any and all contributions, issues, features and tips are welcome.

### License
**DASH** is licence under [GPL v3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html)
