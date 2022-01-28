# Trabalho de Redes: 2021.2

### Professor: Flávio Seixas
### Alunos: Denerson Eduardo, Luana Vidal e Mairon Azevedo

#### Motivação
Este trabalho consiste em uma aplicação onde simula o *Marca-passo inteligente*, ou seja, um dispositivo conectado a um servidor através do protocolo TCP/IP. Seriam registrados os batimentos do paciente e em caso de qualquer tipo de irregularidade, o servidor emitiria um alerta ao doutor cadastrado na plataforma.

#### Bibliotecas utilizadas
- Utilizamos a biblioteca *socket* para a criação do servidor e estabelecimento do protocolo;
- Utilizamos a biblioteca *threading* para a implementação de threads envolvendo o servidor, permitindo a conexão simultânea de mais de um cliente;
- Utilizamos a biblioteca *random* para gerar automaticamente valores aleatórios, tanto de batimentos como de pacientes;

