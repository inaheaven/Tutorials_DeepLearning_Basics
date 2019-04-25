from xml.etree.ElementTree import  parse

tree = parse('xml_exercise03.xml')
myroot = tree.getroot()

print(type(myroot))

print('속성읽기1:', end='')
print(myroot.keys())

print('속성읽기2:', end='')
print(myroot.items())

print('속성읽기3:', end='')
print(myroot.get('설명'))

print('속성읽기4:', end='')
print(myroot.get('foo', '미존재시기본값'))
print()


family1 = myroot.findall('가족')
print('findall는 일치하는 모든 태그를 리스트로 반환한다')
print(family1)

family2 = myroot.findtext('가족')
print('findtext는 일치하는 1번째 태그의 텍스트값을 반환한다')
print(family2)

family = myroot.find('가족')
print('find는 일치하는 1번째 태그를 리턴한다')
print(family)


childs = family.getchildren()
print(childs)

for child in childs:
    print('엘레먼트 정보', end=" ")
    print(child)
    elem = child.getchildren()

    for item in elem:
        print("하위 엘리먼트정보", end="")
        print(item, end="")
        print(item.text, end="")
        if(item.text == '이순자'):
            print(item.attrib['정보'])
        else:
            print()
    print()
print()