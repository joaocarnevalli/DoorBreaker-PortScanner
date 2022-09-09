# DoorKnocker - PortScanner
Checkpoint #5 de Coding for security da [FIAP](https://www.fiap.com.br)
> - Objetivo: Desenvolver  um portscannerem  Python que possibilite  escanear  um ou  mais  servidores  em  busca  de  portas  TCP/UDP que  estejam  abertas.  O programa deve apresentar  o  resultadoda  pesquisa  na tela  e  gerar  um report em arquivo txt, além de possibilitar a definição do range de portas e identificar o tipo  de  protocolo  correspondente  ao  serviço  com  base no  arquivo  services  do IANA.

- - - - - - - - - - - - - - - - - - -
## Conteúdo
* [Autor](#Autor)
* [Informações Gerais](#Geral)
* [Tecnologias](#tecnologias)
* [Configuração](#setup)

- - - - - - - - - - - - - - - - - - -
## Autor
* **João Pedro Zobolli Carnevalli**
    - [GitHub](https://github.com/joaocarnevalli) - [@joaocarnevalli](https://github.com/joaocarnevalli)
    - [Linkedin](https://www.linkedin.com/in/joaopedrozobollicarnevalli/)
    - [Twitch](https://www.twitch.tv/1joaolight)
    - **E-mail** -  **joaocarnevalli.sec@gmail.com**

- - - - - - - - - - - - - - - - - - -
## Geral
Este programa visa fazer um scan em determinado alvo, trazendo as portas abertas e seus respectivos serviços!

- - - - - - - - - - - - - - - - - - -
## Tecnologias
Este projeto foi realizado em [Python 3.10](https://www.python.org), utilizando as bibliotecas [socket](https://docs.python.org/3/library/socket.html), [ipaddress](https://docs.python.org/3/library/ipaddress.html), [sys](https://docs.python.org/3/library/sys.html), [pyfiglet](https://pypi.org/project/pyfiglet/0.7/), [time](https://docs.python.org/3/library/time.html), [current.futures](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) e [datetime](https://docs.python.org/3/library/datetime.html)