# date: 2021/07/22

# <<문자열>> --> 이걸로 행맨 만들어 봐야할듯

# 문자열 안에 ' " 포함시키기
# " 포함 예
food = "Bobby's favorite food is cheese burger!"
print(food)

# ' 포함 예
say = '"Python is very easy." Bobby says.'
print(say)

# 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline_1 = "Life is too short\nYou need Python"
print(multiline_1)

# <문자열 연산하기>

# 문자열 + 더하기
head = "Python"
tail = " is fun!"
print(head + tail)

# 문자열 * 곱하기
a = "Bobby "
print(a*2)

# 문자열 * 곱하기 응용
TwoLine = "="
print(TwoLine * 50)
print("My Program")
print(TwoLine * 50)

# 문자열 길이 구하기
a = "I do what I wanna do, and nobody gon stop me!!"
print(len(a))

# <문자열 인덱싱>
a = "Hustle hard~"
print(a[7]) #문자열 앞에서 7번째 문자 출력
print(a[-2]) #문자열 뒤에서 2번째 문자 출력

# <문자열 슬라이싱>
a = "Hustle hard~"
print(a[0:6]) #문자열 잘라서 출력
print(a[:6])
print(a[0:])

# 슬라이싱 예
DateWeather = "20210721Humid"
date = DateWeather[:8]
weather = DateWeather[8:]
print(date+"\n"+weather)

# 문자열에서 문자 바꾸기 pithon --> python
# 틀린 예
a = "pithon"
a[1] = "y"
print(a)
#올바른 예
a = "pithon"
a = a[:1] + "y" + a[2:]
print(a)

# <문자열 포매팅>
# 1.숫자 바로 대입
print("I eat %d burgers errday" %3)
# 2.문자열 바로 대입
print("I can eat %s burgers today" %"three")
# 3.숫자 값을 나타내는 변수로 대입
number = 3
print("I don't eat %d chicken leg" % number)
# 4.2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. And I was sick for %s days." %(number, day))

# date: 2021/07/22

# <포맷 코드와 숫자 함께 사용>
# 1.정렬과 공백
print("%10s" % "hi")
print("%-10sjane." % 'hi')

# 2.소수점 표현하기
print("%0.4f" % 3.1453113)
print("%10.4f" % 3.5253212)

# <Format 함수를 사용한 포메팅>
# 숫자 바로 대입
print("I ate {0} apples".format(3))

# 문자열 바로 대입
word = "five"
print("I ate {0} apples".format(word))

# 숫자 값을 가진 변수로 대입
number = 3
print("I ate {0} apples".format(number))

# 2개 이상 넣기
number = 3
word = "HAHA"
print("I ate {0} burger. {1}!".format(number, word))

# 이름으로 넣기
print("안녕 나는 형이 {num}명있고 둘 다 {word}야".format(num = 2,word = "바보"))

# 혼용해서 넣기
print("안녕 나는 형이 {0}명있고 둘 다 {word}야".format(2,word = "바보"))

# 왼쪽 정렬
print("{0:<10}".format(("hi")))

# 오른쪽 정렬
print("{0:>10}".format(("hi")))

# 가운데 정렬
print("{0:^10}".format(("hi")))

# 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# 소숫점 표현하기
y = 3.146342
print("{0:0.4f}".format(y))

y = 3.146342
print("{0:10.4f}".format(y))

# { 또는 } 문자 표현하기
print("{{ and }}".format())

# < f 문자열 포매팅 >
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다')

# 수식 추가 가능
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age+1}입니다')

# < 문자열 관련 함수들 >

# 문자 개수 세기(count)
a = "bobby"
print(a.count('b'))

# 위치 알려주기1(find)
a = "Python is the best choice"
print(a.find("b")) #문자열 중 b가 처음 나온 위치를 반환
print(a.find("k")) #찾는 문자나 문자열이 존재X --> -1 반환

# 위치 알려주기2(index)
a = "Life is too short"
print(a.index('t')) #문자열 중 t가 처음 나온 위치를 반환
print(a.index('k')) #찾는 문자나 문자열이 존재X --> 오류 발생

# 문자열 삽입(join)
print(",".join('abcd')) #문자열 각각의 문자사이에 ','를 삽입
print(",".join(['a', 'b', 'c', 'd'])) #리스트나 튜플도 입력으로 사용할 수 있다

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper())

# 대문자르 소문자로 바꾸기(lower)
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기(lstrip)
a = " hi "
print(a.lstrip())

# 오른쪽 공백 지우기(rstrip)
a = " hi "
print(a.rstrip())

# 양쪽 공백 지우기(strip)
a = " hi "
print(a.strip())

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기(split)
a = "Life is too short"
print(a.split())

b = "a:b:c:d"
print(b.split((':'))) # ':'가 구분자가 되어 나누어줌