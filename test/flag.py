from enum import Flag

class AFlag(Flag):
    N = 0
    R = 1
    W = 2
    X = 4

flag = AFlag.N
flag |= AFlag.R
print(flag)
print(AFlag.R in flag)
print(AFlag(3))
print(AFlag(3) == AFlag.R | AFlag.W)
print(AFlag(3) is AFlag.R | AFlag.W)
print(flag is AFlag.R)
print(flag)
print(f'{flag.value} {type(flag.value)}')

a = AFlag(3)
print(type(a))
print(a.value)
print(type(AFlag.R | AFlag.X))
print(a & AFlag.X)
