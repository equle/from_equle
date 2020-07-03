import json

## game save
def set_charact(name):
    character = {
        "name" : name,
        "Lv" : 1,
        "Hp" : 100,
        "item" : ["핑핑이 사료", "집게리아 직원모자", "네모바지"],
        "skill" : ["쿵푸 펀치", "웃음", "사랑"]
    }
    with open('static/save.txt', 'w', encoding='utf-8') as f:
        json.dump(character, f, ensure_ascii=False, indent=4)
    return print('캐릭터의 정보가 저장되었습니다.')

## game lode
def get_charact():
    with open("static/save.txt","r",encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
    return character