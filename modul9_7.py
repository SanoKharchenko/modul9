
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, result // 2 + 1):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper


@is_prime
def sum_three(n1, n2, n3):
    sum_ = n1 + n2 + n3
    return sum_


if __name__ == "__main__":
    result = sum_three(2, 3, 6)
    print(result)
