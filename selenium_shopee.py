from selenium import webdriver


def shopee(driver_path):

    driver = webdriver.Chrome(str(driver_path))
    driver.get("https://shopee.com.br/")
    assert "Shopee" in driver.title
    driver.maximize_window()

    print("Shopee caralho")