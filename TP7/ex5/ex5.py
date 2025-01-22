import pandas as pd

def main():
    # Lire le fichier CSV
    df = pd.read_csv("employees.csv")
    print("Les cinq premières lignes du fichier :")
    print(df.head())

    # Calculer la moyenne d'un champ numérique
    if 'age' in df.columns:
        print(f"Moyenne des âges : {df['age'].mean()}")

if __name__ == "__main__":
    main()
