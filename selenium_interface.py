import selenium_shopee
import selenium_amazon
import selenium_magalu
import os
from termcolor import colored


# Market Places distributor
def mkt_plc_distributor(mkt_plc):
    available_paths = []
    drivers_path = os.getcwd()
    drivers_path = drivers_path + "\\Chrome_Drivers\\"
    chrome_drive_version = 1
    available_drivers = [102, 103, 104]
    while True:
        for h in range(len(available_drivers)):
            print("[" + str(h + 1) + "]" + str(available_drivers[h]))
        print(colored("=-=" * 36, 'blue'))
        chrome_drive_version = input(str("Digite o código da versão do seu navegador chrome correspondente a uma das opções listadas: "))
        print(colored("=-=" * 36, 'blue'))
        if int(chrome_drive_version) > 0 and int(chrome_drive_version) < len(available_drivers):
            driver_path = drivers_path + str(available_drivers[int(chrome_drive_version) - 1])
            break
    if int(mkt_plc) == 1:
        selenium_shopee.shopee(driver_path)
    elif int(mkt_plc) == 2:
        selenium_amazon.amazon(driver_path)
    elif int(mkt_plc) == 3:
        selenium_magalu.magalu(driver_path)