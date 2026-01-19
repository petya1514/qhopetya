def observed ():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", }
    return observations
def run_tasks1():
    print(observed())

run_tasks1()

def observations2():
    observations = []
    for count in range(7):
        observations.append(input("Please enter an observation: "))
    return observations
def run_tasks2():
    print("Counting observations2")
    observations = observations2 ()
    #populate set
    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)
        #display set
        for data in observations_set:
            print(f"{data[0]}observations: {data[1]}times")

run_tasks2()