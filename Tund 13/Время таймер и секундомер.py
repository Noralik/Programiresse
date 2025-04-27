# import time
# 
# def sekundomer():
#     input("Нажмите Enter, чтобы начать секундомер.")
#     start_time = time.time()
#     try:
#         while True:
#             elapsed_time = time.time() - start_time
#             mins, secs = divmod(elapsed_time, 60)
#             hours, mins = divmod(mins, 60)
#             time_format = "{:02}:{:02}:{:02}".format(int(hours), int(mins), int(secs))
#             print(time_format, end="\r")
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("\nСекундомер остановлен.")
#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         mins, secs = divmod(elapsed_time, 60)
#         hours, mins = divmod(mins, 60)
#         time_format = "{:02}:{:02}:{:02}".format(int(hours), int(mins), int(secs))
#         print("Общее время: {}".format(time_format))
# 
# if __name__ == "__main__":
#     sekundomer()


import time

def timer(duration):
    print(f"Таймер установлен на {duration} секунд.")
    time.sleep(duration)
    print("Время вышло!")

if __name__ == "__main__":
    try:
        duration = int(input("Введите длительность таймера в секундах: "))
        timer(duration)
    except ValueError:
        print("Ошибка: Введите корректное число секунд.")
