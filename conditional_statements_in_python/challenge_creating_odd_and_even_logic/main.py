# Initial variables and values
num = 8941 % 931
result = 'blank'

# Determine whether the number is odd or even
if num%2!=0:
    result = 'odd'
else:
    result = 'even'

# Testing
print("The number num is", result)