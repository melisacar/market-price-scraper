from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.hakmarexpress.com.tr/kategoriler")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "categories"))
)

# Kategorileri al
categories = driver.find_elements(By.CLASS_NAME, 'category-title')

for i in range(len(categories)):  
    categories = driver.find_elements(By.CLASS_NAME, 'category-title')  # Kategorileri tekrar bul
    category = categories[i]
    category_name = category.text.strip()
    print(f"Kategorilere Tıklanıyor: {category_name}")

    # Kategoriye tıkla
    ActionChains(driver).move_to_element(category).click().perform()

    # Sayfanın yüklenmesini bekle
    time.sleep(3)
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-price'))
        )
    except:
        print(f"HATA: '{category_name}' kategorisinde ürün bulunamadı veya HTML yapısı farklı!")
        driver.back()  
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "categories"))
        )
        continue  # Sonraki kategoriye geç

    # Sayfayı kaydırarak tüm ürünleri yükle
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Yeni öğelerin yüklenmesi için bekle

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Ürünleri listele
    product_names = driver.find_elements(By.CLASS_NAME, 'product-title')  
    product_prices = driver.find_elements(By.CLASS_NAME, 'product-price')

    if not product_names or not product_prices:
        print(f"UYARI: '{category_name}' kategorisinde ürün bilgisi alınamadı!")

    for product_name, product_price in zip(product_names, product_prices):
        print(f"Ürün Adı: {product_name.text.strip()} - Fiyat: {product_price.text.strip()}")

    driver.back()  

    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.CLASS_NAME, "categories"))
    )

driver.quit()