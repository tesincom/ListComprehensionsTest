"""
My List Comprehension Examples
Özgür
Description: Complex usage of list comprehensions while studying.
"""

# Çift sayıların küpünü al, 3’e bölünebilenleri seç
numbers = range(1, 30)
filtered_cubes = [n**3 for n in numbers if n % 2 == 0 and (n**3) % 3 == 0]
print("Filtered cubes:", filtered_cubes)

# String içindeki harfleri say (frequency dictionary)
text = "im studying list comprehensions"
freq = {ch: text.count(ch) for ch in set(text) if ch.isalpha()}
print("Letter frequencies:", freq)

#İç içe koşullu comprehension
# Pozitifleri "positive", negatifleri "negative", sıfırı "zero" yap
values = [-2, -1, 0, 1, 2]
labels = ["positive" if v > 0 else "negative" if v < 0 else "zero" for v in values]
print("Labels:", labels)

#karekökü tam sayı olan sayılar
perfect_squares = {n for n in range(1, 100) if int(n**0.5) == n**0.5}
print("Perfect squares:", perfect_squares)
