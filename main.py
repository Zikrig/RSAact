from person import person as pers
Ann = pers(3517,1999,181)
Bill = pers(2767,2633,179)

Ak = Ann.key
Bk = Bill.key
sBill=Bill.shifr("Здравствуй Анна, Федор Максимович Гризик",Ak)
readAnna = Ann.deshifr(sBill)
print(readAnna)

sAnna=Ann.shifr("Здравствуй Билл",Bk)
readBill=Bill.deshifr(sAnna)
print(readBill)

