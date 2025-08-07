import asyncio
import random
from hikka import utils, loader
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RobloxAccountCreator(loader.Module):
    """Модуль для автоматизированной регистрации аккаунтов в Roblox"""

    strings = {"name": "RobloxAccountCreator"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            "ROBLOX_ACCOUNT_CREATOR",
            {
                "email": loader.ModuleConfigItem("user@example.com", "Электронная почта для нового аккаунта"),
            },
        )

    def generate_username(self):
        """Генерирует случайное имя пользователя, начинающееся с 'hikka' и заканчивающееся числом от 0 до 9999."""
        return f"hikka{random.randint(0, 9999)}"

    def generate_password(self):
        """Генерирует случайный пароль, начинающийся с 'hikka' и заканчивающееся числом от 0 до 9999."""
        return f"hikka{random.randint(0, 9999)}"

    async def acc_cmd(self, message):
        """ .acc Команда для создания нового аккаунта в Roblox. """
        await utils.answer(message, "Начало создания нового аккаунта в Roblox...")

        # Настройка WebDriver (например, для Chrome)
        driver = webdriver.Chrome()

        try:
            # Генерация имени пользователя и пароля
            username = self.generate_username()
            password = self.generate_password()

            # Открытие страницы регистрации Roblox
            driver.get("https://www.roblox.com/signup")

            # Заполнение формы регистрации
            username_field = driver.find_element(By.ID, "signup-username")
            password_field = driver.find_element(By.ID, "signup-password")
            email_field = driver.find_element(By.ID, "signup-email")

            username_field.send_keys(username)
            password_field.send_keys(password)
            email_field.send_keys(self.config["email"])

            # Подтверждение регистрации
            driver.find_element(By.ID, "signup-button").click()

            # Ожидание завершения процесса регистрации
            time.sleep(5)

            await utils.answer(message, f"Аккаунт успешно создан!\nИмя пользователя: {username}\nПароль: {password}")
        except Exception as e:
            await utils.answer(message, f"Произошла ошибка: {e}")
        finally:
            driver.quit()