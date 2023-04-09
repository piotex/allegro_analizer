from selenium.webdriver.common.by import By


class SeleniumClient():
    @staticmethod
    def click_categories(browser):
        xpath_categories = "/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div/div[3]/header/div[2]/div/div[1]/button"
        element = browser.find_element(by=By.XPATH, value=xpath_categories)
        browser.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @staticmethod
    def get_touple_name_url(browser, i):
        xpath_l2 = f"/html/body/div[2]/div[5]/div/div[2]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/div/section/div[2]/ul/li[{i}]/div/a"
        element = browser.find_element(by=By.XPATH, value=xpath_l2)
        return (element.text, element.get_attribute('href'))

    @staticmethod
    def try_click_accept_pop(browser):
        try:
            xpath_accept = "/html/body/div[2]/div[1]/div/div[2]/div/div[2]/button[1]"
            element = browser.find_element(by=By.XPATH, value=xpath_accept)
            browser.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        except:
            pass

    @staticmethod
    def get_sub_categories_list_touple_title_url(browser, url):
        browser.get(url)
        SeleniumClient.try_click_accept_pop(browser)
        k2 = []
        for j in range(1, 19999):
            try:
                title, url = SeleniumClient.get_touple_name_url(browser, j)
                k2.append((title, url))
            except Exception as eee:
                print(eee)
                break
        return k2
