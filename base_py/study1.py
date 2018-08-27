def yieldmemo():
    i = range(3,0,-1)
    yield 1; yield 0.1; yield "a"; yield 1+2; yield i

def num(max):
    num = 2
    while (num <= max):
        prime = True
        for i in range(2, num):
            if (num % i) == 0:
                prime = False
                break
        if (prime):
            yield num
        num += 1
            
if __name__ == '__main__':
    it = yieldmemo()
    for i in it:
        print(i, type(i))
        
    l = num(100)
    print(type(l))
    for k in l:
        print(k, end=",")
    else:
        print()