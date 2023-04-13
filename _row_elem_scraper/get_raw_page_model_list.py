import json
import time
from datetime import datetime
import random

from allegro_analizer.utils.SeleniumClient import wait_for_selector, try_merge_same_offers, try_click_accept_pop, \
    wait_for_selector_same_offers
from allegro_analizer.utils.html_scraper import find_from_to_index, get_indexes_of_promo_and_normal_offers, \
    get_title_index_row_list
from selenium import webdriver


def test_get_raw_page_model_list():
    res_path = 'C:\\Users\\pkubon\\.wdm\\drivers\\geckodriver\\win64\\0.33\\geckodriver.exe'
    base_url = "https://allegro.pl/kategoria/lampy-lampy-solne-300841?order=qd"  # all kinds of offers
    browser = webdriver.Firefox(executable_path=res_path)

    browser.get(base_url)
    wait_for_selector(browser)
    try_click_accept_pop(browser)
    try_merge_same_offers(browser)
    wait_for_selector_same_offers(browser)
    html = browser.page_source

    title_idx_list = get_title_index_row_list(html)
    for i in range(len(title_idx_list)):
        file_name = "reports_res_Row_elem_data/elem_" + datetime.utcnow().strftime('%Y.%m.%d-%H.%M.%S.%f')[:-2] + ".txt"
        idx = title_idx_list[i][1]
        idx_next = idx + 10000
        if i < len(title_idx_list)-1:
            idx_next = title_idx_list[i+1][1]
        data = html[idx:idx_next]
        with open(file_name, 'w') as F:
            F.write(data)

    for i in range(2, 101):
        try:
            time.sleep(random.randint(0, 9))
            browser.get(base_url + f"&p={i}")
            wait_for_selector_same_offers(browser)
            html = browser.page_source

            title_idx_list = get_title_index_row_list(html)
            for i in range(len(title_idx_list)):
                file_name = "reports_res_Row_elem_data/elem_" + \
                            datetime.utcnow().strftime('%Y.%m.%d-%H.%M.%S.%f')[:-2] + ".txt"
                idx = title_idx_list[i][1]
                idx_next = idx + 10000
                if i < len(title_idx_list) - 1:
                    idx_next = title_idx_list[i + 1][1]
                data = html[idx:idx_next]
                with open(file_name, 'w') as F:
                    F.write(data)
        except Exception as eee:
            print(eee)
            break

    return 1

