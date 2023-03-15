from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import os
from create_dir import create_dir, create_name_dir
from input_url import url
from create_name_for_page import create_name_page

if __name__ == '__main__':
    name_dir = create_name_dir()
    create_dir_ = create_dir()
    os.chdir(name_dir)
    if create_dir_:
        print('Не пугайтесь большому количесву ошибок.')
        print('Парсинг запущен')
        driver = webdriver.Chrome(executable_path="C:\\Users\\cymsi\\Desktop\\парсинг заработок\\chrome\\chromedriver.exe")
        print('Загрузка...')

        driver.get(url)
        
        div_img = driver.find_elements(By.CLASS_NAME, "reader-view__wrap")
        print('Загрузка страниц...')

        try:
            for i in range(0,300):
                src_img = div_img[i].find_element(By.TAG_NAME, "img").get_attribute("src")
                get_img = requests.get(src_img)
                name_page = create_name_page() + str(i+1) + src_img[-4:]
                print(name_page + ' - загружено')
                
                file_img = open(name_page, 'wb')
                file_img.write(get_img.content)
                file_img.close()
                
                div_img[i].click()
                time.sleep(0.5)
        except IndexError:
            pass
            print('Парсинг закончин')
        driver.close()
        driver.quit()
