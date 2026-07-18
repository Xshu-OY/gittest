def car():
    while True:
        try:
            car_v = int(input("请输入一个整数表示车的速度："))
            break
        except ValueError:
            print("输入错误，请输入整数！")
    
    car_status = input("请输入一个字符表示车的行驶状态：")
    return car_v, car_status


def judge_threecars(max_v, min_distance, V):
    cars = []
    for i in range(3):
        cars.append(car())  # 依次按左中右的顺序输入车
    
    # 左车判断
    D = 1 if cars[0][1] == "R" else 0
    
    # 中车判断
    if cars[1][1] == "nomove" or cars[1][1] == "back":
        E = 1
    elif cars[1][1] == "front" and cars[1][0] > max_v:
        E = 1
    else:
        E = 0
    
    # 右车判断
    F = 1 if cars[2][1] == "L" else 0
    
    return D, E, F


def three_road(V):
    l, m, r = map(float, input('请输入3个浮点数表示距离3个车的长度：').split())
    
    if V == 0:
        max_v = 200
        min_distance = 300
    else:
        max_v = 100
        min_distance = 200
    
    return max_v, min_distance


def issafe():
    while True:
        try:
            a = int(input("请输入一个整数表示是否安全："))
            return a
        except ValueError:
            print("输入错误，请输入整数！")


def mycar():
    while True:
        try:
            vi = int(input("请输入一个整数表示自己的车的速度："))
            return vi
        except ValueError:
            print("输入错误，请输入整数！")


def israin():
    print("请输入10个整数表示下雨的概率：")
    while True:
        try:
            b = list(map(int, input().split()))
            if len(b) != 10:
                print("请输入10个整数！")
                continue
            break
        except ValueError:
            print("输入错误，请输入整数！")
    
    aver = sum(b) / 10
    return 1 if aver > 0.6 else 0


def main():
    A = issafe()
    R = israin()
    V = mycar()
    max_v, min_distance = three_road(V)
    D, E, F = judge_threecars(max_v, min_distance, V)
    
    Y = not A and D and E and F
    
    if Y:
        print("刹车")
    else:
        print("不刹车")


if __name__ == '__main__':
    main()