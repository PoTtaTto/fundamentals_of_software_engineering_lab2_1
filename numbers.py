def ask_user_numbers():
    print('Enter 4 non-null numbers splitted by space:')
    nums = [int(num) for num in input().split()]
    sum1, sum2 = nums[0] + nums[1], nums[2] + nums[3]
    print(f'Sum of first elements: {sum1}\nSum of last elements: '
          f'{sum2}\nDivided sums: {round(sum1 / sum2, 2)}')