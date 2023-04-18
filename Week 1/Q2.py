def sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i*i

    return result


print(sum_of_squares(n=2))
# +1 cuz end number not included
