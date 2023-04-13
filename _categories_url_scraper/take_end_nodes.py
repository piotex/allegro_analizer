import json
import os


def test_take_end_nodes():
    aaa = os.getcwd()
    # bbb = __file__

    file_name = "reports_res/dom_i_ogrod.json"
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

    file_name = "reports_res_endNodeList/dom_i_ogrod.json"
    with open(file_name, 'w', encoding="utf-8") as F:
        F.write(json.dumps(end_node_list))

    file_name = "reports_res_endNodeList/dom_i_ogrod_cat_count.json"
    res = dict(sorted(categories.items(), key=lambda item: item[1], reverse=True))
    with open(file_name, 'w', encoding="utf-8") as F:
        F.write(json.dumps(res))
    a = 0