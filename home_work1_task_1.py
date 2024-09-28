from queue import Queue
import random
from time import sleep as sleep
import string
import keyboard

# Емітація заявок
class Blank:
    def __init__(self, name, description):
        self.name = name
        self.description = description


# Черга заявок
queue = Queue()

# Нова заявка, яка додається до черги
def generate_request(id):
    blank = Blank(f"Заявка №{id}", body_request())
    queue.put(blank)

# Оброботка заявок
def process_request():
    if not queue.empty():
        queue.queue[-1] = "Заяка закрита"
        queue.get()
        print("Не закрито заяв:", queue.qsize())

    if queue.empty():
        print("Черга пуста!")

# Емітація інформації для заявки - випадкова набір букв в 4 строки
def body_request():
    description = []
    description.append(''.join(random.choice(string.ascii_lowercase)
                               for i in range(20)))
    description.append(''.join(random.choice(string.ascii_lowercase)
                               for i in range(20)))
    description.append(''.join(random.choice(string.ascii_lowercase)
                               for i in range(20)))
    description.append(''.join(random.choice(string.ascii_lowercase)
                               for i in range(20)))
    return description


def main():
    while True:
        # випадкова генерація заявок
        for i in range(1, random.randint(1, 20), random.randint(1, 5)):
            generate_request(i)

        print(f"Кількість заяв: {queue.qsize()}")
        sleep(2)
        # обов'зкове закриття заявок
        print("Обробка та закриття заяв:")
        while not queue.empty():
            process_request()
            sleep(1)

        print("Натиснить будь-яку клавишу для продовження ")
        print("Натиснить 'space' для виходу з програми")
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == "space":
            break
        else:
            continue


if __name__ == "__main__":
    main()
