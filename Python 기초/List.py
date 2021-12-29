# 리스트 List
    # 파이썬에서는 동적배열로써 리스트 안의 요소들은 자유롭게 변경가능
    # 각 요소들은 서로 다른 타입이 될 수 있고, 컴마(,)로 구분
    # 요소가 없는 빈 리스트는 "[]"와 같이 표현

a = []                   # 빈 리스트
a = ["AB", 10, False]    # 서로 다른 타입이 가능

# 2021/12/28 마무리 
# 2021/12/29 시작

# 리스트 인덱싱
    # a[0] 부터 시작 , a[-1] 은 리스트에서 마지막 요소 
    # a[-2] 는 뒤에서 두번째 요소
a = ["AB", 10, False]
x = a[1]                # a의 두번째 요소 읽기
a[1] = "Test"           # a의 두번째 요소 변경
y = a[-1]               # False
print(y)


# 리스트 슬라이싱
    # 리스트 일부 요소를 선택
    # 콜론 왼쪽 숫자 = 우리가 추출하기 원하는 시작 인덱스 
    # 콜론 오른쪽에 써주는 숫자 = 우리가 추출하기 원하는 끝 인덱스 + 1
a = [1, 3, 5, 7, 10]
x = a[1:3]      # [3, 5]    = 인덱스 1,2 까지만 추출
x = a[:2]       # [1, 3]    = 인덱스 0부터 1까지
x = a[3:]       # [7, 10]   = 인덱스 3부터 끝까지

# 리스트 요소 추가,수정,삭제
    # 추가 = 리스트.append()
    # 삭제 = del 요소
a = ["AB", 10, False]
a.append(21.5)  # 추가 ( 맨뒤로 )
a[1] = 11       # 변경
del a[2]        # 삭제
print(a)        # ['AB', 11, 21.5]  

# 리스트 병합과 반복
    # 병합
a = [1, 2]
b = [3, 4]
c = a + b
print(c)    # [1, 2, 3, 4]
    # 반복
d = a * 3
print(d)    # [1, 2, 1, 2, 1, 2]

# 리스트 검색
mylist = "RiGun Hello Python and RiGun".split()
i = mylist.index('Python')  # i = 2 , index = 몇 번째 인가
n = mylist.count('RiGun')   # n = 2 , count = 특정 문자의 개수
print(i, n)

# List Comprehension
    # 0부터 9 까지 숫자중 3으로 나눈 나머지가 0인 숫자에 대해서 그 제곱에 대한 리스트를 구함
list = [n ** 2 for n in range(10) if n % 3 == 0]
print(list) # [0, 9, 36, 81]