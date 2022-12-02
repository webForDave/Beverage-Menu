q=("a")
g=("x")
v=0
b=0
k=0
z=0
print("T For Tea")
print("C For Coffee")
print("S For Shakes")
print("H For Hot Chocolate")
print("X To End Order")
while q!=g:
    x=str(input("Whats Your Order ? ")).upper()
    y=int(input("Quantity ? "))
    if x==("T"):
        z=6*y
    elif x==("C"):
        v=12*y
    elif x==("S"):
        b=9*y
    elif x==("H"):
        k=10*y
    else:
        print("N/A")
    q=input(str("Anything Else ? ")).lower()
n=z+v+b+k
print("Total Price:",n)
    
    

