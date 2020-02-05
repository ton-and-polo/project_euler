"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# Max three digit
x = 999
y = x

max_two_digit = 99

combinations = True
palindromic_list = []  # Initial list


while combinations:

    product = x * y

    left = str(product)[:(len(str(product))//2)]
    right = str(product)[(len(str(product))//2):]

    palindromic = True

    for i in range((len(left)-1), -1, -1):
        # Comparing elements:
        # e.g. left[-1] right[1]
        if left[i] != right[(len(left) - 1) - i]:
            palindromic = False
            break

    if palindromic:
        palindromic_list.append(product)

        if len(palindromic_list) == 10:  # An average list length to evaluate max palindromic
            print(max(palindromic_list))
            combinations = False

    y -= 1

    if y == max_two_digit:
        x -= 1
        y = x

    if y == max_two_digit:
        combinations = False


# 2st solution:

product = 786687  # Which is a product x and y
left = int(str(product)[:(len(str(product)) // 2)])
right = str(product)[(len(str(product)) // 2):]

new_right = ''

for i in range((len(right) - 1), -1, -1):
    new_right += right[i]

right = int(new_right)

if left == right:
    palindromic_list.append(product)
