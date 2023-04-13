import json
import time
from datetime import datetime
from allegro_analizer.utils.SeleniumClient import wait_for_selector
from allegro_analizer.utils.html_scraper import find_from_to_index, get_indexes_of_promo_and_normal_offers, \
    get_title_index_row_list, get_title_index, get_price_index, \
    get_url_index, get_ratings_numb_index, get_numb_bought_last_30_days_index, get_offer_type_index
from selenium import webdriver
from os import listdir
from os.path import isfile, join


def test_parse_page_model_list():
    dir_name = "reports_res_Row_elem_data"
    only_files = [dir_name + "/" + f for f in listdir(dir_name) if isfile(join(dir_name, f))]

    res_list = []
    for path in only_files:
        html = ""
        with open(path, 'r') as f:
            html = f.read()
        idx = 0
        url, idx = get_url_index(html, idx)
        title, idx = get_title_index(html, idx)
        number_of_ratings, tmp_idx = get_ratings_numb_index(html, idx)
        numb_of_bought_last_30_days, tmp_idx = get_numb_bought_last_30_days_index(html, idx)
        offer_type, tmp_idx = get_offer_type_index(html, idx)
        price, idx = get_price_index(html, idx)

        model = {
            "url": url,
            "title": title,
            "number_of_ratings": number_of_ratings,
            "numb_of_bought_last_30_days": numb_of_bought_last_30_days,
            "offer_type": offer_type,
            "price": price,
        }
        res_list.append(model)
        # print(f"{i} z {len(only_files)}")

    res_list_no_duplicates = []
    key_dict_title = {}
    key_dict_price = {}
    key_dict_number_of_ratings = {}
    for model in res_list:
        if model["title"] not in key_dict_title or \
                model["price"] not in key_dict_price or \
                model["number_of_ratings"] not in key_dict_number_of_ratings:
            res_list_no_duplicates.append(model)
            key_dict_title[model["title"]] = 0
            key_dict_price[model["price"]] = 0
            key_dict_number_of_ratings[model["number_of_ratings"]] = 0

    res_list_1 = sorted(res_list_no_duplicates, key=lambda x: x['number_of_ratings'], reverse=True)
    file_name = "reports_page_model_list/elem_list_number_of_ratings_" + datetime.utcnow().strftime('%Y.%m.%d-%H.%M.%S.%f')[:-2] + ".json"
    with open(file_name, 'w') as F:
        F.write(json.dumps(res_list_1))

    res_list_2 = sorted(res_list_no_duplicates, key=lambda x: x['numb_of_bought_last_30_days'], reverse=True)
    file_name = "reports_page_model_list/elem_list_numb_of_bought_last_30_days_" + datetime.utcnow().strftime('%Y.%m.%d-%H.%M.%S.%f')[:-2] + ".json"
    with open(file_name, 'w') as F:
        F.write(json.dumps(res_list_2))

