password = 'a123456'

i = 3 # 剩餘機會

while i > 0:
    i -= 1
    password_guess = input('請輸入密碼: ')
    if password_guess == password:
        print('登入成功！')
        break

    else :
        print('密碼錯誤！' )
        if i > 0:
            print('還有',i, '次機會')

