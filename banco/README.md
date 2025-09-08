# Sistema Bancário v1 - DESAFIO DIO NTT Data

## Introdução

Este documento descreve os requisitos para a primeira versão do novo sistema bancário. O objetivo é criar uma aplicação simples em Python para modernizar as operações do banco Wxz, começando com as funcionalidades essenciais de depósito, saque e extrato para um único usuário.

## Recursos

- Python 3

## Requisitos Funcionais (RF)

Os Requisitos Funcionais descrevem o que o sistema deve fazer.

| ID | Descrição |
| :--- | :--- |
| **RF01** | O sistema deve permitir ao usuário depositar valores positivos em sua conta. |
| **RF02** | O sistema deve registrar todos os depósitos realizados para que possam ser exibidos no extrato. |
| **RF03** | O sistema deve permitir ao usuário sacar valores da conta, desde que o saldo seja suficiente. |
| **RF04** | O sistema deve registrar todos os saques realizados para que possam ser exibidos no extrato. |
| **RF05** | O sistema deve impedir saques quando o saldo em conta for insuficiente e exibir uma mensagem de erro informativa. |
| **RF06** | O sistema deve limitar a quantidade de saques a um máximo de 3 (três) por dia. |
| **RF07** | O sistema deve impor um limite máximo de R$ 500,00 por operação de saque. |
| **RF08** | O sistema deve fornecer uma opção de extrato que liste todas as movimentações (depósitos e saques) realizadas. |
| **RF09** | O extrato deve exibir o saldo atual da conta ao final da listagem de movimentações. |
| **RF10** | Caso não existam movimentações, o extrato deve exibir a mensagem: "Não foram realizadas movimentações.". |
| **RF11** | Todos os valores monetários (depósitos, saques, saldo) devem ser exibidos no formato `R$ xxx.xx` (ex: `R$ 1500.45`). |

## Requisitos Não Funcionais (RNF)

Os Requisitos Não Funcionais descrevem como o sistema deve operar, definindo suas qualidades e restrições.

| ID | Descrição |
| :--- | :--- |
| **RNF01** | O sistema deve ser desenvolvido utilizando a linguagem de programação Python. |
| **RNF02** | A primeira versão do sistema deve ser projetada para um único usuário, sem necessidade de autenticação ou identificação de agência e conta. |
| **RNF03** | O sistema deve ser operado via interface de console (terminal). |
| **RNF04** | A interação com o usuário deve ser clara e objetiva, fornecendo mensagens informativas sobre o sucesso ou falha das operações. |
| **RNF05** | Os dados das transações (saldo, lista de depósitos e saques) devem ser mantidos em memória durante a execução do programa. |

## Requisitos para Teste

Os testes a seguir devem ser executados para garantir que os requisitos funcionais e as regras de negócio foram implementados corretamente.

### Testes de Depósito

| Cenário de Teste | Passos | Resultado Esperado |
| :--- | :--- | :--- |
| **Depósito Válido** | 1. Iniciar o sistema. 2. Realizar um depósito de R$ 200,00. | O saldo da conta deve ser atualizado para R$ 200,00. A transação deve ser registrada no extrato. |
| **Depósito com Valor Decimal** | 1. Iniciar o sistema com saldo de R$ 50,00. 2. Realizar um depósito de R$ 75,50. | O saldo da conta deve ser atualizado para R$ 125,50. |
| **Depósito com Valor Zero** | 1. Tentar realizar um depósito de R$ 0,00. | O sistema deve recusar a operação e informar que apenas valores positivos são permitidos. O saldo não deve ser alterado. |
| **Depósito com Valor Negativo**| 1. Tentar realizar um depósito de R$ -100,00. | O sistema deve recusar a operação e informar que apenas valores positivos são permitidos. O saldo não deve ser alterado. |

### Testes de Saque

| Cenário de Teste | Passos | Resultado Esperado |
| :--- | :--- | :--- |
| **Saque Válido** | 1. Iniciar com saldo de R$ 1000,00.\<br\>2. Realizar um saque de R$ 300,00. | O saldo deve ser atualizado para R$ 700,00. A transação deve ser registrada no extrato. |
| **Saque Sem Saldo** | 1. Iniciar com saldo de R$ 100,00.\<br\>2. Tentar sacar R$ 200,00. | O sistema deve exibir a mensagem "Não será possível sacar o dinheiro por falta de saldo." e o saldo deve permanecer R$ 100,00. |
| **Saque Acima do Limite por Operação** | 1. Iniciar com saldo de R$ 1000,00.\<br\>2. Tentar sacar R$ 500,01. | O sistema deve recusar a operação e informar que o limite por saque é de R$ 500,00. O saldo não deve ser alterado. |
| **Saque Excedendo Limite Diário** | 1. Iniciar com saldo de R$ 2000,00.\<br\>2. Realizar 3 saques de R$ 100,00 cada.\<br\>3. Tentar realizar um 4º saque. | Os 3 primeiros saques devem ser bem-sucedidos. O 4º saque deve ser recusado com uma mensagem informando que o limite diário foi atingido. |

### Testes de Extrato

| Cenário de Teste | Passos | Resultado Esperado |
| :--- | :--- | :--- |
| **Extrato com Movimentações** | 1. Realizar um depósito de R$ 1000,00.\<br\>2. Realizar um saque de R$ 250,50.\<br\>3. Solicitar o extrato. | O extrato deve listar um depósito de `R$ 1000.00` e um saque de `R$ 250.50`. O saldo final exibido deve ser `R$ 749.50`. |
| **Extrato Vazio** | 1. Iniciar o sistema.\<br\>2. Solicitar o extrato sem ter feito nenhuma operação. | O sistema deve exibir a mensagem: "Não foram realizadas movimentações.". |
| **Formatação Monetária** | 1. Realizar depósitos e saques com valores inteiros e decimais.\<br\>2. Solicitar o extrato. | Todos os valores no extrato (depósitos, saques e saldo) devem estar no formato `R$ xxx.xx`. |
