def get_start_end_idx(html: str):
    start_idx = 0
    end_idx = len(html)
    start = "ted&quot;:false}"
    end = "0"
    res, start_idx_res = find_from_to_index(html, start, end, start_idx, end_idx)
    start_idx_res -= 1500  # this selector is after first url, so we bo back 1500 chars

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


def get_indexes_of_promo_and_normal_offers(html):
    last_idx = len(html) - 150

    index_oferty_promowane = -1
    index_oferty_zwykle = -1
    try:
        tmp_index = 0
        selector = "mqu1_1j mryx_0 mp4t_0\">"
        selector_end = "<"
        oferty_title, tmp_index = find_from_to_index(html, selector, selector_end, tmp_index, last_idx)
        if oferty_title == "Oferty promowane":
            index_oferty_promowane = tmp_index
            oferty_title, tmp_index = find_from_to_index(html, selector, selector_end, tmp_index, last_idx)

        if oferty_title == "Oferty":
            index_oferty_zwykle = tmp_index
    except Exception as eee:
        print(eee)

    return (index_oferty_promowane, index_oferty_zwykle)


def get_title_index_row_list(html):
    title_idx_list = []
    tmp_indexing_index = 0
    last_idx = len(html) - 150
    for i in range(100):
        try:
            selector = "h2 class=\"mgn2"
            selector_end = ">"
            title, tmp_indexing_index = find_from_to_index(html, selector, selector_end, tmp_indexing_index, last_idx)
            title_idx_list.append([title, tmp_indexing_index])
        except Exception as eee:
            print(eee)
            break
    return title_idx_list



def get_url_index(html, start_idx):
    last_idx = len(html) - 150
    try:
        selector = "href=\""
        selector_end = "\""
        title, tmp_index = find_from_to_index(html, selector, selector_end, start_idx, last_idx)
        return title, tmp_index
    except Exception as eee:
        print(eee)
    return "", start_idx

def get_title_index(html, start_idx):
    last_idx = len(html) - 150
    try:
        selector = ">"
        selector_end = "<"
        title, tmp_index = find_from_to_index(html, selector, selector_end, start_idx, last_idx)
        return title, tmp_index
    except Exception as eee:
        print(eee)
    return "", start_idx

def get_ratings_numb_index(html, start_idx):
    last_idx = len(html) - 150
    try:
        selector = "id=\"rating-ful"
        selector_end = "\""
        title, tmp_index = find_from_to_index(html, selector, selector_end, start_idx, last_idx)
        selector = ">"
        selector_end = " o"
        title, tmp_index = find_from_to_index(html, selector, selector_end, tmp_index, last_idx)

        return int(title), tmp_index
    except Exception as eee:
        print(eee)
    return 0, start_idx

def get_numb_bought_last_30_days_index(html, start_idx):
    last_idx = len(html) - 150
    try:
        selector = "product_popularity\">"
        selector_end = " o"
        title, tmp_index = find_from_to_index(html, selector, selector_end, start_idx, last_idx)
        return int(title), tmp_index
    except Exception as eee:
        print(eee)
    return 0, start_idx

def get_offer_type_index(html, start_idx):
    last_idx = len(html) - 150
    try:
        selector = "mpof_ki mgn2_12\">"
        selector_end = "<"
        title, tmp_index = find_from_to_index(html, selector, selector_end, start_idx, last_idx)
        return title, tmp_index
    except Exception as eee:
        print(eee)
    return "", start_idx

def get_price_index(html, start_idx):
    last_idx = len(html) - 150
    try:
        selector = "mgn2_27 mgn2_30_s\">"
        selector_end = ","
        price_zl, tmp_index = find_from_to_index(html, selector, selector_end, start_idx, last_idx)
        selector = "m9qz_yq\">"
        selector_end = "<"
        price_gr, tmp_index = find_from_to_index(html, selector, selector_end, tmp_index, last_idx)
        price = price_zl + "." + price_gr
        return float(price), tmp_index
    except Exception as eee:
        print(eee)
    return 0, start_idx











