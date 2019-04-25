from xml.etree.ElementTree import ElementTree, SubElement, Element


def indent(elem, level=0):
    mytab = '\t'
    i = '\n' + level * mytab
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


mydict = {'kim' : ('김철수', 30, '남자', '마포 공덕'), 'park' : ('박영희', 40, '여자', '용산 도원')}
print('사전', mydict)

members = Element('members')
members.attrib['date'] = '20161225'

for key, mytuple in mydict.items():
    mem = SubElement(members, 'member')
    mem.attrib['id'] = key

    SubElement(mem, 'name').text = mytuple[0]
    SubElement(mem, 'age').text = str(mytuple[1])
    SubElement(mem, 'gender').text = mytuple[2]
    SubElement(mem, 'addr').text = mytuple[3]

indent(members)
xmlFile = 'xml_exercise02.xml'
ElementTree(members).write(xmlFile, encoding='utf-8')
print("finished")

