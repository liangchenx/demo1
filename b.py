#猜数字游戏
while True:
    input1 = input("请输入您的答案：")
    if input1 == 'quit':
        break
    else:
        number = int(input1)
        if number == 444:
            print("这都能猜到，你真棒！")
            break
        else:
            print("不对哦，再试试吧！")
            continue