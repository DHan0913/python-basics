# Operator
# 기본적으로 하나의 py 파일은 그 자체가 모듈
from sympy.codegen.cnodes import union


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

import keyword # import 키워드 -> 모듈을 불러오는 명령어
def var_ex():
    print("====== 변수")
    # 문자, 숫자, _의 조합
    # 숫자로 시작하면 안됨
    # 파일명도 변수 명명 규칙에 맞춰 줘야 한다
    print("예약어 목록:", keyword.kwlist)
    print("예약어 개수:", len(keyword.kwlist))

def assignment_ex():
    print("==== 치환문")
    # 변수 선언 절차 없다
    print("namespace:", dir())
    a = 2024 # 첫 번째 할당이 발생할 때 namespace에 추가
    b = a + 1
    print(a, b)
    print("namespace:", dir())

    # 여러 변수를 한꺼번에 할당
    c, d = 3.5, 5.3
    print("c, d = ", c, d)
    # 값의 교환 (Swap)
    c, d = d, c
    print("c, d = ", c, d )

    # 같은 값을 동시 할당
    x = y = z = 10
    print(x, y, z)

    # 파이썬은 동적 타이핑 언어
    a = 2024 # 값이 할당될 때 타입이 결정 -> 타입이 뭔지 확인
    print(a, "is", type(a)) # 현재 객체의 형식을 체크
    a = "Hello Python"
    print(a, "is", type(a))

    # 특정 객체인지 여부를 판단하는 함수 : isinstance
    print("a는 str의 객체?", isinstance(a, str))

    # 확장 치환문 : 산술, 비트 연산자 등은 확장 치환문으로 변경 가능
    a = 10
    a += 10 # a = a + 10
    print(a)

def bool_ex():
    print("======= bool 연습")
    # 참, 거짓
    # 내부적으로 거짓은 0, 나머지는 모두 참으로 판정
    # 조건 분기, 흐름 제어 활용되기 때문에 중요
    # boolean 판정
    # 논리 연산자 비교 연산자의 비교
    # bool 객체 함수를 통해 얻을 수 있음
    print(bool(0))
    a = 2024
    print(a > 0)
    print(type(a))

    print(isinstance(True, bool)) # True
    print(isinstance(True, int)) # True
    print(True + True)

    # 자료의 형태에 의한 boolean 판정
    print(bool(2024), bool(0)) # int 값에 의한 boolean
    print(bool(3.14), bool(0)) # float 값에 의한 boolean
    print(bool("Pyton"), bool("")) # str 값에 의한 boolean

    print(bool([1, 2, 3]), bool([]))
    print(bool({"key": "value"}), bool({}))
    print(bool(None)) # None -> 비어 있음 -> Java null

    # 논리식의 계산 순서 : Curcuit Break
    # OR(논리합)
    # AND일 경우, 둘 다 True면 뒤쪽 결과를 취한다
    # AND일 경우, 전체 논리식이 거짓이라면 None을 반환
    print("CB 1:", [] or "logical") # False or True
    print("CB 2:", 'logical' or 'operator') # True or True
    print("CB 2-1:", 'logical' and 'operator') # True and True
    print("CB 3", '' or 'operator') # False or True
    print("CB 3-2", '' and 'operator') # False and True
    print("CB 4:", None and 1) # False and True
    print("CB 5:", None or []) # False or False


def type_hint():
    # 파이썬은 동적 타이핑 언어 -> 변수의 타입을 명시적으로 지정하지 않음
    # 3.5부터 타입 힌트를 이용, 타입체크를 진행할 수 있음
    def add(a: int, b: int) -> int:
        return a + b
    print(add(10, 20))
    # print(add("Python", 3.10))

    def greet(name:str) -> str: # str 입력 받아서 str을 리턴하는 함수
        return 2024
        # return "Hello, " + name

    untyped = "string"
    print(untyped)
    untyped = 2024
    print(untyped)

    typed: str = "string" # 타입 힌트가 적용된 변수
    print(typed)
    typed = 2024
    print(typed)

if __name__ == "__main__":
    # 다른 모듈로 import 되는 경우 __name__ == "python_basics"
    # 직접 실행될 경우(최상위 모듈일 경우) __name__ == "__main__"
    # arith_oper()
    # rel_oper() # 비교 연산자 연습
    # var_ex()
    # assignment_ex() # 변수 치환 연습
    # bool_ex()
    type_hint()