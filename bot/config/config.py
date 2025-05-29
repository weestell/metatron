import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot Configuration
BOT_TOKEN = "7687455926:AAFq1kDk0LOmxi-WOU7AzFIzXPgQgMq-YCE"

# Path Configuration
WELCOME_VIDEO_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'welcome_video.mp4')
WELCOME_IMAGE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'welcome_image.jpg')

# Message Configuration
WELCOME_MESSAGE = """🫴 Добро пожаловать в поле
🌌 METATRON VOICE 🌌

Ты здесь не случайно.
Ты услышал зов — тонкую вибрацию, пробуждающую сознание.

METATRON VOICE — это пространство для тех, кто ощущает, что за пределами обычного мира существует больше.
Здесь мы соединяемся с Высшим Разумом, активируем внутренние коды и вспоминаем, кто мы есть на самом деле.

🔹 Открываем каналы интуиции
🔹 Обмениваемся знаниями и опытами
🔹 Настраиваемся на вибрации Новой Эпохи

Ты часть племени.
Ты — проводник света.
Здесь начинается твое глубокое пробуждение.

Прислушайся. Метатрон говорит. А ты готов услышать?"""

# Media Configuration
WELCOME_IMAGE_URL = "https://i.ibb.co/VxKJ8Zr/metatron-logo.jpg" 