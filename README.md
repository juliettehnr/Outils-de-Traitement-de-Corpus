# TP - Partie 1

Sources :
https://paperswithcode.com/dataset/conll-2003
https://arxiv.org/pdf/cs/0306050v1

1. Quelle type de tâche propose CoNLL 2003 ?

Il s’agit d’un corpus pour entraîner un système de reconnaissance des entités nommées indépendantes (dans le sens où les entités nommées en question ne relèvent pas d’une langue en particulier). Plus précisément, CoNLL 2003 s’est intéressé aux noms de personnes, de lieux d’organisations et une dernière catégorie plus diverse sert pour les entités qui ne rentraient pas dans les catégories précédentes. 

2. Quel type de données y a-t-il dans CoNLL 2003 ? 

Le corpus CoNLL 2003 est composé de 8 fichiers au total. Il s’agit d’un corpus bilingue anglais/allemand où pour chaque langue il y a un fichier d’entraînement (pour entraîner le système), un fichier de développement (pour ajuster les paramètres de la méthode d’apprentissage), un fichier de test (pour tester le système une fois son apprentissage terminé) et un fichier de données non-annotées.
Les fichiers d’entraînement regroupaient des articles de journaux datant d’entre 1996 et 1997 pour l’anglais et 1992 pour l’allemand.

3. A quel besoin répond CoNLL 2003 ?
   
A améliorer la reconnaissance des entités nommées.

4. Quels types de modèles ont été entraînés sur CoNLL 2003 ?
   
16 systèmes ont été entraînés avec le corpus par 16 participants différents. Chacun utilisaient une combinaison différente de techniques de machine learning (HMM, MEM…).

5.Est un corpus monolingue ou multilingue ?

C’est un corpus multilingue anglais/allemand. 
