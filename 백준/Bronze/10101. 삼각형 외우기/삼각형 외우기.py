ang_1 = int(input())
ang_2 = int(input())
ang_3 = int(input())
sum_ang = ang_1 + ang_2 + ang_3
set_Isosceles = {ang_1, ang_2, ang_3}
if sum_ang != 180:
    print("Error")
if sum_ang == 180 and len(set_Isosceles) == 3:
    print("Scalene")
if ang_1 == ang_2 == ang_3 == 60:
    print("Equilateral")
if sum_ang == 180 and len(set_Isosceles) == 2:
    print("Isosceles")