from collections import deque


def define_simetry(expession):
    pattern = ["(", "[", "{", "}", "]", ")"]
    counter = {}
    is_simetry = "Симетрично"
    i = 0
    for el in pattern:
        if expession.count(el) != 0:
            counter[el] = expession.count(el)

    values = list(val for val in counter.values())
    print("keys: ", counter.keys())
    print("values: ", values)

    if len(counter.keys()) == 0:
        is_simetry = "Несиметрично"
        return is_simetry

    while i != len(values)//2:
        if values[i] != values[-(i+1)]:
            is_simetry = "Несиметрично"
            break
        i += 1

    return is_simetry


def main():
    input_string = input("Введить послідовність: ")
    print(input_string, ":", define_simetry(input_string))


if __name__ == "__main__":
    main()
