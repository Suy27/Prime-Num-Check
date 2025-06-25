def is_prime(number: int) -> bool:
    """
    Check if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if number is prime, False otherwise.
    """
    # Prime numbers are greater than 1
    if number <= 1:
        return False
        
    # Only check for divisibility up to the square root of the number
    # If a number is divisible by any number in this range, it is not prime
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
            
    # If no divisors found, the number is prime
    return True

def main():
    """
    Handle user input and display the result.
    Wrapped in a try-except block to catch invalid inputs.
    """
    try:
        # Prompt User for Input
        number = int(input("Enter a number to check if it's prime: "))
        
        # Use the is_prime function to evaluate and print result
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        # Handle non-integer inputs gracefully
        print("Invalid input. Please enter an integer.")

# Entry point guard ensures main() runs only when script is executed directly
if __name__ == "__main__":
    main()
