import math

while True:
    n1 = int(input('n1 = '))
    N1 = int(input('N1 = '))
    D1 = int(input('D1 = '))
    n2 = int(input('n2 = '))
    N2 = int(input('N2 = '))
    D2 = int(input('D2 = '))

    N = n1*n2*D1*D2 + N1*N2 + n2*N1*D2 + n1*N2*D1
    D = D1*D2
    G = math.gcd(N,D)

    NA = int(N/G)
    DA = int(D/G)
    
    n3 = int(NA/DA)
    N3 = int(NA%DA)
    D3 = DA

    if N3 == 0:
        print ('(n1 N1/D1)×(n2 N2/D2) =', NA)

    else:
         print('(n1 N1/D1)×(n2 N2/D2) =', str(NA)+'/'+str(DA),
          'or', n3, str(N3)+'/'+str(D3))
    
