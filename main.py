from person import person as pers
Ann = pers(59,43,23)
Bill = pers(41,97,997)

Ak = Ann.key
Bk = Bill.key
sBill=Bill.shifr("привет, Анна",Ak)
readAnna = Ann.deshifr(sBill)
print(readAnna)

sAnna=Ann.shifr("Здравствуй, Билл",Bk)
readBill=Bill.deshifr(sAnna)
print(readBill)
