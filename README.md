# HandsTracking
 
# Projet 1 : Suivi du volume avec les gestes des doigts (PYCaw + MediaPipe)

## Description
Ce projet utilise **PYCaw** pour contrôler le volume du système en fonction de la distance entre les doigts d'une main détectée via **MediaPipe**. Plus les doigts sont écartés, plus le volume augmente. L'application permet un contrôle intuitif du volume en utilisant la caméra de l'ordinateur et des gestes de la main.

## Fonctionnalités
- Suivi en temps réel des mouvements des doigts via la caméra.
- Contrôle du volume du système en fonction de l'écartement des doigts.
- Affichage du volume actuel en pourcentage.

## Prérequis
- **Python 3.x**
- **Bibliothèques :**
  - `opencv-python` (pour la gestion de la caméra et du traitement d'image)
  - `mediapipe` (pour la détection des mains et des gestes)
  - `pycaw` (pour contrôler le volume du système Windows)

## Installation
1. Clone le projet sur ton ordinateur.
2. Assures-toi d'avoir les librairies python nécessaires
3. Exécute le fichier "Projet1.py" : python Projet1.py

## Explication du code
1. Détection des mains : Utilisation de MediaPipe pour détecter les positions des doigts dans l'image de la caméra.
2. Calcul de l'écartement des doigts : L'écartement entre les doigts est calculé, et cette information est utilisée pour ajuster le volume du système via PYCaw.
3. Affichage du volume : Le volume actuel est affiché en pourcentage et est ajusté dynamiquement lorsque l'écartement des doigts change.

# Projet 2

## Description
Ce projet utilise **MediaPipe** pour détecter les doigts levés en temps réel via la caméra et afficher une image correspondante au nombre de doigts levés. Chaque image représente un nombre spécifique de doigts levés (0 à 5 doigts).

## Fonctionnalités
- Détection des mains via la caméra en temps réel.
- Comptage des doigts levés.
- Affichage d'une image associée au nombre de doigts levés, avec une position fixée dans la fenêtre de la caméra.
- Support d'une interface visuelle avec OpenCV.

## Prérequis
- **Python 3.x**
- **Bibliothèques :**
    - `opencv-python` (pour la gestion de la caméra et du traitement d'image)
    - `mediapipe` (pour la détection des mains et des gestes)

## Installation
1. Clone le projet sur ton ordinateur.
2. Assures-toi d'avoir les librairies python nécessaires
3. Exécute le fichier "Projet2.py" : python Projet2.py

## Explication du code
1. Détection des mains : Le code utilise MediaPipe pour détecter la main et les repères de la main en temps réel via la caméra.
2. Comptage des doigts levés : Chaque doigt est comparé pour déterminer s'il est levé ou non en fonction de sa position.
3. Affichage des images : Selon le nombre de doigts levés, une image associée (par exemple, ZeroFinger.png, OneFingers.png, etc.) est affichée sur l'écran dans la fenêtre vidéo. Cette image est redimensionnée et placée dans un coin de l'écran.
4. Effet miroir : La caméra est affichée avec un effet miroir pour une interaction plus intuitive.