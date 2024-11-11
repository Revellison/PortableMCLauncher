import os
import logging
import minecraft_launcher_lib

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("download_launcher.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    # Определение пути для загрузки версий
    base_path = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.join(base_path, "game")

    # Создание папки для версий, если она отсутствует
    if not os.path.exists(download_path):
        os.makedirs(download_path)
        logger.info("Создана папка для загрузки версий Minecraft: %s", download_path)

    # Ввод версии для загрузки
    version = input("Введите версию Minecraft, которую хотите скачать: ")
    logger.info("Пользователь выбрал версию для загрузки: %s", version)

    # Путь к папке версии
    version_path = os.path.join(download_path, "versions", version)

    # Проверка, была ли версия уже загружена (наличие нужных файлов)
    if not os.path.exists(version_path):
        logger.info("Версия %s не найдена. Начинается загрузка...", version)
        print(f"Версия {version} не найдена. Начинается загрузка...")
        try:
            # Загрузка указанной версии Minecraft
            minecraft_launcher_lib.install.install_minecraft_version(version, download_path)
            logger.info("Версия %s успешно загружена в %s", version, download_path)
            print(f"Версия {version} успешно загружена в {download_path}.")
        except Exception as e:
            logger.error("Ошибка при загрузке версии %s: %s", version, e)
            print(f"Ошибка при загрузке версии {version}: {e}")
    else:
        logger.info("Версия %s уже загружена.", version)
        print(f"Версия {version} уже загружена.")

if __name__ == "__main__":
    main()
