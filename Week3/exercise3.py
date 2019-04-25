import json
import requests

def getUrlInfo():
    url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTime/1/5"
    source_code = requests.get(url)

    text = source_code.text
    print(text)

    json_data = json.loads(text)
    print(json_data)

    print(json_data['SeoulLibraryTime']['RESULT']['CODE'])
    print(json_data['SeoulLibraryTime']['row'][0]['LBRRY_NAME'])
    print(json_data['SeoulLibraryTime']['row'][0]['ADRES'])
    print(json_data['SeoulLibraryTime']['row'][0]['FDRM_CLOSE_DATE'])

    print(len(json_data['SeoulLibraryTime']['row']))

    for i in range(len(json_data['SeoulLibraryTime']['row'])):
        print(json_data['SeoulLibraryTime']['row'][i]['LBRRY_NAME'])

# can map with folium

if __name__ == '__main__':
    getUrlInfo()