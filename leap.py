YEAR = int(input())
if (( YEAR%400 == 0)or (( YEAR%4 == 0 ) and ( YEAR%100 != 0))):
    print("yes")
else:
    print("no")
