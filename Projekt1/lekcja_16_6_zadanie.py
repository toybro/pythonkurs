"""
Napiszcie funkcje, która zwróci 5 najczestrzych słów dzieła Mickiewicza.

https://pastebin.com/raw/aAHeW5Pt (przekopiucje i zapiszcie do pliku tekstowego to,
co znajdziecie pod tym linkiem).

Podpowiedź:  skorzystajcie z metody open(), split(),słownik , pętli
"""

file_ = 'text_input.txt'

slowa = set()
stats = {}

with open(file_, 'r') as f:
    linia = f.readline()
    while linia:

        linia = f.readline()
        slowa_ = linia.split()
        for slowo in slowa_:
            if not stats.get(slowo):
                stats[slowo] = 1
            else:
                stats[slowo] += 1

stats_rev = {y: x for x, y in stats.items()}
print(stats)
print(stats_rev)
print(len(stats_rev))

for i in range(len(stats_rev) - 1, len(stats_rev) - 6, -1):
    print("najczestsze slowo", i, stats_rev[i])
