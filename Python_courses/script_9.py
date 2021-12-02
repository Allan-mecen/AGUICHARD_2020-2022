"""Description

TODO :

- Crée un Enum sous-jacent qui répertorie toutes
possibilités d'hyer paramètres par modèle. C'est plus
long et plus lourd mais c'est exhaustif. 

"""

import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
from enum import Enum, auto
from serde import serialize, deserialize
from serde.yaml import from_yaml, to_yaml
import typer


# Enum : poser des alternatives à l'utilisateur pour l'empecher de faire de la merde.

@dataclass
class Dataset:
    #Importer un dataset
    #Création du X et du y.

@dataclass
class Visualisation:
    # Stats descriptives / Première visualisations
    # Utilisation de la commande print avec la librairie `rich`

@dataclass
class Apprentissage:
    # Utilisation de la fonction `train_test_split`

class Complexite(Enum):
    SIMPLE = "simple"
    COMPEXE = "complexe"

@serialize
@deserialize
@dataclass
class Modeles:
    LogisticRegression: Complexite
    MultinomialNB: Complexite
    DecisionTree: Complexite
    Kneighbors: Complexite
    SVC: Complexite
    RandomForest: Complexite
    MLP: Complexite



@dataclass
class Synthèse:
    # 