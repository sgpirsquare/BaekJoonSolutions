home_to_school = int(input())
school_to_PC = int(input())
PC_to_academy = int(input())
academy_to_home = int(input())

sum_times = home_to_school + school_to_PC + PC_to_academy + academy_to_home

print(int(sum_times // 60))
print(int(sum_times % 60))