from typing import List


def check(count: int) -> int:
    with open("Numbers.txt") as file:
        for line in file:
            data: List[int] = list(map(int, line.split()))
            for i in range(len(data)):
                if data[i] % 2 == 0:
                    count += 1
        return count


if __name__ == "__main__":
    num = 0
    print(check(num))
