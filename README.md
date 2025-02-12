# Projet : La fouille de données au service du développement durable

## Contexte  

**Big Datext**, une entreprise grenobloise spécialisée dans l'analyse prédictive, et la **mairie de Grenoble** se sont associées pour mettre en place et diffuser une base de données dans le cadre d'un défi associé à la conférence nationale **EGC 2017**.  

Ce défi porte sur l'analyse des **données relatives aux espaces verts** et poursuit deux objectifs principaux.  

---

## Défi 1 : Prédiction des défauts des arbres  

Ce défi comprend **deux tâches de prédiction** visant à déterminer si un arbre présente un **défaut** et, si oui, **où il est situé**.  

### 🔹 Tâche supervisée 1 : Classification uni-label  
> Prédire si un arbre a un défaut.  

Il s'agit d'un **problème de classification uni-label**, car **chaque arbre possède un unique label de défaut**.  

### 🔹 Tâche supervisée 2 : Classification multi-label  
> Prédire les localisations des défauts d’un arbre.  

C'est un **problème de classification multi-label**, car **un arbre peut avoir des défauts à plusieurs endroits** (ex. racine et tronc simultanément).  

**Une approche possible** consiste à construire **autant de classifieurs que de classes**, par exemple :  
- Un classifieur pour prédire si un arbre a un défaut au **collet** ou non.  
- Un classifieur pour prédire si un arbre a un défaut à la **racine** ou non.  
- Etc.  

### 🔸 Baseline (modèle de référence)  

| Modèle | Accuracy | Précision | Rappel |
|--------|----------|-----------|---------|
| **Uni-label** | 86% | 82% | 72% |
| **Multi-label** | - | 64% | 37% |

---

## Défi 2 : Analyse descriptive du parc végétal de Grenoble  

Ce second défi est **plus exploratoire** et vise à mieux **connaître, analyser et comprendre l’évolution du parc végétal de Grenoble**.  

### Objectifs possibles :  
✔️ **Appliquer diverses techniques d’analyse**  
✔️ **Explorer l’évolution et l’entretien des arbres**  
✔️ **Utiliser des données externes pour enrichir l’étude**  
✔️ **Visualiser les données de manière pertinente**  
✔️ **Effectuer des clusterings pour identifier des groupes d'arbres similaires**  
✔️ **Rechercher des règles d’association entre variables**  

---

## Données  

Les données concernent des **arbres situés dans la ville de Grenoble**, entretenus par les services municipaux.  

Elles contiennent des variables décrivant :  
- **Le type d’arbre**  
- **Son stade de développement**  
- **Sa localisation et son environnement**  
- **Son état sanitaire**  
- **Et d’autres caractéristiques pertinentes**  

---

## Déroulement du projet  

📌 **Travail en groupe** : Chaque membre devra justifier **au moins 20h de travail**.  
📌 **Les deux défis devront être abordés avec un logiciel**.  

### 🔍 Contenu du rapport  

Le rapport devra contenir **au minimum** :  

1. **Exploration des données**  
   - Quelles sont les principales tendances et structures des données ?  

2. **Préparation des données**  
   - Quelles variables sont intéressantes ?  
   - Existe-t-il de fortes corrélations ?  
   - Quelle est la meilleure façon d’encoder numériquement chaque variable ?  

3. **Modélisation et algorithmes**  
   - **Au moins 3 algorithmes** seront appliqués pour le défi 1.  
   - Justification du choix des algorithmes.  

4. **Évaluation et interprétation des résultats**  
   - Comparaison avec le classifieur baseline.  
   - Analyse des performances, de l’intelligibilité et de la simplicité des modèles.  
   - Interprétation des modèles au-delà des simples métriques.  
   - Identification des variables les plus prédictives.  

---

## 📅 Dates importantes  

- **21 mars** : Envoi du rapport (PDF) à **Tabbone**.  
- **24-25 mars** : **Soutenance**.  
