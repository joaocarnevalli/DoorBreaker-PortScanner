<p align="right"><strong>English</strong> | <a href="https://github.com/joaocarnevalli/DoorKnocker-PortScanner/blob/main/README-ptbr.md">Português</a></p>

# DoorBreaker - PortScanner
Checkpoint #5 de Coding for security da [FIAP](https://www.fiap.com.br)
> - Objective: Develop a portscannerin Python that makes it possible to scan one or more servers in search of TCP/UDP ports that are open. The program must present the search result on the screen and generate a report in a txt file, in addition to allowing the definition of the port range and identifying the type of protocol corresponding to the service based on the IANA services file.

- - - - - - - - - - - - - - - - - - -
## 
Contents
* [Author](#Author)
* [General information](#General)
* [Technologies](#Technologies)
* [Setup](#Setup)

- - - - - - - - - - - - - - - - - - -
## Author
* **João Pedro Zobolli Carnevalli**
    - [GitHub](https://github.com/joaocarnevalli) - [@joaocarnevalli](https://github.com/joaocarnevalli)
    - [Linkedin](https://www.linkedin.com/in/joaopedrozobollicarnevalli/)
    - [Twitch](https://www.twitch.tv/1joaolight)
    - **E-mail** -  **joaocarnevalli.sec@gmail.com**

- - - - - - - - - - - - - - - - - - -
## General
This program aims to scan a specific target, bringing open ports and their respective services!

- - - - - - - - - - - - - - - - - - -
## Technologies

This project was carried out in [Python 3.10](https://www.python.org), using the libraries [socket](https://docs.python.org/3/library/socket.html), [ipaddress](https://docs.python.org/3/library/ipaddress.html), [sys](https://docs.python.org/3/library/sys.html), [pyfiglet](https://pypi.org/project/pyfiglet/0.7/), [time](https://docs.python.org/3/library/time.html), [current.futures](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) and [datetime](https://docs.python.org/3/library/datetime.html)

- - - - - - - - - - - - - - - - - - -
## Setup
* 1 - install [Python](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe)
* 2 - install the library [scikit-learn](https://scikit-learn.org/stable/install.html#)
	- Open CMD
	- Type it `pip install -U scikit-learn` and run it
* 3 - install the library [ipaddress](https://pypi.org/project/ipaddress/)
	- Open CMD
	- Type it `pip install ipaddress` and run it
* 4 - install the library [pyfiglet](https://pypi.org/project/pyfiglet/0.7/)
    - Open CMD
    - Type it `pip install pyfiglet==0.7` and run it
* 5 - Download the `DoorKnocker0.1` and run it
