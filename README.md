# Russifier DRK - Русификатор для драйверов Darmoshark

[![Download](https://img.shields.io/badge/Download-DRK_Russifier-ff6b8b?style=for-the-badge&logo=github&logoColor=white&labelColor=ffc3d0)](https://github.com/Xanixsl/Russifier-Drk/releases/latest/download/DRK.exe)
![Badge](https://hitscounter.dev/api/hit?url=https%3A%2F%2Fgithub.com%2FXanixsl%2FRussifier-Drk&label=Visitors&icon=people&color=%23c5b3e6)
[![Latest Version](https://img.shields.io/github/v/release/Xanixsl/Russifier-Drk?label=Latest%20Version&style=flat-square)](https://github.com/Xanixsl/Russifier-Drk/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square&logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

<img src="https://github.com/user-attachments/assets/0f139f68-0bd6-4068-b7e9-9480534085d2" alt="Russifier DRK Screenshot" width="650"/>

[![Download Multi Lang Version](https://img.shields.io/badge/Download-Multi_Lang_Version-0078D7?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Xanixsl/Drk-Multi-Lang)
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

<img src="https://github.com/user-attachments/assets/56ab3c34-8fef-425c-881f-381c5d78617c" alt="Russifier DRK Screenshot" width="650"/>

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
<img src="https://github.com/user-attachments/assets/34478cde-6cee-4914-8df6-a51628710985" alt="Russifier DRK Screenshot" width="750"/>

Кэш - это временное хранилище данных, которое:
- Сохраняет путь к драйверу мыши (`DeviceDriver.exe`)
- Ускоряет повторный запуск программы
- Позволяет быстро откатить изменения

Чтобы открыть папку TEMP (где хранится кэш):

<img src="https://github.com/user-attachments/assets/1bad9a28-585d-47e6-94fa-b7b247df1825" alt="Russifier DRK Screenshot" width="550"/>

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

## ☕ Чашка кофе

Если вам нравится эта программа и вы хотите поддержать разработчика, вы можете:

[![DonationAlerts](https://img.shields.io/badge/Donate-DonationAlerts-red?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTExLjY0NjIgNi42NDYyNUMxMS44NzUgNi40MTc1IDEyLjEyNSA2LjQxNzUgMTIuMzUzOCA2LjY0NjI1TDE3LjM1MzggMTEuNjQ2M0MxNy41NDYyIDExLjgzODcgMTcuNTQ2MiAxMi4xNjI1IDE3LjM1MzggMTIuMzU1TDEyLjM1MzggMTcuMzU1QzEyLjEyNSAxNy41ODM3IDExLjg3NSAxNy41ODM3IDExLjY0NjIgMTcuMzU1TDYuNjQ2MjUgMTIuMzU1QzYuNDUzNzUgMTIuMTYyNSA2LjQ1Mzc1IDExLjgzODcgNi42NDYyNSAxMS42NDYzTDExLjY0NjIgNi42NDYyNVoiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPg==)](https://www.donationalerts.com/r/saylont) 

[![Boosty](https://img.shields.io/badge/Donate-Boosty-8A2BE2?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDIyQzE3LjUyMjggMjIgMjIgMTcuNTIyOCAyMiAxMkMyMiA2LjQ3NzE1IDE3LjUyMjggMiAxMiAyQzYuNDc3MTUgMiAyIDYuNDc3MTUgMiAxMkMyIDE3LjUyMjggNi40NzcxNSAyMiAxMiAyMloiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik0xMiAxN0MxNC43NjE0IDE3IDE3IDE0Ljc2MTQgMTcgMTJDMTcgOS4yMzg1OCAxNC43NjE0IDcgMTIgN0M5LjIzODU4IDcgNyA5LjIzODU4IDcgMTJDNyAxNC43NjE0IDkuMjM4NTggMTcgMTIgMTdaIiBmaWxsPSI4QTJCRTIiLz4KPC9zdmc+)](https://boosty.to/saylontoff/donate) 

*Даже маленькая поддержка мотивирует на дальнейшее развитие проекта!*
