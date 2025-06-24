# Day 4 Challenge: Check if a number is prime
num = int(input("Please enter a number:"))

# Prime numbers are greater than 1
if num <= 1:   # This checks if num is greater or equals to 1 then not a prime number
    print("Not a prime number")
else:
    for n in range(2, int(num ** 0.5) +1):  # This loops checks all the number 'n' starting from 2 up to the square root of num
                                            # + 1 We add this because range (a, b) it goes upto but does not include 'b'.
# Why up to square root? > Because if a number has a factor, it will show up before or at the square root.
# Thus, we dont need to check all the way upto num-1
        if num % n == 0: # Means num is divisible by n, then it's not a prime number
            print(f"{num} is not a prime number (divisible by {n})")
            break # Then it will stop checking with break if num is divisible
    else: 
        print(f"{num} is a prime number") # Means in the whole loop there is no number found that divides 'num'
                                          # Then it's a prime number.
    # This else belongs to the 'for' loop, not the if statement.