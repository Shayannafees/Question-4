# Q#4
#Discrete Logic HW#4
#Muhammad Shayan Nafees


# A Function to check if a number is composite or not
def isComposite(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False

# Check if k^2 + 2k + 1 is composite for every integer k > 0
def theorem_Validity(k):
    expression = k**2 + 2*k + 1
    return isComposite(expression)

# Verify the theorem for a range of k values, for example from 1 to 20
for k in range(1, 21):
    print(f"For k = {k}, k^2 + 2k + 1 is composite: {theorem_Validity(k)}")



'''Output: 
For k = 1, k^2 + 2k + 1 is composite: True
For k = 2, k^2 + 2k + 1 is composite: True
For k = 3, k^2 + 2k + 1 is composite: True
For k = 4, k^2 + 2k + 1 is composite: True
For k = 5, k^2 + 2k + 1 is composite: True
For k = 6, k^2 + 2k + 1 is composite: True
For k = 7, k^2 + 2k + 1 is composite: True
For k = 8, k^2 + 2k + 1 is composite: True
For k = 9, k^2 + 2k + 1 is composite: True
For k = 10, k^2 + 2k + 1 is composite: True
For k = 11, k^2 + 2k + 1 is composite: True
For k = 12, k^2 + 2k + 1 is composite: True
For k = 13, k^2 + 2k + 1 is composite: True
For k = 14, k^2 + 2k + 1 is composite: True
For k = 15, k^2 + 2k + 1 is composite: True
For k = 16, k^2 + 2k + 1 is composite: True
For k = 17, k^2 + 2k + 1 is composite: True
For k = 18, k^2 + 2k + 1 is composite: True
For k = 19, k^2 + 2k + 1 is composite: True
For k = 20, k^2 + 2k + 1 is composite: True'''