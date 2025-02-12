import pandas as pd  # Pour la manipulation des données tabulaires
import numpy as np   # Pour les opérations numériques
from pathlib import Path  # Pour gérer les chemins de fichiers de façon portable

def main():
    """
    Fonction principale qui nettoie et complète les données manquantes d'un fichier Excel.
    Le script remplace les valeurs manquantes par la médiane pour les données numériques
    et par le mode (valeur la plus fréquente) pour les données catégorielles.
    """
    # Configuration des chemins de fichiers
    base_dir = Path('C:/Users/sofiane.mebchour/Downloads/Tabbone/Données nettoyées')
    cleaned_data_path = base_dir / 'Donnees-nettoyees.xlsx'  # Fichier d'entrée
    output_path = base_dir / 'Donnees-nettoyees-imputed.xlsx'  # Fichier de sortie
    
    # Étape 1 : Chargement du fichier Excel dans un DataFrame pandas
    print("Chargement des données...")
    cleaned_data = pd.read_excel(cleaned_data_path)
    
    # Étape 2 : Remplacement des '?' par NaN (Not a Number)
    # Cela permet d'uniformiser la représentation des valeurs manquantes
    cleaned_data.replace('?', np.nan, inplace=True)
    
    # Étape 3 : Analyse des types de données de chaque colonne
    # Cela nous permet de choisir la bonne méthode d'imputation
    column_types = cleaned_data.dtypes
    
    # Étape 4 : Traitement des valeurs manquantes colonne par colonne
    print("Imputation des valeurs manquantes...")
    for column in cleaned_data.columns:
        # Pour les colonnes numériques (nombres entiers ou décimaux)
        if column_types[column] in ['int64', 'float64']:
            median_value = cleaned_data[column].median()
            cleaned_data[column].fillna(median_value, inplace=True)
            print(f"Colonne {column}: Remplacement par la médiane ({median_value})")
            
        # Pour les colonnes textuelles (catégories, texte, etc.)
        elif column_types[column] == 'object':
            mode_value = cleaned_data[column].mode()[0]
            cleaned_data[column].fillna(mode_value, inplace=True)
            print(f"Colonne {column}: Remplacement par le mode ({mode_value})")
    
    # Étape 5 : Vérification finale des valeurs manquantes
    missing_values_after = cleaned_data.isnull().sum()
    print("\nRésultat - Nombre de valeurs manquantes par colonne:")
    print(missing_values_after)

    # Étape 6 : Sauvegarde des données nettoyées
    print(f"\nSauvegarde du fichier nettoyé dans: {output_path}")
    cleaned_data.to_excel(output_path, index=False)
    print("Traitement terminé avec succès!")

# Point d'entrée du script
if __name__ == "__main__":
    main()
