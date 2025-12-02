"""
Napisz funkcję, która przyjmuje dwa stringi i sprawdza, czy są swoimi anagramami.

Na przykład:
„army” i „Mary”,
„dzielenia” i „niedziela”,
„Quid est veritas?” i „Vir est qui adest”,
„Jim Morrison” i „Mr Mojo Risin”
„Tom Marvolo Riddle” i „I am Lord Voldemort”
"""

def if_anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()

    text1_set = list(text1)
    text1_set.sort()
    text2_set = list(text2)
    text2_set.sort()
    result = text1_set == text2_set
    print(text1_set, text2_set, result)

if __name__ == '__main__':
    if_anagram("army", "Mary")
    if_anagram("Dzielenie", "niedziela")