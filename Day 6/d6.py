Distance = [400, 1213, 1011, 1540]
Time = [47, 98, 66, 98]
ways_to_beat = [0, 0, 0, 0]

for i, time in enumerate(Time):
    threshold = Distance[i]
    ## held is equivalent for 
    for held in range(0, time):
        distance = (time - held) * held
        if distance > threshold:
            ways_to_beat[i] += 1
total = 1 
for li in ways_to_beat:
    if li != 0:
        total *= li 
print(total)
        

## my next attempt was to start in the middle and do a search from the middle out
## However, this was not required as it ran in reasonable time
Distance = 400121310111540
Time = 47986698
ways_to_beat = 0
## held is equivalent for 
for held in range(0, Time):
    distance = (Time - held) * held
    if distance > Distance:
        ways_to_beat += 1

print(ways_to_beat)
        

 
