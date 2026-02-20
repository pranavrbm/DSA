def count_bits(x):
    num_bits= 0
    while x:
        print("x:",x)
        num_bits += x&1
        print("num bits :",num_bits)
        x >>=1
        print("x after :",x)
    return num_bits
print(count_bits(5))
