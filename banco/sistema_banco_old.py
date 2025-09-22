def main():
    """
    Função principal que executa o sistema bancário.
    """
    menu = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """

    # Variáveis de estado da conta
    saldo = 0.0
    limite_saque_valor = 500.0
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES_DIARIOS = 3

    print("\nBem-vindo ao nosso banco!")

    while True:
        opcao = input(menu).lower()

        # --- Operação de Depósito ---
        if opcao == 'd':
            print("\n--- Depósito ---")
            try:
                valor_deposito = float(
                    input("Informe o valor do depósito: R$ "))

                if valor_deposito > 0:
                    saldo += valor_deposito
                    extrato += f"Depósito:\t\tR$ {valor_deposito:.2f}\n"
                    print(
                        f"\nDepósito de R$ {valor_deposito:.2f} realizado com sucesso!")
                else:
                    print(
                        "\nOperação falhou! O valor informado é inválido. Deposite apenas valores positivos.")

            except ValueError:
                print("\nOperação falhou! Por favor, insira um valor numérico válido.")

        # --- Operação de Saque ---
        elif opcao == 's':
            print("\n--- Saque ---")
            try:
                valor_saque = float(input("Informe o valor do saque: R$ "))

                excedeu_saldo = valor_saque > saldo
                excedeu_limite_valor = valor_saque > limite_saque_valor
                excedeu_limite_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

                if excedeu_saldo:
                    print(
                        f"\nOperação falhou! Você não tem saldo suficiente. Saldo atual: R$ {saldo:.2f}")

                elif excedeu_limite_valor:
                    print(
                        f"\nOperação falhou! O valor do saque excede o limite de R$ {limite_saque_valor:.2f} por operação.")

                elif excedeu_limite_saques:
                    print(
                        f"\nOperação falhou! Número máximo de {LIMITE_SAQUES_DIARIOS} saques diários excedido.\n Tente novamente amanhã.")

                elif valor_saque > 0:
                    saldo -= valor_saque
                    extrato += f"Saque:\t\t\tR$ {valor_saque:.2f}\n"
                    numero_saques += 1
                    print(
                        f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso!")

                else:
                    print("\nOperação falhou! O valor informado é inválido.")

            except ValueError:
                print("\nOperação falhou! Por favor, insira um valor numérico válido.")

        # --- Operação de Extrato ---
        elif opcao == 'e':
            print("\n================ EXTRATO ================")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                print(extrato)
            print(f"\nSaldo atual:\t\tR$ {saldo:.2f}")
            print("========================================")

        # --- Sair do Sistema ---
        elif opcao == 'q':
            print("\nObrigado por usar nosso sistema. Até logo!")
            break

        # --- Opção Inválida ---
        else:
            print(
                "\nOperação inválida, por favor selecione novamente a operação desejada.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()