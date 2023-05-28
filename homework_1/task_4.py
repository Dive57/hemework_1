# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input("общее количество сделанных журавликов"))
sergey = s / 6
petr = sergey
ekaterina = (sergey + petr) * 2
print(int(sergey), int(ekaterina), int(petr))