import os
import minecraft_launcher_lib
import subprocess

def main():
    # Ввод псевдонима игрока
    playernickname = input("Nickname$ ")

    # Определение пути к папке с игрой
    base_path = os.path.dirname(os.path.abspath(__file__))
    game_path = os.path.join(base_path, "game")

    # Проверка существования папки с игрой
    if not os.path.exists(game_path):
        print("Папка с файлами игры не найдена.")
        return

    # Ввод версии для запуска
    version = input("Введите версию: ")

    # Проверка, доступна ли версия Minecraft
    if not minecraft_launcher_lib.utils.is_version_valid(version, game_path):
        print(f"Версия {version} не установлена. Начинается установка...")
        try:
            minecraft_launcher_lib.install.install_minecraft_version(version, game_path)
        except Exception as e:
            print(f"Ошибка при установке версии {version}: {e}")
            return
    else:
        print(f"Версия {version} найдена.")

    # Настройка параметров запуска Minecraft
    options = minecraft_launcher_lib.utils.generate_test_options()
    options["username"] = playernickname  # Псевдоним игрока
    options["uuid"] = "0-0-0-0-0"         # UUID
    options["token"] = ""                 # Пустой токен для оффлайн-режима

    # Получение команды для запуска Minecraft
    try:
        command = minecraft_launcher_lib.command.get_minecraft_command(version, game_path, options)
    except Exception as e:
        print(f"Ошибка при получении команды запуска: {e}")
        return

    # Запуск игры
    print("Запуск Minecraft...")
    try:
        subprocess.run(command)
    except Exception as e:
        print(f"Ошибка при запуске Minecraft: {e}")

if __name__ == "__main__":
    main()