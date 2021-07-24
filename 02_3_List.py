#02-3 리스트 자료형


odd = [1, 3, 5, 7, 9]

# 리스트명 = [요소1, 요소2, 요소3, ...]
# 여러가지 리스트
a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# < 리스트의 인덱싱과 슬라이싱 >

# <리스트의 인덱싱>
a = [1, 2, 3]
print(a[0])
print(a[0] + a[2])
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

# <삼중 리스트 인덱싱>
a = [1,2, ['a','b',['Life', 'is']]]
print(a[2][2][0])

# 리스트의 슬라이싱(나누기)
a = [1,2,3,4,5,]
print(a[0:2])
# --> 문자열과 비교(밑 참고)
a = "12345"
print(a[0:2])

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)

# 중첩된 리스트에서 슬라이싱 하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

# < 리스트 연산하기 >

# 리스트 더하기(+)
a = [1,2,3]
b = [4,5,6]
print(a+b)

# 리스트 반복하기(*)
a = [1,2,3]
print(a*3)

# 리스트 길이구하기
a = [1,2,3]
print(len(a))

# 리스트 연산 오류
a = [1,2,3]
print(a[2] +"hi") #a[2]의 값은 정수형, "hi'는 문자열이므로 연산 오류 발생
print(str(a[2])+"hi") #a[2]를 문자열로 바꿔서 연산가능

# < 리스트의 수정과 삭제 >
a = [1,2,3]
a[2] = 4
print(a)

# 리스트 요소 삭세 (del함수)
a = [1,2,3]
del a[1]
print(a)

a = [1,2,3,4,5]
del a[2:]
print(a)

# <리스트 관련 함수 >

# 리스트에 요소 추가(append)
a = [1,2,3]
a.append(4)
print(a)

a.append([5,6]) #다른 자료형 추가
print(a)

# 리스트 정렬(sort)
a = [1,4,3,2]
a.sort()
print(a)

a = ['a','c','b']
a.sort() # 알파벳 순으로 정렬 가능
print(a)

# 리스트 뒤집기(reverse)
a = ['a','b','c']
a.reverse()
print(a)

# 위치 반환(index)
a = [1,2,3]
print(a.index(3))
print(a.index(1))
print(a.index(0)) #리스트에 없으므로 오류 발생

# 리스트에 요소 삽입(insert)
a = [1,2,3]
a.insert(0,4)
print(a)
a.insert(3,5)
print(a)

# 리스트 요소 제거(remove) --> remove(x) : 리스트에서 첫번째로 나오는 x를 삭제하는 함수

a = [1,2,3,1,2,3]
a.remove(3) # 첫번째 3제거
print(a)
a.remove(3) # 한번더 실행에 남은 3 제거
print(a)

# 리스트 요소 끄집어내기(pop)
a = [1,2,3]
print(a.pop()) # pop() : 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제
print(a)

a = [1,2,3]
print(a.pop(1)) # pop(x) : 리스트의 x번째 요소를 돌려주고 그 요소를 삭제한다
print(a)

# 리스트에 포함된 요소 x의 개수 세기(count) --> count(x) : 리스트 안에 x가 몇개 있는지 조사하여 그 개수 반환
a = [1,2,3,1]
print(a.count(1))

# 리스트 확장(extend) --> extend(x) : x값에 리스트형만 사용가능
a = [1,2,3]
a.extend(([4,5]))
print(a)

b = [6,7]
a.extend(b)
print(a)

a+= [8,9,10] # a.extend([8,9,10])과 동일한 기능
print(a)