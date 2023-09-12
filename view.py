def loadPrime(file):
    data = open(file, "r")
    primes_s = data.read().split(" ")

    data.close()

    return primes_s

primes = loadPrime("primes/prime.txt")
message = "몇 번째 소수가 궁금하십니까? (소수: %d개) " % len(primes)

while True:
    i = int(input(message))
    
    if i > 0 and i <= len(primes):
        print("%d번째 소수는 '%s'입니다." % (i, primes[i-1]))
    else:
        break
