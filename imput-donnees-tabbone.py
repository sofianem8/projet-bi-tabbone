import pandas as pd
import numpy as np
from pathlib import Path

def main():
    # Utilisation de pathlib
    base_dir = Path('C:/Users/sofiane.mebchour/Downloads/Tabbone/Données nettoyées')
    cleaned_data_path = base_dir / 'Donnees-nettoyees.xlsx'
    output_path = base_dir / 'Donnees-nettoyees-imputed.xlsx'
    
    # Charger les données
    cleaned_data = pd.read_excel(cleaned_data_path)
    
    # Remplacer les valeurs '?' par NaN pour une gestion uniforme des valeurs manquantes
    cleaned_data.replace('?', np.nan, inplace=True)
    
    # Déterminer les types de chaque colonne pour choisir la méthode d'imputation appropriée
    column_types = cleaned_data.dtypes
    
    # Imputation des valeurs manquantes
    for column in cleaned_data.columns:
        if column_types[column] in ['int64', 'float64']:  # Pour les colonnes numériques
            # Imputer avec la médiane
            cleaned_data[column].fillna(cleaned_data[column].median(), inplace=True)
        elif column_types[column] == 'object':  # Pour les colonnes catégorielles
            # Imputer avec le mode
            cleaned_data[column].fillna(cleaned_data[column].mode()[0], inplace=True)
    
    # Vérifier et afficher le nombre de valeurs manquantes pour chaque colonne après l'imputation
    missing_values_after = cleaned_data.isnull().sum()
    print("Nombre de valeurs manquantes par colonne après imputation:")
    print(missing_values_after)

    # Optionnel : Sauvegarder le DataFrame nettoyé
    # Correction du chemin de sortie également
    cleaned_data.to_excel(output_path, index=False)

if __name__ == "__main__":
    main()
