from TP7.ex1.conversion import dollars_to_dirhams, meters_to_kilometers

def main():
    dollars = 100
    meters = 5000

    print(f"{dollars} dollars = {dollars_to_dirhams(dollars)} dirhams")
    print(f"{meters} mètres = {meters_to_kilometers(meters)} kilomètres")

if __name__ == "__main__":
    main()
