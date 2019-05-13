
if __name__ == '__main__':
    c = raw_input()
    print any(s.isalnum()  for s in c)
    print any(s.isalpha() for s in c)
    print any(s.isdigit() for s in c)
    print any(s.islower() for s in c)
    print any(s.isupper() for s in c)