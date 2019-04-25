from xml.etree.ElementTree import Element, SubElement, ElementTree

blog = Element('blog')
blog.attrib['date'] = '20161225'

SubElement(blog, 'subject').text = '파이썬'
SubElement(blog, 'author').text = '홍길동'
SubElement(blog, 'content').text = '파이썬 xml으로 다루기'

def indent (elem, level = 0):
    mytab ='\t'
    i = '\n' + level * mytab
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level+1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(blog)

xmlFile = 'xml_exercise01.xml'
ElementTree(blog).write(xmlFile, encoding='utf-8')

print("작업완료")