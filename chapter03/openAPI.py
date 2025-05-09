import requests

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

# print(rjson)
# print(rjson['RealtimeCityAir']['row'][0])


# 1. 모든 구의 IDEX_MVL 값 프린트하기
for value in rjson['RealtimeCityAir']['row']:
    print(value['MSRSTE_NM'], value['IDEX_MVL'])


# IDEX_MVL 값이 60 미만인 구의 이름과 값 프린트하기
for value in rjson['RealtimeCityAir']['row']:
    IDEX_MVL = value['IDEX_MVL']
    if IDEX_MVL < 60:
        print(value['MSRSTE_NM'], IDEX_MVL)

