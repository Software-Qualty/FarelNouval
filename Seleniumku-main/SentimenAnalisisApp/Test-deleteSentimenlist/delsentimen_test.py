import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tunggu sebelum menutup WebDriver
        time.sleep(5)
        self.driver.quit()

    def login(self, username, password):
        # Temukan input email dan password
        time.sleep(2)
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")

        # Masukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(2)
        # Klik tombol login
        button = self.driver.find_element(By.ID, "button")
        button.click()

        # Tunggu alert muncul
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            # Tangani alert dengan menerima (klik OK)
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            # Jika alert tidak muncul dalam 10 detik, tangani sesuai kebutuhan
            pass

        print("Login berhasil")


    def createTopikSentimen(self):
        #klik daftar sentimen
        time.sleep(10)
        button = self.driver.find_element(By.XPATH, "//a[@href='sentimen.html']")
        button.click()

        #klik tombol tambah
        button = self.driver.find_element(By.ID, "showModalButton")
        button.click()

        time.sleep(2)
        # masukkan judul, topik yang ingin dianalisis, dan sumber data
        judul_input = self.driver.find_element(By.ID, "judulInput")
        time.sleep(2)
        topik_input = self.driver.find_element(By.ID, "topikInput")
        time.sleep(2)

        radio_youtube = self.driver.find_element(By.ID, "radioYoutube")
        radio_youtube.click()

        # Memasukkan nama pengguna dan kata sandi
        judul_input.send_keys("selenium")
        topik_input.send_keys("KQKfULYtaI0")
        

        # klik tombol simpan
        button = self.driver.find_element(By.ID, "saveModalButton")
        button.click()
        print("Topik berhasil ditambahkan")

    def test_createTopikSentimen(self):
        # Buka halaman web
        self.driver.get("https://trensentimen.my.id/")

        # Login
        self.login("farel123@gmail.com", "farelnd23")

        self.createTopikSentimen()

if __name__ == "__main__":
    unittest.main()
