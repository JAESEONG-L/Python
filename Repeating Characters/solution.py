p= int(input())

for i in range(p):
    input_list= input().split()


    if len(input_list)!=2:
        print("INVALID INPUT.")

        break

    r= int(input_list[0])

    s= input_list[1]

    t= ""


    for char in s:
        t += char * r

    print(t)
