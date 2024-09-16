def product_of_odd_digits_v2(n):
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit > 1:  # Change here: consider digits greater than 1 as odd digits
            product = product * int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product