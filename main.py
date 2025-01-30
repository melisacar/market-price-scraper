from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Chrome tarayıcısını başlatma
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Sayfayı açma
driver.get("https://www.hakmarexpress.com.tr/kategoriler")

# Kategorilerin bulunduğu öğenin yüklenmesini bekle
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "categories"))
)

# Sayfa kaynağını almak
html_content = driver.page_source

# BeautifulSoup ile sayfa kaynağını parse etme
soup = BeautifulSoup(html_content, 'html.parser')

# Kategori başlıklarını ve linklerini çekme
categories = soup.find_all('div', class_='category-title')

# Kategorilerin adlarını ve linklerini yazdırma
for category in categories:
    category_name = category.get_text(strip=True)
    # Bağlantının bulunduğu <a> etiketi varsa çekme
    category_link = category.find_parent('a')['href'] if category.find_parent('a') else None
    
    print(f"Kategori Adı: {category_name}")
    print(f"Kategori Linki: {category_link}")

# Tarayıcıyı kapatma
driver.quit()
