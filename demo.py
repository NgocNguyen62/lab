a = int(input("Nhập vào a: "))
b = int(input("nhập vào b: "))
c = int(input("Nhập c: "))
if a == 0 :
    if (c == 0):
        if(b == 0):
            print("Vô só nghiệm")
        else:
            print("Vô nghiệm")
    else:
        print("Phương trình có 1 nghiệm: ", -c/b)
else:
    delta = b*b - 4*a*c
    print(delta)