
def bacteria_double_life():
    time=0
    bacteria_population = int(input("Enter the population of bacteria :"))
    growth_rate = float(input("Enter the growth rate:"))
    dub_population = bacteria_population * 2
    while bacteria_population <= dub_population:
        bacteria_population = bacteria_population + (bacteria_population * growth_rate)
        time=time+1
    print("Bacteria_population:",bacteria_population)
    print("Bacteria doubling time:",time,"min")
        
bacteria_double_life()
