import time
import os

def clear_screen():
    """Очищає екран консолі."""
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(total_seconds):
    """Форматує час у вигляді DD:HH:MM:SS."""
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}"

def countdown():
    """Запускає зворотний відлік з введенням користувача."""
    try:
        # Запитуємо тривалість у днях, годинах, хвилинах, секундах
        print("Введіть тривалість відліку:")
        days = int(input("Дні (0 або більше): "))
        hours = int(input("Години (0-23): "))
        minutes = int(input("Хвилини (0-59): "))
        seconds = int(input("Секунди (0-59): "))

        # Перевірка коректності введення
        if days < 0 or hours < 0 or minutes < 0 or seconds < 0:
            print("Значення не можуть бути від'ємними!")
            return
        if hours > 23 or minutes > 59 or seconds > 59:
            print("Години мають бути 0-23, хвилини та секунди 0-59!")
            return

        # Переводимо все в секунди
        total_seconds = days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds

        if total_seconds == 0:
            print("Тривалість має бути більше 0!")
            return

        clear_screen()
        print("Зворотний відлік почався!")

        # Зворотний відлік
        for remaining in range(total_seconds, -1, -1):
            clear_screen()
            print(f"Залишилося: {format_time(remaining)}")
            time.sleep(1)

        # Повідомлення після завершення
        clear_screen()
        print("Час вийшов!")

    except ValueError:
        print("Будь ласка, введіть цілі числа!")

if __name__ == "__main__":
    countdown()
