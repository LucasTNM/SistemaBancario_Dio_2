# Sistema Bancário - DIO

Este é um projeto simples de um sistema bancário desenvolvido em Python, como parte do bootcamp Santander na Digital Innovation One (DIO).

## Funcionalidades

- **Depósito:** Permite ao usuário depositar valores positivos em sua conta.
- **Saque:** Permite ao usuário realizar saques, respeitando o limite de valor por saque e o número máximo de saques diários.
- **Extrato:** Exibe todas as movimentações realizadas e o saldo atual da conta.
- **Criar Usuário:** Permite cadastrar um novo usuário no sistema, informando CPF, nome, data de nascimento e endereço.
- **Criar Conta:** Permite criar uma conta bancária vinculada a um usuário já cadastrado.
- **Sair:** Encerra o programa.

## Regras do Sistema

- O usuário pode realizar até 3 saques por sessão.
- O valor máximo por saque é de R$ 500,00.
- Não é permitido depositar valores negativos.
- O extrato mostra todas as operações realizadas.
- Só é possível criar uma conta para um usuário já cadastrado.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou baixe os arquivos.
3. No terminal, navegue até a pasta `SistemaBancario_Dio_2`.
4. Execute o arquivo `app.py`:

   ```sh
   python app.py
   ```

## Observações

- O projeto utiliza apenas recursos básicos da linguagem Python, sem dependências externas.
- Projeto desenvolvido para fins educacionais no bootcamp Santander - DIO.