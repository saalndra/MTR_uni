# coefs
probability_of_rain = 0.3 # change this
rain_house = 2
rain_forest = 0 
dry_house = 5
dry_forest = 10
#====

def main():
    m_house = (probability_of_rain * rain_house) + ((1-probability_of_rain) * dry_house)
    m_forest = (probability_of_rain * rain_forest) + ((1-probability_of_rain) * dry_forest)

    print(" M(house):", m_house, "\n", "M(forest):", m_forest)
    if (m_forest > m_house):
        print("welcome to the forest")
    else:
        print("home sweet home")

main()

