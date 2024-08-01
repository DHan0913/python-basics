# Operator
# 기본적으로 하나의 py 파일은 그 자체가 모듈
def arith_oper():
    print("======= 산술 연산")
    print(7/3) # 파이썬 3 -> int / int -> float
    print(7//3) # 정수 나눗셈의 몫 연산자 //
    print(7%3) # 정수 나눗셈의 나머지 연산자

    # 나눗셈의 몫과 나머지 동시에 구함
    print(divmod(7, 3)) # -> (2, 1) : Tuple

    print("7/3의 몫:", divmod(7, 3)[0])
    print("7/3의 나머지:", divmod(7, 3)[1])

    print(7**3) # 지수승: 7의 3제곱
    print(pow(7, 3)) # 지수 함수: 7의 3제곱

def rel_oper():
    # pass # 함수 구현부 없어도 비워두면 안됩니다.

    print("===== 비교 연산자")

    s1 = "python"; s2 ="python"
    print("문자열의 비교:", s1 == s2)

    # 복합 관계식
    a = 6
    # a가 0 ~ 10 사이의 값?
    #      조건 1: a > 0
    #      조건 2: a < 10
    print(0 < a and a < 10)
    print(0 < a < 10)

    # 다양한 자료 구조의 대소 비교
    print("문자열의 대소:", "abcd" > "abd")
    print("튜플의 대소:", (1, 2, 3) > (1, 3, 4))

    # 동질성의 비교 ==, 동일성의 비교 is
    a = 10; b = 20; c = a
    print("a == b ?", a == b)
    print("a is b? ", a is b)
    print("a == c", a == c)
    print("a is b ?", a is c)




if __name__ == "__main__":
    # 다른 모듈로 import 되는 경우 __name__ == "python_basics"
    # 직접 실행될 경우(최상위 모듈일 경우) __name__ == "__main__"
    # arith_oper()
    rel_oper() # 비교 연산자 연습
