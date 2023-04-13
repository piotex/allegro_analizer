import json
import random
import time
from selenium import webdriver
from allegro_analizer.utils.SeleniumClient import try_click_accept_pop, wait_for_selector
from allegro_analizer.utils.html_scraper import is_last_node, get_start_end_idx, get_list_name_url_tuple
from allegro_analizer.utils.k0 import k0


def save_list_json(main_name_url_list):
    file_name = "reports/main_name_url_list_" + time.strftime("%Y.%m.%d-%H.%M.%S") + ".json"
    with open(file_name, 'w') as F:
        F.write(json.dumps(main_name_url_list))


def test_get_categories_lists():
    # res_path = GeckoDriverManager().install()
    res_path = 'C:\\Users\\pkubon\\.wdm\\drivers\\geckodriver\\win64\\0.33\\geckodriver.exe'
    browser = webdriver.Firefox(executable_path=res_path)

    base_url = "https://allegro.pl"

    main_name_url_list = k0.get_k0_3()
    count = 0
    while count < len(main_name_url_list):
        time.sleep(random.randint(0, 9))
        try:
            url = main_name_url_list[count][-1]
            name_list = main_name_url_list[count][0:-1]
            browser.get(base_url + url)
            try_click_accept_pop(browser)
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

        # if count >= 10:
        #     break

    save_list_json(main_name_url_list)


