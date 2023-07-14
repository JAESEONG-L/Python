abc= [*map(int, input().split())]


start_seconds= abc[0]*3600+abc[1]*60+abc[2]

finished_seconds= start_seconds+int(input())

ss= finished_seconds%60

finished_minutes= finished_seconds//60

mm= finished_minutes%60

finished_hours= finished_minutes//60

hh= finished_hours%24

print(hh, mm, ss)
