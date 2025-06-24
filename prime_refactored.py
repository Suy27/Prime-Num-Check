def is_prime(number: int) -> bool:
    """
    Check if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
        return True

def main():
    try:
        number = int(input("Enter a number to check if it's prime: "))
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")