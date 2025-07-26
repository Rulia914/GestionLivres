# 📘 Gestion de livres 

## 📋 Table des matières

1. [🎯 Fonctionnalités à implémenter](#fonctionnalités-à-implémenter)
2. [📚 Structure des livres](#structure-des-livres)
3. [📂 Contraintes de persistance](#contraintes-de-persistance)
4. [🧠 Travail demandé](#travail-demandé)
5. [✅ Exemple d'interface en console](#exemple-dinterface-en-console)
6. [🔗 Liens utiles](#liens-utiles)

---

Tu dois développer un programme en **Python** pour gérer une collection de livres, avec enregistrement et lecture des données dans un **fichier texte** (`livres.txt`).

## Fonctionnalités à implémenter

Le programme doit te permettre de :

1. 📖 **Lister** tous les livres enregistrés
2. ➕ **Ajouter** un nouveau livre
3. ❌ **Supprimer** un livre par son titre
4. ✏️ **Modifier** les informations d'un livre
5. 💾 **Sauvegarder automatiquement** les changements dans le fichier `livres.txt`
6. 🚪 **Quitter** le programme

## Structure des livres

Chaque livre contient :
* `ISBN` (chaîne)
* `Titre` (chaîne)
* `IdAuteur` (entier)
* `Année de publication` (entier)

Les livres seront enregistrés dans un fichier texte sous le format suivant l'exemple :

```txt
Isbn | Titre | IdAuteur | Année

123456 | Le Petit Prince | 1 | 1943
789456 | Nos étoiles contraires | 2 | 2012
```

Chaque ligne représente un livre, les champs sont séparés par un `|`.

## Contraintes de persistance

* À chaque modification (ajout, suppression, modification), le fichier `livres.txt` doit être **écrit ou mis à jour**


## Travail demandé

1. **Analyser** les besoins et réfléchir à la meilleure structure de données (livres ET auteurs)
2. Créer des **fonctions** pour chaque fonctionnalité
3. Implémenter un **menu** interactif en boucle
4. Gérer la **lecture/écriture dans le fichier texte**
5. T'assurer que le programme est **robuste** (ex : vérifier si un livre existe avant de le modifier ou le supprimer)

## Exemple d'interface en console

```text
===== MENU BIBLIOTHÈQUE =====
1. Livres
2. Auteur
5. Quitter

> Choix: 1

===== MENU LIVRES =====

1. Lister les livres
2. Ajouter un livre
3. Supprimer un livre
4. Modifier un livre
5. RETOUR

> Choix : 1

Liste des livres :

- 123456 - Le Petit Prince - Antoine de Saint-Exupéry (1943)
- 789456 - Nos étoiles contraire - John Green (2012)
```

---

## Liens utiles

### 📖 Manipulation des dictionnaires
Si tu veux mieux comprendre comment créer et gérer des dictionnaires : [W3Schools – Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)


### 📁 Manipulation de fichiers
Pour apprendre à lire et écrire des fichiers :  [W3Schools – Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)


### 🧩 Bonus – Programmation orientée objet
Si tu te sens à l’aise et veux aller plus loin, essaie de créer ce programme en utilisant des **classes** : [W3Schools – Python Classes](https://www.w3schools.com/python/python_classes.asp)

