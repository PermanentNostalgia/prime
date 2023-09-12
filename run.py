def loadPrime(file):
    data = open(file, "r")
    primes_s = data.read().split(" ")
    primes = []

    for x in primes_s:
        primes.append(int(x))

    data.close()
    
    return primes

def savePrime(file, primes, begin):
    data = open(file, "a")

    for i in range(begin, len(primes)):
        data.write(" "+str(primes[i]))

    data.close()

#prime.txt 수정하지 말아주세요.
file = "primes/prime.txt"
primes = loadPrime(file)
origin_len = len(primes)

number = primes[-1] + 2
p_count = len(primes)
MAX = int(input("몇 번째 소수까지 구하고 싶으십니까? (현재 소수 개수: %d) " % origin_len))

while p_count < MAX:
    p_flag = True
    
    for p in primes:
        if number % p == 0: #지금 현제 number가 합성수이면
            p_flag = False
            break
        
    if p_flag:
        primes.append(number)
        p_count += 1
    
    number += 2

savePrime(file, primes, origin_len)
