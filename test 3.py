#third test case

def expo(x,y):
    return x**y
if __name__ =="__main__":
    if expo(2,3)==8 and expo(4,10)==1048576:
        print ("test successful")
    else:
        print("test failure")
