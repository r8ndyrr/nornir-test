# Welcome to my Nornir Lab Set up!
Hi! I've just started playing around with the **Nornir automation framework** and 
decided to create this repo. It took me a while to figure out what I needed to get up 
and running, so i'm putting everything here in case you're stuck like I was :).
## My Environment
To get things started, I'll explain my Lab environment so that you can see and compare 
with what you're using in the event that some stuff don't work.
## Server
- I'm using GNS3 server v2.1.21 hosted on google cloud to store my Cisco images. -
		- **I'm also using an Ubuntu Docker docker container (pulled from here 
--> ubuntu:latest)
		- Description: Ubuntu 18.04.3 LTS
		- Release: 18.04
		- Codename: bionic** -
		- GNS3 Nat Cloud for Internet access via DHCP -
		- A couple cisco 7200 routers 
Docker container needs to be updated and the following needs to be installed: 
- apt update 
- apt full-upgrade -y 
- apt-get install software-properties-common -y 
- add-apt-repository ppa:deadsnakes/ppa 
- apt-get install python-pip -y 
- apt-get install python3-pip -y 
- pip3 install nornir 
- apt-get install nano -y 
- apt-get install inetutils-ping -y 
- apt-get install iputils-ping -y 
- apt-get install traceroute

#### Change python3 and pip3 to be default by editing .bashrc file
- nano ~/.bashrc

#### Add the following lines at the top:
alias python=python3 alias pip=pip3

#### Save file, close and then run the command below:
- source ~/.bashrc You can now test your application by running the python command 
line as per below: -
		-	root@ubuntu-1:/home/nornir-test# python
			Python 3.6.8 (default, Oct 7 2019, 12:59:55)
			[GCC 8.3.0] on linux
			Type "help", "copyright", "credits" or "license" for more 
information.
			>>>
Python 3 is now default.

## Install Git
- apt-get install git -y Clone directory git clone 
https://github.com/r8ndyrr/nornir-test.git

## Client
- I'm using GNS3 v2.1.21 for my dev and config work.
