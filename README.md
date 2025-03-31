Flight Control Tower

Este projeto implementa um simulador de controlador de voo, utilizando o padrão de projeto Observer para notificar mudanças no status dos voos.

Estrutura do Projeto

FlightControlTower: Classe principal que gerencia os voos e notifica observadores sobre mudanças de status.

Flight: Representa um voo com número, companhia aérea e status.

Observer: Interface para observadores que serão notificados sobre alterações.

FlightObserver: Implementação concreta do observer que imprime notificações no console.


Como Executar

1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).


2. Clone ou baixe este repositório.


3. Execute o arquivo principal:

python flight_controller.py



Exemplo de Uso

Após a execução, você verá uma saída semelhante a esta:

Flight AB123 (AirBlue) - Scheduled
Flight CD456 (SkyJet) - Scheduled
[NOTIFICATION] Flight AB123 status updated to Boarding
[NOTIFICATION] Flight CD456 status updated to Departed

Possíveis Melhorias

Implementação de uma interface gráfica para visualização dos voos.

Persistência dos dados em um banco de dados.

Simulação de eventos em tempo real.


Licença

Este projeto é de código aberto e pode ser modificado e distribuído conforme necessário.

