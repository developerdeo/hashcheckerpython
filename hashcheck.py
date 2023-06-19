x='0'
y=0
while x=='0':     
    ONE=input("Enter the HASH 1 to be compared: ")
    
    while y==0:
        any=input("\nUse power GET-FILEHASH then the name of the file, compare with\nthe one on the website\n\n        press Enter to continue")
        y +=1
    TWO=input("\nEnter the HASH 2 to be compared: ")
    if ONE==TWO:
        print("\n\tThe File hash matches")
        y=input()
    else:
        print("\n\tThey don't match")
        y=input()
    
    x=input("If you wish to continue press (0), \nif you wish to end press any value: ")
    
        




