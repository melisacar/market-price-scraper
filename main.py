from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver'ı otomatik olarak indirmek ve başlatmak için:
service = Service(ChromeDriverManager().install())

# Chrome tarayıcısını başlatma
driver = webdriver.Chrome(service=service)

# Sayfayı açma
driver.get("https://www.hakmarexpress.com.tr/kategoriler")

# Sayfanın tamamen yüklenmesini beklemek için bir süre bekleyin
import time
time.sleep(5)

# Sayfa kaynağını almak
html_content = driver.page_source

# HTML içeriğini yazdırma
print(html_content)

# Tarayıcıyı kapatma
driver.quit()
