'''l = []
l.append(31)
l.append(12)
l.append(93)
l.append(l[0] + l[1] + l[2])
print(l)

print()

d = {}
d['x'] = 9
d['y'] = 2
d['z'] = d['x'] ** d['y']
print(d)
print()


rdict = {
  "code": 1,
  "content": {
    "text": "apple",
    "changedText": "apple",
    "tpl_name": "one_plus_word",
    "records": {
      "words_additions": [
        {
          "name": "apple watch",
          "href": "https://rozetka.com.ua/search/?text=apple+watch"
        },
        {
          "name": "apple iphone 7",
          "href": "https://rozetka.com.ua/search/?text=apple+iphone+7"
        },
        {
          "name": "apple iphone 7 plus",
          "href": "https://rozetka.com.ua/search/?text=apple+iphone+7+plus"
        },
        {
          "name": "apple iphone",
          "href": "https://rozetka.com.ua/search/?text=apple+iphone"
        },
        {
          "name": "apple iphone 6",
          "href": "https://rozetka.com.ua/search/?text=apple+iphone+6"
        }
      ],
      "cats_searches": [
        {
          "id": "80004",
          "top_id": "80253",
          "name": "в категории <span class='bold'> Ноутбуки</span>",
          "href": "https://rozetka.com.ua/search/?text=apple&section_id=80004&redirected=1"
        },
        {
          "id": "180768",
          "top_id": "80253",
          "name": "в категории <span class='bold'> Блоки питания для ноутбуков</span>",
          "href": "https://rozetka.com.ua/search/?text=apple&section_id=180768&redirected=1"
        },
        {
          "id": "80003",
          "top_id": "4627949",
          "name": "в категории <span class='bold'> Мобильные телефоны</span>",
          "href": "https://rozetka.com.ua/search/?text=apple&section_id=80003&redirected=1"
        }
      ]
    },
    "count": 8,
    "total_count": 0,
    "page": 0,
    "start": 0,
    "sections_menu": [
      
    ],
    "move_to_category": "Перейти в категорию",
    "price_with_promo": "Цена с промокодом",
    "sudg_noth_to_find": "По вашему запросу ничего не найдено. <nobr>Уточните свой запрос",
    "all_find_result": "Все результаты поиска",
    "currency": "грн"
  }
}
print(rdict['content']['records']['words_additions'][-1]['name'])'''

def foo():
  return

a = 5
if a > 2:
  print("a > 2")
else:
  print("a <= 2")