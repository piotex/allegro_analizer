import json
import random
import time
import pymongo
from SeleniumClient import SeleniumClient
from k0 import k0
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main2():
    usr = "pkubon2"
    pwd = ""
    with open('mongo_pwd.txt') as f:
        pwd = f.readlines()

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


def get_start_end_idx(html: str):
    start_idx = 0
    end_idx = len(html)
    start = "ted&quot;:false}"
    end = "0"
    res, start_idx_res = find_from_to_index(html, start, end, start_idx, end_idx)
    start_idx_res -= 1500 # this selector is after first url, so we bo back 1500 chars

    start_idx = 0
    start = "</ul></div> </section></div>"
    end = "</div>"
    res, last_idx_res = find_from_to_index(html, start, end, start_idx, end_idx)

    return (start_idx_res, last_idx_res)

def find_from_to_index(data: str, start: str, end: str, start_index: int, end_index: int):
    for i in range(start_index, len(data)):
        res = ""
        is_next = True
        if i > end_index:
            return res
        for j in range(len(start)):
            if data[i + j] != start[j]:
                is_next = False
                break
        if is_next:
            i += len(start)
            k = 0
            is_end = False
            while not is_end:
                is_end = True
                for l in range(len(end)):
                    if data[i + k + l] != end[l]:
                        is_end = False
                        break
                if not is_end:
                    res += data[i + k]
                k += 1
            return (res, i + k)
    return ""

def get_list_name_url_tuple(html, start_idx, last_idx):
    res_list = []
    for i in range(9999):
        try:
            start = "<a href=\""
            end = "\""
            url, start_idx = find_from_to_index(html, start, end, start_idx, last_idx)
            start = "}\">"
            end = "</a>"
            name, start_idx = find_from_to_index(html, start, end, start_idx, last_idx)
            res = (name, url)
            res_list.append(res)
        except Exception as eee:
            print(eee)
            break
    return res_list

def wait_for_selector(browser):
    try:
        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id=\"filters\"]/div[1]/div/div/div/section/div[2]/ul/li[1]/div/a")
            )
        )
    except Exception as eee:
        print(eee)

def is_last_node(html):
    start_idx = 400000
    last_idx = 1000000
    start = "<span class=\"mgmw_0t\">"
    end = "\""
    try:
        url, start_idx = find_from_to_index(html, start, end, start_idx, last_idx)
        return True
    except Exception as eee:
        return False

def save_list_json(main_name_url_list):
    file_name = "reports/main_name_url_list_" + time.strftime("%Y.%m.%d-%H.%M.%S") + ".json"
    with open(file_name, 'w') as F:
        F.write(json.dumps(main_name_url_list))

def get_categories_lists():
    res_path = 'C:\\Users\\pkubon\\.wdm\\drivers\\geckodriver\\win64\\0.33\\geckodriver.exe'
    browser = webdriver.Firefox(executable_path=res_path)

    base_url = "https://allegro.pl"

    main_name_url_list = k0.get_k0_3()
    count = 0
    while count < len(main_name_url_list):
        time.sleep(random.randint(0,9))
        try:
            url = main_name_url_list[count][-1]
            name_list = main_name_url_list[count][0:-1]
            browser.get(base_url + url)
            SeleniumClient.try_click_accept_pop(browser)
            wait_for_selector(browser)
            html = browser.page_source
            is_last_node_res = is_last_node(html)
            if not is_last_node_res:
                start_idx, last_idx = get_start_end_idx(html)
                name_url_list = get_list_name_url_tuple(html, start_idx, last_idx)
                for elem in name_url_list:
                    title = elem[0]
                    url = elem[1]
                    tmp = [a for a in name_list]
                    tmp.append(title)
                    tmp.append(url)
                    main_name_url_list.append(tmp)
        except Exception as eee:
            print(eee)

        count += 1
        if count % 100 == 0:
            save_list_json(main_name_url_list)

    save_list_json(main_name_url_list)



if __name__ == '__main__':
    # main2()
    get_categories_lists()
