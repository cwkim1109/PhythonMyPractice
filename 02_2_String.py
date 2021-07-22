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

# # 왼쪽 정렬
# "{0<10}".format(("hi"))

