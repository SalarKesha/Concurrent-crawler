from multiprocessing import Lock as mpLock
from threading import Lock as mtLock
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from storage import products
import queue

q = queue.Queue()


# multi_processing_lock = mpLock
# multi_thread_lock = mtLock
def crawl_mt():
    while True:
        search_word = q.get()
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("https://emalls.ir/")
        input_element = driver.find_element('xpath', '//*[@id="SearchInBottom_txtSearch"]')
        input_element.clear()
        input_element.send_keys(search_word)
        # element.send_keys(Keys.RETURN)
        btn = driver.find_element('xpath', '//*[@id="SearchInBottom_btnSearch"]')
        btn.click()
        list_container = driver.find_element('xpath', '//*[@id="listdiv"]')
        product_elements = list_container.find_elements(By.CLASS_NAME, 'product-block-parent')
        for product_element in product_elements:
            image_element = product_element.find_element(By.TAG_NAME, 'img').get_attribute('src')
            # print(f"img:{image_element}")
            title_element = product_element.find_element(By.CLASS_NAME, 'prd-name').text
            # print(f"title:{title_element}")
            price_element = product_element.find_element(By.CLASS_NAME, 'prd-price').find_element(By.TAG_NAME,
                                                                                                  'span').text
            # print(f"price:{price_element}")
            product = {'title': title_element, 'image': 'https://emalls.ir' + image_element, 'price': price_element}
            products.append(product)
        # sleep(10)
        driver.close()
        q.task_done()
        if q.empty():
            break


def crawl_mp(search_word):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://emalls.ir/")
    element = driver.find_element('xpath', '//*[@id="SearchInBottom_txtSearch"]')
    element.clear()
    element.send_keys(search_word)
    # element.send_keys(Keys.RETURN)
    btn = driver.find_element('xpath', '//*[@id="SearchInBottom_btnSearch"]')
    btn.click()
    list_container = driver.find_element('xpath', '//*[@id="listdiv"]')
    product_elements = list_container.find_elements(By.CLASS_NAME, 'product-block-parent')
    for product_element in product_elements:
        image_element = product_element.find_element(By.TAG_NAME, 'img').get_attribute('src')
        # print(f"img:{image_element}")
        title_element = product_element.find_element(By.CLASS_NAME, 'prd-name').text
        # print(f"title:{title_element}")
        price_element = product_element.find_element(By.CLASS_NAME, 'prd-price').find_element(By.TAG_NAME,
                                                                                              'span').text
        # print(f"price:{price_element}")
        product = {'title': title_element, 'image': 'https://emalls.ir' + image_element, 'price': price_element}
        products.append(product)
    # sleep(10)
    driver.close()
