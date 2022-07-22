import Validadores
import selenium_interface
from termcolor import colored
import getpass


# Keep requesting the e-mail while the user don't write "SAIR"
keep_going = True
while keep_going == True:
    # E-mail validation
    email_validation = True
    print(colored("=-=" * 36, 'blue'))
    email_1 = str(input("Digite o e-mail ou " + "'SAIR'" + " para finalizar o programa: "))
    if email_1.strip().upper() == "SAIR":
        print(colored("=-=" * 36, 'blue'))
        print(colored("Finalizando o programa...", 'red'))
        print(colored("=-=" * 36, 'blue'))
        quit()
    email_2 = str(input("Digite o e-mail novamente para verificação: "))

    if email_validation == Validadores.validate_domain(email_1, email_2):
        print(colored("=-=" * 36, 'blue'))
        print(colored("E-mail válido", 'yellow'))
        # Password validation
        for h in range(3, -1, -1):
            print(colored("=-=" * 36, 'blue'))
            marketplaces = """[1]Shopee
[2]Amazon
[3]Magalu
[4]Gerar relatório
[5]Finalizar o programa"""
            password_1 = str(getpass.getpass("Digite a senha: "))
            password_2 = str(getpass.getpass("Digite a senha novamente: "))
            password_validation = Validadores.validate_password(password_1, password_2)
            if password_validation is True:
                print(colored("=-=" * 36, 'blue'))
                print(colored("Senha válida", 'yellow'))
                # Ask the user which marketplaces he wants to appear in the final report
                print(colored("=-=" * 36, 'blue'))
                print(marketplaces)
                marketplaces_codes_list = [1, 2, 3]
                marketplaces_user_list = []
                while len(marketplaces_user_list) == 0:
                    print(colored("=-=" * 36, 'blue'))
                    mkt_code_1 = str(input("Digite o código desejado: "))
                    print(colored("=-=" * 36, 'blue'))
                    try:
                        if int(mkt_code_1) in marketplaces_codes_list:
                            marketplaces_user_list.append(int(mkt_code_1))
                            mkt_code_2 = "0"
                            while int(mkt_code_2) != 4:
                                print(marketplaces)
                                print(colored("=-=" * 36, 'blue'))
                                mkt_code_2 = str(input("Insira outro código: "))
                                print(colored("=-=" * 36, 'blue'))
                                for m in marketplaces_user_list:
                                    if int(mkt_code_2) == int(m):
                                        print(colored("Esse código já foi inserido!", 'red'))
                                        print(colored("=-=" * 36, 'blue'))
                                        break
                                if int(mkt_code_2) in marketplaces_codes_list:
                                    marketplaces_user_list.append(int(mkt_code_2))
                                    marketplaces_user_list = set(marketplaces_user_list)
                                    marketplaces_user_list = list(marketplaces_user_list)
                                elif int(mkt_code_2) == 4:
                                    continue
                                elif int(mkt_code_2) == 5:
                                    print(colored("Finalizando o programa...", 'red'))
                                    print(colored("=-=" * 36, 'blue'))
                                    quit()
                                else:
                                    print(colored("O código inserido não é válido!", 'red'))
                                    print(colored("=-=" * 36, 'blue'))
                                    print(marketplaces)
                                    continue
                            for mkt_plc in marketplaces_user_list:
                                selenium_interface.mkt_plc_distributor(mkt_plc)
                            print(colored("=-=" * 36, 'blue'))
                            print("RECEBA!")
                            print(colored("=-=" * 36, 'blue'))
                            quit()
                        elif int(mkt_code_1) == 4:
                            print(colored("Por gentileza, insira o código de pelo menos um marketplace antes de prosseguir com a geração do relatório.", 'yellow'))
                            print(colored("=-=" * 36, 'blue'))
                            print(marketplaces)
                            continue
                        elif int(mkt_code_1) == 5:
                            print(colored("Finalizando o programa...", 'red'))
                            print(colored("=-=" * 36, 'blue'))
                            quit()
                        else:
                            print(colored("O código inserido não é válido!", 'red'))
                            print(colored("=-=" * 36, 'blue'))
                            print(marketplaces)
                    except ValueError:
                        print(colored("O código inserido não é válido!", 'red'))
                        print(colored("=-=" * 36, 'blue'))
                        print(marketplaces)
            else:
                print(colored("=-=" * 36, 'blue'))
                if h == 0:
                    print(colored("Limite de tentativas atingido, reiniciando programa...", 'red'))
                    continue
                else:
                    print(colored(f"As senhas não correspondem. Tentativas restantes: {h}", 'red'))
    else:
        print(colored("=-=" * 36, 'blue'))
        print(colored(Validadores.validate_domain(email_1, email_2), 'red'))
        continue