def even_numbers(n):
    for number in range(2,n+1,2):
        yield number
        
zarf = even_numbers(20)
print(next(zarf))

print(next(zarf))

print(next(zarf))
