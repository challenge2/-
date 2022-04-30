password = 'a123456'

i = 0
j = 2
while i < 3:
    password_guess = input('最多輸入3次密碼: ')
    if password_guess != password:
        print('密碼錯誤！ 還有{}次機會'.format(j))
        j -= 1
        i += 1
    elif password_guess == password:
        print('登入成功！')
        break
    else:
        break
