import json
import os
import time
from selenium import webdriver

def test_find_from_to():
    from main import find_from_to_index

    data = "a-role=\"Categories\" class=\"\"><ul class=\" ala ma kota_7a_8\">"
    start = "<ul class=\" "
    end = "_7a_8\">"
    expected = "ala ma kota"
    res = find_from_to_index(data, start, end, 0)[0]
    assert res == expected

def test_find_from_to_2():
    from main import find_from_to_index

    html = "<ul class=\"mp4t_0"
    start_idx = 0
    start = "<ul class=\"mp4"
    end = "0"
    expected = "t_"
    res, start_idx = find_from_to_index(html, start, end, start_idx)
    assert res == expected

def test_stop_node():
    from main import is_last_node

    res_path = 'C:\\Users\\pkubon\\.wdm\\drivers\\geckodriver\\win64\\0.33\\geckodriver.exe'
    browser = webdriver.Firefox(executable_path=res_path)

    base_url = "https://allegro.pl/kategoria/akcesoria-lazienkowe-pozostale-54057"   # last node
    # base_url = "https://allegro.pl/kategoria/wyposazenie-akcesoria-lazienkowe-54051" # not last node
    browser.get(base_url)
    html = browser.page_source
    res = is_last_node(html)
    a = 3

def test_save_json():
    data = [['Wyposażenie Domu i Ogrodu', ' Akcesoria łazienkowe', '/kategoria/wyposazenie-akcesoria-lazienkowe-54051'],
     ['Wyposażenie Domu i Ogrodu', ' Dekoracje i ozdoby', '/kategoria/wyposazenie-dekoracje-i-ozdoby-9317'],
     ['Wyposażenie Domu i Ogrodu', ' Dywany i dywaniki', '/kategoria/wyposazenie-dywany-i-dywaniki-9018'],
     ['Wyposażenie Domu i Ogrodu', ' Gazetniki', '/kategoria/wyposazenie-gazetniki-319953'],
     ['Wyposażenie Domu i Ogrodu', ' Koszyki', '/kategoria/wyposazenie-koszyki-68679'],
     ['Wyposażenie Domu i Ogrodu', ' Lustra', '/kategoria/wyposazenie-lustra-15973']]

    file_name = "reports/main_name_url_list_" + time.strftime("%Y.%m.%d-%H.%M.%S") + ".json"

    with open(file_name, 'w', encoding="utf-8") as F:
        F.write(json.dumps(data))

    with open(file_name, 'r', encoding="utf-8") as F:
        B = json.loads(F.read())
        print(B)

def test_ala_take_end_nodes():
    aaa = os.getcwd()
    bbb = __file__

    file_name = "allegro_analizer/reports_res/dom_i_ogrod.json"
    with open(file_name, 'r', encoding="utf-8") as F:
        main_name_url_list = json.loads(F.read())

    res = sorted(main_name_url_list, key=lambda i: len(i), reverse=True)
    end_node_list = []
    categories = {}
    for elem in res:
        titles_list = elem[0:-1]
        is_end_node = False
        for title in titles_list:
            if title not in categories:  # is end node
                categories[title] = 0
                is_end_node = True
            categories[title] += 1      # increase category count
        if is_end_node:
            end_node_list.append(elem)

    file_name = "allegro_analizer/reports_res_endNodeList/dom_i_ogrod.json"
    with open(file_name, 'w', encoding="utf-8") as F:
        F.write(json.dumps(end_node_list))

    file_name = "allegro_analizer/reports_res_endNodeList/dom_i_ogrod_cat_count.json"
    res = dict(sorted(categories.items(), key=lambda item: item[1], reverse=True))
    with open(file_name, 'w', encoding="utf-8") as F:
        F.write(json.dumps(res))
    a = 0






















