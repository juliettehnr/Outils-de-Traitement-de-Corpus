## TP 1 - Partie 1 

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

5. Est un corpus monolingue ou multilingue ?

C’est un corpus multilingue anglais/allemand.


## TP 1 - Partie 2


1. Quel sujet allez vous traiter ?

Au début je voulais reprendre le même sujet sur lequel j'avais travaillé en Fouille de Texte (matière enseignée par Yoann Dupont), car ça m'aurait fait gagner du temps. On avait travailler en groupe sur un classifieur qui catégorise les discours des députés de l'Assemblée Nationale en fonction de leur orientations politiques. Mais pour ce projet, les données étaient en opensource donc pas besoin de faire de scraping. Or je voulais m'entraîner à faire du scraping. Donc je vais aussi faire un classifieur mais avec des données que j'aurais récupérées sur internet.

Le lien vers le projet de Fouille de Texte si ça vous intéresse : https://github.com/KerenDague/Fouille-de-textes

2. Quel type de tâche allez vous réaliser ?

Un classifieur qui catégorise les avis des lecteurs en fonction de s'ils sont positifs ou négatifs.

3. Quel type de données allez vous exploiter ?

Des avis lecteurs du livre 1984 de Georges Orwell.

4. Où allez vous récupérer vos données ?

Sur le site babelio.com.

5. Sont-elles libres d'accès ?

Elles ne sont pas libres de droit mais elles sont visibles par tous.
  
