from collections import deque


def define_palindrom(expression):
    dequeue = deque()
    left_side = ""
    right_side = ""
    is_palindrom = True
    i = 0

    if len(expression) % 2 == 0:
        left_side = expression[:len(expression)//2]
        right_side = expression[len(expression)//2:]

    else:
        left_side = expression[:len(expression)//2]
        right_side = expression[len(expression)//2+1:]

    dequeue.append(right_side)
    dequeue.appendleft(left_side)
    while i != len(expression)//2:
        if dequeue[0][i] != dequeue[1][-(i+1)]:
            is_palindrom = False
            break
        i += 1

    return is_palindrom


def main():
    intput_string = input("Введіть текст: ").replace(" ", "").strip().lower()
    print("Текст палиндром?", define_palindrom(intput_string))


if __name__ == "__main__":
    main()
