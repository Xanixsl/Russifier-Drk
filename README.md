# Russifier DRK - Русификатор для драйверов Darmoshark

![Badge](https://hitscounter.dev/api/hit?url=https%3A%2F%2Fgithub.com%2FXanixsl%2FRussifier-Drk&label=Visitors&icon=people&color=%23c5b3e6)
[![Downloads](https://img.shields.io/github/downloads/Xanixsl/Russifier-Drk/total?label=Downloads&style=flat-square)](https://github.com/Xanixsl/Russifier-Drk/releases)
[![Latest Version](https://img.shields.io/github/v/release/Xanixsl/Russifier-Drk?label=Latest%20Version&style=flat-square)](https://github.com/Xanixsl/Russifier-Drk/releases/latest)
[![License](https://img.shields.io/github/license/Xanixsl/Russifier-Drk?label=License&style=flat-square)](LICENSE)

<img src="https://github.com/user-attachments/assets/0f139f68-0bd6-4068-b7e9-9480534085d2" alt="Russifier DRK Screenshot" width="650"/>

## 🚀 О программе

**Russifier DRK** - это программа для автоматического перевода драйверов мыши **Darmoshark** моделей **M3, M3s и N3** на русский язык без необходимости ручного изменения файлов локализации.

🔗 **Официальный сайт:** [https://russifier-drk.ru/](https://russifier-drk.ru/)

## ✨ Особенности

✔ Полностью автоматический процесс русификации  
✔ Безопасность: все файлы остаются на вашем ПК  
✔ Возможность отката к стандартным настройкам  
✔ Современный интерфейс с эффектами прозрачности  
✔ Поддержка версий драйверов 1.6.5 - 1.8.2.9  

🔒 **Важно:** Русификатор НЕ собирает и НЕ отправляет ваши данные! Все файлы хранятся строго на вашем компьютере.

## 📥 Установка

1. Скачайте последнюю версию программы:
   - [Скачать DRK.exe v2.0.0](https://github.com/Xanixsl/Russifier-Drk/releases/download/v2.0.0/DRK.exe)
   - [Все версии](https://github.com/Xanixsl/Russifier-Drk/releases)

2. Запустите программу от имени администратора

## 🛠 Как это работает

1. Программа ищет драйвер (`DeviceDriver.exe`)
2. Определяет папку локализации (`language`)
3. Заменяет стандартные файлы на переведенные
4. Сохраняет путь в кэш для быстрого отката

## 🔄 Как переключить язык после русификации

1. Дождитесь, пока Russifier DRK запустит драйвер мыши
2. Перейдите в самую нижнюю вкладку настроек драйвера
3. Во вкладке с выпадающим списком выберите язык **English**

> **Примечание:** Перевод на русский язык работает только при выборе английского языка в драйвере.

## 📂 О кэше программы

Кэш - это временное хранилище данных, которое:
- Сохраняет путь к драйверу мыши (`DeviceDriver.exe`)
- Ускоряет повторный запуск программы
- Позволяет быстро откатить изменения

Чтобы открыть папку TEMP (где хранится кэш):
1. Нажмите `Win + R`
2. Введите `%temp%`
3. Нажмите `Enter`

## 💻 Технические детали

Программа написана на Python с использованием:
- PyQt5 для современного интерфейса
- psutil для работы с процессами
- ctypes для запроса прав администратора

## 📜 Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).

## 👨‍💻 Разработчик

**Saylont (Xanixsl на GitHub)**  
💖 Поддержать разработчика:  
- [DonationAlerts](https://www.donationalerts.com/r/saylont)  
- [Boosty](https://boosty.to/saylontoff/donate)  
