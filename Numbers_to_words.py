# ko dùng def, dict,... chỉ dùng if
# nhập số
a = int(input("nhập số: "))
num = str(a)
length = len(num)
Normal_a = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

# các số từ 0 đến 9
if length == 1:
    word = Normal_a[a]
    print(word)

# các số có 2 chữ số
elif length == 2:
    if num[-2] == '1':
        # 10
        if num[-1] == '0':
            word = 'mười'
        # 11, 12, 13, 14, 16, 17, 18, 19
        elif num[-1] != '0' and num[-1] != '5':
            word = 'mười' + ' ' + Normal_a[int(num[1])]
        # 15
        elif num[-1] == '5':
            word = 'mười' + ' lăm'
    elif num[-2] != '1':
        # x0
        if num[-1] == '0':
            word = Normal_a[int(num[0])] + ' mươi'
        # x1
        elif num[-1] == '1':
            word = Normal_a[int(num[0])] + ' mươi' + ' mốt'
        # x5
        elif num[-1] == '5':
            word = Normal_a[int(num[-2])] + ' mươi' + ' lăm'
        else:
            word = Normal_a[int(num[-2])] + ' mươi ' + Normal_a[int(num[-1])]
    print(word)
# số có 3 chữ số
elif length == 3:
    # x0x
    if num[-2] == '0':
        # x00
        if num[-1] == '0':
            word = Normal_a[int(num[-3])] + ' trăm'
        # x0x
        elif num[-1] != '0':
            word = Normal_a[int(num[-3])] + ' trăm' + ' linh ' + Normal_a[int(num[-1])]
    # x(x!=0)x
    else:
        # xx0
        if num[-1] == '0':
            if num[-2] == '1':
                word = Normal_a[int(num[-3])] + ' trăm ' + 'mười'
            if num[-2] != '1':
                word = Normal_a[int(num[-3])] + ' trăm ' + Normal_a[int(num[-2])] + ' mươi'
        # xxx
        else:
            # x1x
            if num[-2] == '1':
                # 11, 12, 13, 14, 16, 17, 18, 19
                if num[-1] != '0' and num[-1] != '5':
                    word = Normal_a[int(num[-3])] + ' mười ' + Normal_a[int(num[1])]
                # 15
                elif num[-1] == '5':
                    word = Normal_a[int(num[-3])] + ' trăm' + ' mười' + ' lăm'
            elif num[-2] != '1':
                # x0
                if num[-1] == '0':
                    word = Normal_a[int(num[-3])] + 'trăm ' + Normal_a[int(num[-1])] + ' mươi'
                # x1
                elif num[-1] == '1':
                    word = Normal_a[int(num[-3])] + 'trăm ' + Normal_a[int(num[-1])] + ' mươi' + ' mốt'
                # x5
                elif num[-1] == '5':
                    word = Normal_a[int(num[-3])] + ' trăm ' + Normal_a[int(num[-2])] + ' mươi' + ' lăm'
                else:
                    word = Normal_a[int(num[-3])] + ' trăm ' + Normal_a[int(num[-2])] + ' mươi ' + Normal_a[int(num[-1])]
    print(word)