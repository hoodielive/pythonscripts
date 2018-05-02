import heapq 

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2] 

print(heapq.nlargest(3, nums)) 

print(heapq.nsmallest(3, nums)) 

portfolio = [
        {'name' : 'Paimon', 'speciality' : 'mind control', 'legions' : 200.1}, 
        {'name' : 'Purson', 'speciality' : 'alchemy', 'legions' : 30.1}, 
        {'name' : 'Bael', 'speciality' : 'kingliness', 'legions' : 120.1}, 
        {'name' : 'Beleth', 'speciality' : 'emotional control', 'legions' : 91.1}, 
        {'name' : 'Vine', 'speciality' : 'protection and revenge', 'legions' : 75.1}, 
        {'name' : 'Zagan', 'speciality' : 'concealment', 'legions' : 82.1}, 
        {'name' : 'Balaam', 'speciality' : 'prophecy', 'legions' : 52.1}, 
        {'name' : 'Asmoday', 'speciality' : 'mystical sight', 'legions' : 20.1}, 
        {'name' : 'Belial', 'speciality' : 'self-governance', 'legions' : 50.1}, 
] 

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['legions']) 
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['legions']) 

print(cheap)
print(expensive)
