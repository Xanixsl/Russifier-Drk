import json
import os
import sys
import ctypes
import time
import shutil
import psutil
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QTextEdit, QProgressBar, QMessageBox, QHBoxLayout,
    QSizePolicy, QGraphicsDropShadowEffect, QFrame, QSizeGrip,
    QSlider
)
from PyQt5.QtGui import (
    QIcon, QColor, QCursor, QFont,
    QPainter, QPixmap, QLinearGradient, QBrush,
    QPen, QImage
)
from PyQt5.QtCore import (
    Qt, QPropertyAnimation, QPoint,
    QRect, QEasingCurve, QParallelAnimationGroup,
    QSize, QTimer, QEvent
)
try:
    from PyQt5.QtWinExtras import QtWin
    HAS_WINEXTRAS = True
except ImportError:
    HAS_WINEXTRAS = False

os.environ.pop("QT_QUICK_BACKEND", None)
os.environ.pop("QT_QPA_PLATFORM", None)
os.environ.pop("QT_LOGGING_RULES", None)

class ModernTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFixedHeight(40)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 0, 10, 0)
        self.layout.setSpacing(10)
        
        self.title = QLabel("Russifier Drk 2.0")
        self.title.setStyleSheet("""
            color: white;
            font-size: 14px;
            font-weight: 600;
            font-family: Arial, sans-serif;
        """)
        
        self.about_btn = QPushButton("О программе")
        self.about_btn.setFixedSize(100, 28)
        self.about_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: white;
                border-radius: 4px;
                font-size: 12px;
                font-family: Arial, sans-serif;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.1);
            }
            QPushButton:pressed {
                background: rgba(255, 255, 255, 0.2);
            }
        """)
        self.about_btn.clicked.connect(self.parent.show_modern_description)
        
        self.spacer = QWidget()
        self.spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.minimize_btn = QPushButton("—")
        self.close_btn = QPushButton("✕")
        
        for btn in [self.minimize_btn, self.close_btn]:
            btn.setFixedSize(28, 28)
            btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    color: white;
                    border-radius: 7px;
                    font-size: 14px;
                    font-family: Arial, sans-serif;
                }
                QPushButton:hover {
                    background: rgba(255, 255, 255, 0.1);
                }
                QPushButton:pressed {
                    background: rgba(255, 255, 255, 0.2);
                }
            """)
        
        self.minimize_btn.clicked.connect(self.parent.showMinimized)
        self.close_btn.clicked.connect(self.parent.close)
        
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.about_btn)
        self.layout.addWidget(self.spacer)
        self.layout.addWidget(self.minimize_btn)
        self.layout.addWidget(self.close_btn)
        
        self.drag_pos = None
        self.drag_window_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos()
            self.drag_window_pos = self.parent.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_pos:
            new_pos = self.drag_window_pos + (event.globalPos() - self.drag_pos)
            self.parent.move(new_pos)
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.drag_pos = None
        self.drag_window_pos = None
        super().mouseReleaseEvent(event)

class GlassCard(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setStyleSheet("""
            background-color: rgba(30, 35, 40, 180);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        """)
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.shadow.setOffset(0, 3)
        self.setGraphicsEffect(self.shadow)

class ModernButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setMinimumHeight(42)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self._bg_color = QColor(0, 120, 215)
        self._text_color = QColor(255, 255, 255)
        
        self.shadow_effect = QGraphicsDropShadowEffect(self)
        self.shadow_effect.setBlurRadius(10)
        self.shadow_effect.setColor(QColor(0, 150, 255, 0))
        self.shadow_effect.setOffset(0, 2)
        self.setGraphicsEffect(self.shadow_effect)
        
        self.update_styles()
        
    def update_styles(self):
        style = f"""
        QPushButton {{
            background-color: {self._bg_color.name()};
            color: {self._text_color.name()};
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: 500;
            font-size: 12px;
            font-family: Arial, sans-serif;
            border: none;
            text-align: center;
        }}
        QPushButton:hover {{
            background-color: {self._bg_color.lighter(110).name()};
        }}
        QPushButton:pressed {{
            background-color: {self._bg_color.darker(120).name()};
        }}
        """
        self.setStyleSheet(style)
    
    def enterEvent(self, event):
        self._animate_button(QColor(0, 140, 255), QColor(0, 150, 255, 100))
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        self._animate_button(QColor(0, 120, 215), QColor(0, 150, 255, 0))
        super().leaveEvent(event)
    
    def _animate_button(self, bg_color, shadow_color):
        self._bg_color = bg_color
        self.shadow_effect.setColor(shadow_color)
        self.update_styles()

class ModernProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(8)
        self.setTextVisible(False)
        self.setRange(0, 100)
        self.setValue(0)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        
        bg_rect = QRect(0, 0, self.width(), self.height())
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(30, 35, 40))
        painter.drawRoundedRect(bg_rect, 4, 4)
        
        progress = int((self.value() / (self.maximum() - self.minimum())) * self.width())
        progress_rect = QRect(0, 0, progress, self.height())
        
        gradient = QLinearGradient(0, 0, progress, 0)
        gradient.setColorAt(0, QColor(0, 180, 255))
        gradient.setColorAt(1, QColor(0, 120, 215))
        
        painter.setBrush(QBrush(gradient))
        painter.drawRoundedRect(progress_rect, 4, 4)
        
        painter.setPen(QColor(255, 255, 255))
        painter.setFont(QFont("Arial", 8))
        text = f"{self.value()}%"
        text_rect = painter.fontMetrics().boundingRect(text)
        text_x = (self.width() - text_rect.width()) // 2
        text_y = (self.height() + text_rect.height()) // 2 - 2
        painter.drawText(text_x, text_y, text)

class AboutDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("О программе")
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(500, 520)
        
        self.background = QWidget(self)
        self.background.setGeometry(self.rect())
        self.background.setStyleSheet("""
            background-color: rgba(30, 35, 40, 220);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        """)
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setOffset(0, 3)
        self.setGraphicsEffect(shadow)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        
        title = QLabel("Russifier Drk v2.0")
        title.setStyleSheet("""
            color: #00b4ff;
            font-size: 20px;
            font-weight: 600;
            font-family: Arial, sans-serif;
        """)
        title.setAlignment(Qt.AlignCenter)
        
        subtitle = QLabel("АВТОМАТИЧЕСКИЙ ПЕРЕВОД ДРАЙВЕРОВ DARMOSHARK")
        subtitle.setStyleSheet("""
            color: white;
            font-size: 14px;
            font-family: Arial, sans-serif;
        """)
        subtitle.setAlignment(Qt.AlignCenter)
        
        version = QLabel("МОДЕЛИ M3/M3s/N3 | ВЕРСИИ 1.6.5 - 1.8.2.9")
        version.setStyleSheet("""
            color: #aaaaaa;
            font-size: 12px;
            font-family: Arial, sans-serif;
        """)
        version.setAlignment(Qt.AlignCenter)
        
        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        separator1.setStyleSheet("background: rgba(255,255,255,0.1);")
        
        info_text = QLabel("""
        <p style="font-size:13px; color:#ffffff; margin-bottom:8px; font-family:Arial,sans-serif;">
            <b>Russifier Drk</b> - программа для автоматического перевода<br>
             драйверов мыши Darmoshark на русский язык.              
        </p>
        <p style="font-size:13px; color:#ffffff; margin-bottom:8px; font-family:Arial,sans-serif;">
            ✔ Полностью автоматический процесс<br>
            ✔ Безопасность: файлы остаются на вашем ПК<br>
            ✔ Возможность отката к стандартным настройкам
        </p>
        <p style="font-size:13px; color:#ffffff; margin-bottom:8px; font-family:Arial,sans-serif;">
            <b>ВАЖНО:</b> Программа НЕ собирает и НЕ отправляет ваши данные!<br>
            Все файлы хранятся строго на вашем компьютере.
        </p>
        <p style="font-size:13px; color:#ffffff; margin-bottom:8px; font-family:Arial,sans-serif;">
            • ОБНОВЛЕНИЯ ДРАЙВЕРОВ: 
            <a href="https://docs.google.com/spreadsheets/d/1XSOc279P7e8JUpseJtwDvjeJQalX5SEadXpr1AYCQM0/edit?gid=0#gid=0" 
               style="color:#00b4ff; text-decoration:none;">
               Google Таблица
            </a>
        </p>
        <p style="font-size:13px; color:#ffffff; margin-bottom:8px; font-family:Arial,sans-serif;">
            • САЙТ РУСИФИКАТОРА: 
            <a href="https://russifier-drk.ru/" 
               style="color:#00b4ff; text-decoration:none;">
               russifier-drk.ru
            </a>
        </p>
        """)
        info_text.setOpenExternalLinks(True)
        
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)
        separator2.setStyleSheet("background: rgba(255,255,255,0.1);")
        
        dev_info = QLabel("""
        <p style="font-size:13px; color:#ffffff; margin-bottom:5px; font-family:Arial,sans-serif;">
            <b>РАЗРАБОТЧИК:</b> Saylont (Xanixsl на GitHub)
        </p>
        <p style="font-size:13px; color:#ffffff; margin-bottom:5px; font-family:Arial,sans-serif;">
            <b>ПОДДЕРЖКА РАЗРАБОТЧИКА:</b>
        </p>
        <p style="font-size:13px; color:#ffffff; margin-bottom:5px; font-family:Arial,sans-serif;">
            • <a href="https://www.donationalerts.com/r/saylont" 
               style="color:#00b4ff; text-decoration:none;">
               DonationAlerts
            </a>
        </p>
        <p style="font-size:13px; color:#ffffff; font-family:Arial,sans-serif;">
            • <a href="https://boosty.to/saylontoff/donate" 
               style="color:#00b4ff; text-decoration:none;">
               Boosty
            </a>
        </p>
        """)
        dev_info.setOpenExternalLinks(True)
        
        close_btn = QPushButton("Закрыть")
        close_btn.setMinimumHeight(40)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 120, 215, 150);
                color: white;
                border-radius: 8px;
                font-size: 14px;
                font-family: Arial, sans-serif;
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(0, 120, 215, 200);
            }
        """)
        close_btn.clicked.connect(self.close)
        
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(version)
        layout.addWidget(separator1)
        layout.addWidget(info_text)
        layout.addWidget(separator2)
        layout.addWidget(dev_info)
        layout.addStretch()
        layout.addWidget(close_btn)
        
        self.drag_pos = None
        self.drag_window_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos()
            self.drag_window_pos = self.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_pos:
            new_pos = self.drag_window_pos + (event.globalPos() - self.drag_pos)
            self.move(new_pos)
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.drag_pos = None
        self.drag_window_pos = None
        super().mouseReleaseEvent(event)

    def showEvent(self, event):
        if self.parent():
            self.move(
                self.parent().x() + (self.parent().width() - self.width()) // 2,
                self.parent().y() + (self.parent().height() - self.height()) // 2
            )
        super().showEvent(event)

class ModernRusificatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("ModernRusificator")
        self.initUI()
        self.setup_animations()
    
    def initUI(self):
        self.setWindowTitle('Russifier Drk 2.0')
        icon_path = self.resource_path('main.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        self.setFixedSize(800, 650)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Фоновый виджет
        self.background = QWidget(self)
        self.background.setGeometry(self.rect())
        self.background.setStyleSheet("background-color: rgba(30, 35, 40, 220);")
        
        # Основной макет
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Панель заголовка
        self.title_bar = ModernTitleBar(self)
        main_layout.addWidget(self.title_bar)
        
        # Виджет содержимого
        content_widget = QWidget()
        content_widget.setObjectName("contentWidget")
        content_widget.setStyleSheet("#contentWidget { background: transparent; }")
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 15, 20, 20)
        content_layout.setSpacing(15)
        
        # Карточка управления размытием
        blur_control = GlassCard()
        blur_layout = QHBoxLayout(blur_control)
        blur_layout.setContentsMargins(15, 8, 15, 8)
        
        blur_label = QLabel("Интенсивность размытия:")
        blur_label.setStyleSheet("color: white; font-size: 12px; font-family: Arial, sans-serif;")
        
        self.blur_slider = QSlider(Qt.Horizontal)
        self.blur_slider.setRange(0, 100)
        self.blur_slider.setValue(50)
        
        self.blur_value_label = QLabel("50")
        self.blur_value_label.setStyleSheet("color: white; font-size: 12px; font-family: Arial, sans-serif;")
        self.blur_value_label.setFixedWidth(30)
        
        # Стилизация слайдера
        self.blur_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                height: 4px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 2px;
            }
            QSlider::handle:horizontal {
                width: 14px;
                height: 14px;
                margin: -5px 0;
                background: #00b4ff;
                border-radius: 7px;
            }
            QSlider::sub-page:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00b4ff, stop:1 #0078d7);
                border-radius: 2px;
            }
        """)
        
        self.blur_slider.valueChanged.connect(self.update_blur_intensity)
        
        blur_layout.addWidget(blur_label)
        blur_layout.addWidget(self.blur_slider)
        blur_layout.addWidget(self.blur_value_label)
        content_layout.addWidget(blur_control)
        
        # Карточка статуса
        status_card = GlassCard()
        status_layout = QVBoxLayout(status_card)
        status_layout.setContentsMargins(15, 15, 15, 15)
        
        self.status_label = QLabel("Готов к русификации")
        self.status_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 16px;
                font-weight: 500;
                font-family: Arial, sans-serif;
            }
        """)
        status_layout.addWidget(self.status_label)
        
        self.progress_bar = ModernProgressBar()
        status_layout.addWidget(self.progress_bar)
        
        content_layout.addWidget(status_card)
        
        # Логи
        log_card = GlassCard()
        log_card.setMinimumHeight(180)
        log_layout = QVBoxLayout(log_card)
        log_layout.setContentsMargins(10, 10, 10, 10)
        
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setStyleSheet("""
            QTextEdit {
                background-color: rgba(20, 25, 30, 150);
                color: #e0e0e0;
                border-radius: 6px;
                border: 1px solid rgba(255, 255, 255, 0.05);
                padding: 8px;
                font-family: 'Consolas';
                font-size: 14px;
            }
        """)
        log_layout.addWidget(self.log)
        
        content_layout.addWidget(log_card)
        
        # Кнопки управления
        button_layout = QHBoxLayout()
        button_layout.setSpacing(12)
        
        self.start_button = ModernButton('НАЧАТЬ РУСИФИКАЦИЮ')
        self.start_button.setObjectName("startButton")
        self.start_button.clicked.connect(self.start_rusification)
        
        self.rollback_button = ModernButton('ОТКАТИТЬ ИЗМЕНЕНИЯ')
        self.rollback_button.setObjectName("rollbackButton")
        self.rollback_button.clicked.connect(self.rollback_changes)
        
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.rollback_button)
        content_layout.addLayout(button_layout)
        
        main_layout.addWidget(content_widget)
        
        # Эффекты
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.shadow.setOffset(0, 3)
        self.setGraphicsEffect(self.shadow)
        
        self.size_grip = QSizeGrip(self)
        self.size_grip.setStyleSheet("""
            QSizeGrip {
                width: 12px;
                height: 12px;
                background: transparent;
            }
        """)
    
    def update_blur_intensity(self, value):
        """Обновление интенсивности размытия фона"""
        self.blur_value_label.setText(str(value))
        alpha = 180 + int((value / 100) * 40)
        self.background.setStyleSheet(f"background-color: rgba(30, 35, 40, {alpha});")
        
        if HAS_WINEXTRAS:
            try:
                QtWin.enableBlurBehindWindow(self, region=self.background.rect(), enable=True)
            except:
                pass
    
    def setup_animations(self):
        self.status_anim = QPropertyAnimation(self.status_label, b"pos")
        self.status_anim.setDuration(1000)
        self.status_anim.setLoopCount(-1)
        self.status_anim.setEasingCurve(QEasingCurve.Linear)
        self.status_anim.setKeyValueAt(0, QPoint(self.status_label.x(), self.status_label.y()))
        self.status_anim.setKeyValueAt(0.5, QPoint(self.status_label.x(), self.status_label.y() - 1))
        self.status_anim.setKeyValueAt(1, QPoint(self.status_label.x(), self.status_label.y()))
        self.status_anim.start()
    
    def show_modern_description(self):
        self.about_dialog = AboutDialog(self)
        self.about_dialog.show()
    
    def clear_log(self):
        self.log.clear()
    
    def update_status(self, message):
        self.log.append(message)
        self.log.verticalScrollBar().setValue(self.log.verticalScrollBar().maximum())
        QApplication.processEvents()
    
    def start_rusification(self):
        self.clear_log()
        self.start_button.setEnabled(False)
        self.update_status('> ПОИСК ПРИЛОЖЕНИЯ...')
        self.simulate_long_task(1)
        self.progress_bar.setValue(20)
        
        driver_path = self.find_driver()
        if driver_path:
            self.update_status('> УСПЕШНО. ЗАКРЫТИЕ ПРИЛОЖЕНИЯ...')
            self.simulate_long_task(1)
            self.progress_bar.setValue(40)
            self.kill_process('DeviceDriver.exe')
            
            self.update_status('> ОБРАБОТКА ЯЗЫКОВЫХ ФАЙЛОВ...')
            self.simulate_long_task(1)
            self.progress_bar.setValue(60)
            self.process_language_files(driver_path)
            
            self.update_status('> ЗАПУСК ПРИЛОЖЕНИЯ...')
            self.simulate_long_task(1)
            self.progress_bar.setValue(80)
            self.run_driver(driver_path)
            
            self.update_status('> ПРОЦЕСС ЗАВЕРШЕН!')
            self.progress_bar.setValue(100)
        else:
            self.update_status('> ПРИЛОЖЕНИЕ НЕ НАЙДЕНО!')
        
        self.start_button.setEnabled(True)
    
    def rollback_changes(self):
        self.clear_log()
        self.rollback_button.setEnabled(False)
        self.update_status('> ОТКАТ ИЗМЕНЕНИЙ...')
        self.simulate_long_task(1)
        self.progress_bar.setValue(20)
        
        driver_path = self.find_driver()
        if driver_path:
            self.update_status('> УСПЕШНО. ЗАКРЫТИЕ ПРИЛОЖЕНИЯ...')
            self.simulate_long_task(1)
            self.progress_bar.setValue(40)
            self.kill_process('DeviceDriver.exe')
            
            self.update_status('> УДАЛЕНИЕ ФАЙЛОВ ПЕРЕВОДА...')
            self.simulate_long_task(1)
            self.progress_bar.setValue(60)
            self.rollback_language_files(driver_path)
            
            self.update_status('> ЗАПУСК ПРИЛОЖЕНИЯ...')
            self.simulate_long_task(1)
            self.progress_bar.setValue(80)
            self.run_driver(driver_path)
            
            self.update_status('> ОТКАТ ЗАВЕРШЕН!')
            self.progress_bar.setValue(100)
        else:
            self.update_status('> ПРИЛОЖЕНИЕ НЕ НАЙДЕНО!')
        
        self.rollback_button.setEnabled(True)
    
    def simulate_long_task(self, seconds):
        QApplication.processEvents()
        time.sleep(seconds)
    
    def find_driver(self):
        self.update_status('Загрузка кэшированных путей...')
        cached_paths = self.load_cached_paths()
        self.update_status(f'Кэшированные пути: {cached_paths}')
        for path in cached_paths:
            if os.path.exists(os.path.join(path, 'DeviceDriver.exe')):
                self.update_status(f'Найдено в кэше: {path}')
                return path
        
        drives = self.get_available_drives()
        self.update_status(f'Доступные диски: {drives}')
        for drive in drives:
            self.update_status(f'Поиск в {drive}')
            for root, dirs, files in os.walk(drive):
                if 'DeviceDriver.exe' in files:
                    self.update_status(f'Файл найден: {root}')
                    self.save_cached_path(root)
                    return root
        return None
    
    def get_available_drives(self):
        self.update_status('Получение списка доступных дисков...')
        drives = [f'{d}:\\' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f'{d}:\\')]
        self.update_status(f'Найдены диски: {drives}')
        return drives
    
    def load_cached_paths(self):
        temp_dir = os.getenv('TEMP')
        cache_file = os.path.join(temp_dir, 'rusificator_cache.json')
        self.update_status(f'Проверка существования файла кэша: {cache_file}')
        if os.path.exists(cache_file):
            self.update_status('Файл кэша найден. Загрузка...')
            try:
                with open(cache_file, 'r') as file:
                    paths = json.load(file)
                    if not isinstance(paths, list):
                        raise ValueError("Неверный формат данных в файле кэша")
                    self.update_status(f'Загружены пути из кэша: {paths}')
                    return paths
            except (json.JSONDecodeError, ValueError) as e:
                self.update_status(f'Ошибка чтения файла кэша: {e}')
                self.recreate_cache_file(cache_file)
        else:
            self.update_status('Файл кэша не найден.')
        return []
    
    def save_cached_path(self, path):
        self.update_status(f'Сохранение пути в кэш: {path}')
        temp_dir = os.getenv('TEMP')
        cache_file = os.path.join(temp_dir, 'rusificator_cache.json')
        cached_paths = self.load_cached_paths()
        if path not in cached_paths:
            cached_paths.append(path)
        try:
            with open(cache_file, 'w') as file:
                json.dump(cached_paths, file)
            self.update_status('Путь успешно сохранен.')
        except Exception as e:
            self.update_status(f'Ошибка сохранения пути: {e}')
    
    def recreate_cache_file(self, cache_file):
        self.update_status(f'Создание нового файла кэша: {cache_file}')
        try:
            with open(cache_file, 'w') as file:
                json.dump([], file)
            self.update_status('Файл кэша успешно создан.')
        except Exception as e:
            self.update_status(f'Ошибка создания файла кэша: {e}')
    
    def kill_process(self, process_name):
        self.update_status(f'Завершение процесса: {process_name}')
        try:
            for proc in psutil.process_iter():
                if proc.name() == process_name:
                    proc.terminate()
                    self.update_status(f'Процесс {process_name} успешно завершен.')
                    proc.wait()
        except Exception as e:
            self.update_status(f'Ошибка завершения процесса {process_name}: {e}')
    
    def process_language_files(self, driver_path):
        self.update_status(f'Обработка файлов в {driver_path}')
        language_path = os.path.join(driver_path, 'language')
        self.update_status(f'Проверка директории: {language_path}')
        os.makedirs(language_path, exist_ok=True)
        lan_files = ['1033.lan']
        self.update_status('Чтение библиотек...')
        
        if getattr(sys, 'frozen', False):
            lib_path = os.path.join(sys._MEIPASS, 'lib.lib')
        else:
            lib_path = 'lib.lib'
        
        if not os.path.exists(lib_path):
            self.update_status(f'ОШИБКА: Файл библиотеки не найден: {lib_path}')
            self.update_status('Пожалуйста, убедитесь что файл lib.lib находится в той же папке что и программа')
            return
        
        try:
            with open(lib_path, 'r', encoding='utf-16') as lib_file:
                content = lib_file.read()
                self.update_status('Библиотека успешно прочитана.')
        except UnicodeDecodeError:
            self.update_status('Ошибка чтения библиотеки. x0001')
            return
        
        for lan_file in lan_files:
            file_path = os.path.join(language_path, lan_file)
            try:
                with open(file_path, 'w', encoding='utf-16') as file:
                    file.write(content)
                    self.update_status(f'Файл записан: {file_path}')
            except PermissionError:
                self.update_status(f'Нет доступа для изменения: {lan_file}')
                return
    
    def rollback_language_files(self, driver_path):
        self.update_status(f'Откат изменений в {driver_path}')
        language_path = os.path.join(driver_path, 'language')
        self.update_status(f'Проверка директории: {language_path}')
        if not os.path.exists(language_path):
            self.update_status('Директория не существует.')
            return
        
        translation_files = []
        for root, _, files in os.walk(language_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-16') as f:
                        if any(char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' for char in f.read()):
                            translation_files.append(file_path)
                except UnicodeDecodeError:
                    continue
        
        if translation_files:
            self.update_status(f'Обнаружен перевод в файлах: {translation_files}')
            for file in translation_files:
                os.remove(file)
                self.update_status(f'Файл удален: {file}')
        
        main_dir = os.path.dirname(os.path.abspath(__file__))
        lan_files = ['1033.lan']
        
        for lan_file in lan_files:
            src = os.path.join(main_dir, lan_file)
            dst = os.path.join(language_path, lan_file)
            if os.path.exists(src):
                shutil.copy(src, dst)
                self.update_status(f'Файл скопирован: {dst}')
            else:
                self.update_status(f'Файл не найден: {src}')
    
    def run_driver(self, driver_path):
        self.update_status(f'Запуск приложения: {driver_path}')
        try:
            os.startfile(os.path.join(driver_path, 'DeviceDriver.exe'))
            self.update_status('Приложение успешно запущено.')
        except Exception as e:
            self.update_status(f'Ошибка запуска приложения: {e}')
    
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    def resizeEvent(self, event):
        self.background.setGeometry(self.rect())
        self.size_grip.move(self.width() - 16, self.height() - 16)
        super().resizeEvent(event)

def main():
    try:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, ' '.join(sys.argv), None, 1
            )
            return

        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
        
        app = QApplication(sys.argv)
        app.setStyle('Fusion')
        
        font = QFont("Arial", 9)
        app.setFont(font)
        
        app.setStyleSheet("""
            QToolTip {
                background-color: rgba(30, 35, 40, 220);
                color: white;
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 4px;
                padding: 4px;
            }
        """)
        
        rus_app = ModernRusificatorApp()
        rus_app.show()
        
        sys.exit(app.exec_())
        
    except Exception as e:
        print(f"Критическая ошибка: {str(e)}")
        input("Нажмите Enter для выхода...")

if __name__ == "__main__":
    main()
