if __name__ == '__main__':
   s = input()
   '''
    al = True if s.isalnum() else False
    print(al)
    a = True if s.isalpha() else False
    print(a)
    d = True if s.isdigit() else False
    print(d)
    l = True if s.islower() else False
    print(l)
    u = True if s.isupper() else False
    print(u)''' 
    
print(any(a.isalnum() for a in s))
print(any(a.isalpha() for a in s))
print(any(a.isdigit() for a in s))
print(any(a.islower() for a in s))
print(any(a.isupper() for a in s))
