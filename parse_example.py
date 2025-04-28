import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

    try:
        driver.maximize_window()
        driver.get('https://example.com')
        assert 'Example' in driver.title, 'Заголовок страницы не содержит "Example"'

        links = driver.find_elements(By.CSS_SELECTOR, 'a')
        more_info_links = list(filter(lambda l: 'More information' in l.text, links))
        assert len(more_info_links) > 0, 'Ссылка с текстом "More information" не найден'

        more_info_links[0].click()
        assert driver.current_url == 'https://www.iana.org/help/example-domains', 'Совершен переход на некорректный URL'

        time.sleep(10)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
