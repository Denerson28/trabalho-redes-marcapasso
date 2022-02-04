# Trabalho de Redes II: 2021.2

### Professor: Flávio Seixas
### Alunos: Denerson Eduardo, Luana Vidal e Mairon Azevedo

#### Motivação
Este trabalho consiste em uma aplicação onde simula o *Marca-passo inteligente*, ou seja, um dispositivo conectado a um servidor através do protocolo TCP/IP. Seriam registrados os batimentos do paciente e em caso de qualquer tipo de irregularidade, o servidor emitiria um alerta ao doutor cadastrado na plataforma.

#### Bibliotecas utilizadas
- Utilizamos a biblioteca *socket* para a criação do servidor e estabelecimento do protocolo;
- Utilizamos a biblioteca *threading* para a implementação de threads envolvendo o servidor, permitindo a conexão simultânea de mais de um cliente;
- Utilizamos a biblioteca *random* para gerar automaticamente valores aleatórios, tanto de batimentos como de pacientes;

#### Pré-requisitos
Neste projeto, como utilizamos apenas bibliotecas nativas do python, é necessária apenas a instalação do mesmo :)
- Python Download (https://www.python.org/downloads/release/python-3102/)
- Caso você use linux, basta executar o comando ```sudo apt-get install python```

#### Executando o projeto
*(É de suma importância que os passos sejam seguidos na ordem da documentação)*
- Não é necessária a instalação de nenhuma biblioteca adicional para a execução. 
- Abra o terminal na pasta onde o projeto se encontra e digite ```python server.py```, feito isso, o servidor estará rodando.
- Abra outro terminal e execute o comando ```python doctor.py```.
- Por fim abra quantos terminais desejar e execute em cada um deles o comando ```python client.py```

