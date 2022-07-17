import selenium_shopee
import selenium_amazon
import selenium_magalu
from termcolor import colored


# Market Places distributor
def mkt_plc_distributor(mkt_plc):
    available_paths = []
    driver_102 = r'C:\Users\User\Desktop\BOLOLO\HENRIQUENATOR\Relatório_De_Vendas-16-06-22\Chrome_Drivers\102\chromedriver.exe'
    available_paths.append(driver_102)
    driver_103 = r'C:\Users\User\Desktop\BOLOLO\HENRIQUENATOR\Relatório_De_Vendas-16-06-22\Chrome_Drivers\103\chromedriver.exe'
    available_paths.append(driver_103)
    driver_104 = r'C:\Users\User\Desktop\BOLOLO\HENRIQUENATOR\Relatório_De_Vendas-16-06-22\Chrome_Drivers\104\chromedriver.exe'
    available_paths.append(driver_104)
    chrome_drive_version = 1
    available_drivers = [102, 103, 104]
    while True:
        for h in range(len(available_drivers)):
            print("[" + str(h + 1) + "]" + str(available_drivers[h]))
        print(colored("=-=" * 36, 'blue'))
        chrome_drive_version = input(str("Digite o código da versão do seu navegador chrome correspondente a uma das opções listadas: "))
        print(colored("=-=" * 36, 'blue'))
        if int(chrome_drive_version) > 0 and int(chrome_drive_version) < len(available_drivers):
            driver_path = available_paths[int(chrome_drive_version) - 1]
            break
    if int(mkt_plc) == 1:
        selenium_shopee.shopee(driver_path)
    elif int(mkt_plc) == 2:
        selenium_amazon.amazon(driver_path)
    elif int(mkt_plc) == 3:
        selenium_magalu.magalu(driver_path)