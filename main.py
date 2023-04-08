import pymongo
from lxml import html
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


def main2():
    usr = "pkubon2"
    pwd = ""

    client = pymongo.MongoClient(
        f"mongodb://{usr}:{pwd}@ac-1tltdjz-shard-00-00.kdizqwu.mongodb.net:27017,"
        f"ac-1tltdjz-shard-00-01.kdizqwu.mongodb.net:27017,"
        f"ac-1tltdjz-shard-00-02.kdizqwu.mongodb.net:27017/?"
        f"ssl=true&replicaSet=atlas-rba8e3-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.test

    mydb = client["allegro_database"]
    mycol = mydb["categories_collection"]

    mydict = {"name": "John", "address": "Highway 37"}

    x = mycol.insert_one(mydict)

def click_categories(browser):
    xpath_categories = "/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div/div[3]/header/div[2]/div/div[1]/button"
    element = browser.find_element(by=By.XPATH, value=xpath_categories)
    browser.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

def get_touple_name_url(browser, i):
    xpath_l2 = f"/html/body/div[2]/div[5]/div/div[2]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/div/section/div[2]/ul/li[{i}]/div/a"
    element = browser.find_element(by=By.XPATH, value=xpath_l2)
    return (element.text, element.get_attribute('href'))

def try_click_accept_pop(browser):
    try:
        xpath_accept = "/html/body/div[2]/div[1]/div/div[2]/div/div[2]/button[1]"
        element = browser.find_element(by=By.XPATH, value=xpath_accept)
        browser.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    except:
        pass

def get_sub_categories_list_touple_title_url(browser, url):
    browser.get(url)
    try_click_accept_pop(browser)
    k2 = []
    for j in range(1, 19999):
        try:
            title, url = get_touple_name_url(browser, j)
            k2.append((title, url))
        except Exception as eee:
            print(eee)
            break
    return k2

def get_categories_lists():
    k1 = range(1, 13)
    url = "https://allegro.pl/"
    xpath = "/html/body/div[2]/div/div/div/div/div/div/div/div/div/div[3]/header/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/div/div/ul/li/a"
    xpath = "/html/body/div[2]/div/div/div/div/div/div/div/div/div/div[3]/header/div[2]/div/div[1]/div/div/div/div[4]/div/div/div/div/div/div/div[1]/div/div/div[3]/div/div/ul/li/a"

    # res_path = GeckoDriverManager().install()
    res_path = 'C:\\Users\\pkubon\\.wdm\\drivers\\geckodriver\\win64\\0.33\\geckodriver.exe'
    browser = webdriver.Firefox(executable_path=res_path)

    browser.get(url)

    try_click_accept_pop(browser)

    click_categories(browser)

    k0_1 = [
        "https://allegro.pl/kategoria/telefony-i-akcesoria",
        "https://allegro.pl/kategoria/komputery",
        "https://allegro.pl/kategoria/tv-i-video-717",
        "https://allegro.pl/kategoria/konsole-i-automaty",
        "https://allegro.pl/kategoria/agd-drobne-67414",
        "https://allegro.pl/kategoria/agd-wolnostojace-67413",
        "https://allegro.pl/kategoria/agd-do-zabudowy-67524",
        "https://allegro.pl/kategoria/fotografia",
    ]
    k0_2 = [
        "https://allegro.pl/kategoria/bizuteria-i-zegarki",
        "https://allegro.pl/kategoria/bielizna-damska-75993",
        "https://allegro.pl/kategoria/bielizna-meska-256925",
        "https://allegro.pl/kategoria/odziez-damska-76033",
        "https://allegro.pl/kategoria/odziez-meska-1455",
        "https://allegro.pl/kategoria/obuwie-1469",
        "https://allegro.pl/kategoria/galanteria-i-dodatki-1487",
        "https://allegro.pl/kategoria/odziez-obuwie-dodatki-bagaz-300537",
        "https://allegro.pl/kategoria/przebrania-kostiumy-maski-74170",
        "https://allegro.pl/kategoria/ciaza-i-macierzynstwo-78013",
        "https://allegro.pl/kategoria/slub-i-wesele-74169",
    ]
    k0_3 = [
        ["Wyposażenie Domu i Ogrodu", "https://allegro.pl/kategoria/wyposazenie-123"],
        # ["Narzędzia warsztatowe, budowlane", "https://allegro.pl/kategoria/narzedzia-1536"],
        # ["Oświetlenie domu", "https://allegro.pl/kategoria/oswietlenie-5317"],
        # ["Budownictwo i Akcesoria", "https://allegro.pl/kategoria/budownictwo-i-akcesoria-1520"],
        # ["Ogród, wszystko do ogrodu", "https://allegro.pl/kategoria/ogrod-1532"],
        # ["Meble", "https://allegro.pl/kategoria/meble-522"],
    ]

    count = 0
    len_k0_3 = len(k0_3)
    while len_k0_3 > count:
        i = count
        title_list = []
        url = k0_3[i][-1]
        for j in range(len(k0_3[i])-1):
            title_list.append(k0_3[i][j])

        res_touple = get_sub_categories_list_touple_title_url(browser, url)
        for elem_1 in res_touple:
            title_1 = elem_1[0]
            url_1 = elem_1[1]

            title_list.append(title_1)
            title_list.append(url_1)
            k0_3.append(title_list)
            # break

        len_k0_3 = len(k0_3)
        count += 1

    print(k0_3)
    # browser.close()

    # file = open('Failed.txt', 'w')
    # file.write(html_source)
    # file.close()


if __name__ == '__main__':
    # main2()
    get_categories_lists()
