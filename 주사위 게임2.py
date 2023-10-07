def solution(a, b, c):
    answer = 0
    if a == b and b == c:
        answer = (3**3)*a**6
    elif a != b and b != c and c != a:
        answer = a + b + c
    else:
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    return answer