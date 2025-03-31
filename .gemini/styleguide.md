# Guia de Estilo para o Projeto Flight Control Tower

Este guia de estilo define as diretrizes para manter a consistência, legibilidade e qualidade do código no projeto Flight Control Tower.

## 1. Estrutura do Código

- Utilize a convenção de nomenclatura PEP8 para classes, métodos e variáveis.
- Organize as importações seguindo a ordem:
  1. Bibliotecas padrão do Python
  2. Bibliotecas de terceiros
  3. Módulos internos do projeto
- Separe blocos lógicos do código com quebras de linha para melhor legibilidade.

## 2. Nomenclatura

- **Classes:** Utilize `CamelCase` (exemplo: `FlightControlTower`).
- **Métodos e variáveis:** Utilize `snake_case` (exemplo: `register_flight`).
- **Constantes:** Utilize `UPPER_CASE` (exemplo: `MAX_FLIGHTS = 100`).

## 3. Boas Práticas

- Escreva docstrings para todas as classes e métodos seguindo o formato Google Docstring.
- Evite números mágicos. Utilize constantes nomeadas quando necessário.
- Prefira funções puras e métodos de instância quando apropriado.
- Utilize anotações de tipo (`type hints`) para facilitar a compreensão do código.

## 4. Tratamento de Erros

- Utilize `try-except` para capturar e tratar exceções de forma adequada.
- Sempre forneça mensagens de erro claras e úteis.
- Evite capturar exceções genéricas (`except Exception:`), especificando o tipo correto de erro.

## 5. Padrão de Projeto

- O projeto utiliza o padrão *Observer* para gerenciar notificações sobre mudanças de status dos voos.
- Ao adicionar novas funcionalidades, siga princípios de orientação a objetos como encapsulamento e responsabilidade única.

## 6. Formatação

- Utilize 4 espaços para indentação (não utilize tabs).
- Limite as linhas a 79 caracteres sempre que possível.
- Adicione quebras de linha entre funções e classes para melhorar a legibilidade.

## 7. Testes

- Todos os módulos devem ser acompanhados de testes unitários.
- Utilize `pytest` como framework de testes.
- Nomeie os arquivos de teste seguindo o padrão `test_<nome_do_modulo>.py`.

## 8. Versionamento

- Siga a convenção *Semantic Versioning* (`MAJOR.MINOR.PATCH`).
- As alterações significativas devem ser documentadas no `CHANGELOG.md`.

## 9. Comentários

- Utilize comentários para explicar o “porquê” do código, não apenas o “como”.
- Evite comentários óbvios ou redundantes.
- Prefira docstrings para documentação formal e comentários inline para explicações específicas.
