#1 class defination is one time process
class A():
    #1. property/variable
    name=""
    #2. constructor/esp.function
    def __init__(self,n):
        self.name=n
        
        
        pass
    pass

class B(A):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class C(B):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class D(C):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class E(D):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class F(E):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class G(F):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class H(G):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class I(H):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class J(I):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class K(J):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class L(K):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class M(L):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class N(M):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class O(N):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class P(O):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class Q(P):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class R(Q):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class S(Q):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class T(S):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class U(T):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class V(U):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class W(V):
    #2.constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class X(W):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class Y(X):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass
class Z(Y):
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    pass

#2 create class external object is many time process
z1=Z("Vishal")
#we are going to access parent class property
print(f'My name is {z1.name}')