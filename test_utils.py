import json
import time

from seleniumwire import webdriver

from allegro_analizer.main import find_from_to_index, is_last_node


def test_find_from_to():
    data = "a-role=\"Categories\" class=\"\"><ul class=\" ala ma kota_7a_8\">"
    start = "<ul class=\" "
    end = "_7a_8\">"
    expected = "ala ma kota"
    res = find_from_to_index(data, start, end, 0)[0]
    assert res == expected

def test_find_from_to_2():
    html = "<ul class=\"mp4t_0"
    start_idx = 0
    start = "<ul class=\"mp4"
    end = "0"
    expected = "t_"
    res, start_idx = find_from_to_index(html, start, end, start_idx)
    assert res == expected

def test_stop_node():
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