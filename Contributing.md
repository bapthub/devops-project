# Guide de Contribution

## Préambule

Merci de votre intérêt pour notre projet !
Si vous souhaitez y contribuer, vous êtes au bon endroit !
Ce document a pour but de vous guider tout au long du processus de contribution. N'hésitez pas à contacter l'équipe de développement si vous souhaitez l'intégrer ou si vous avez la moindre question.

## Travailler en multibranche

Nous utilisons le modèle de développement Git multi-branche. Cela signifie que chaque fonctionnalité, correctif ou autre forme de contribution doit se faire dans une nouvelle branche. Les branches principales ne doivent jamais recevoir de commit directement.

Pour commencer à travailler sur une nouvelle contribution, créez d'abord une nouvelle branche depuis la branche de développement principale avec un nom qui décrit le travail que vous allez réaliser. Par exemple, si vous travaillez sur un correctif de bug pour le bouton de login, vous pourriez nommer votre branche `fix/login-button`.

Une fois que vous avez terminé votre travail sur votre branche, vous devez ouvrir une Merge Request (MR) vers la branche de développement principale. Ne fusionnez jamais directement votre branche avec la branche de développement principale.

Votre MR sera alors examinée par d'autres membres de l'équipe. Selon leurs commentaires, vous devrez peut-être faire des modifications supplémentaires à votre branche avant qu'elle ne soit fusionnée.

## Mettre à jour la documentation

Chaque fois que vous faites des modifications qui affectent le fonctionnement du projet, il est crucial de mettre à jour la documentation en conséquence. Cela peut être des commentaires dans le code, mais aussi la documentation du projet externe.

Nous utilisons Overleaf pour notre documentation. Vous recevrez un lien privé pour y accéder et la modifier. Veillez à toujours garder cette documentation à jour avec vos modifications.

## Proposer de nouvelles technologies

Nous sommes toujours à la recherche de moyens d'optimiser notre code. Si vous avez des suggestions de nouvelles technologies qui pourraient être bénéfiques pour le projet, n'hésitez pas à les proposer. Vous pouvez le faire en ouvrant une issue sur GitHub, en décrivant la technologie et comment elle pourrait améliorer le projet.

Veuillez noter que la décision d'adopter une nouvelle technologie ne sera pas prise à la légère. Elle sera soumise à un examen approfondi par l'équipe de développement et nécessitera un consensus avant d'être adoptée.

## Etapes à suivre

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)

## Installation

Pour installer ce projet sur votre machine, vous placer dans le répertoire de votre choix puis entrer :
```
git clone git@gitlab.com:bapthub/devops-final-project.git
```

Sinon pour connecter votre repository local existant à ce Gitlab, entrez les commandes suivantes :

```
cd existing_repo
git remote add origin https://gitlab.com/bapthub/devops-final-project.git
git branch -M main
git push -uf origin main
```

## Utilisation

Pour faire tourner l'application, vous pouvez lancer la commande 'run' une fois dans le répertoire.

Pour arrêter l'application, lancer la commande 'down' ou 'kill'.

## Contribuer

Enfin pour contriber au projet voici un exemple de commandes pour créer une branche :

```
git checkout -b ma-branche-de-travail
```

Y ajouter des modifications :

```
git add fichier-modifié
```

Décrire et enregistrer ces modifications en local :

```
git commit -m "Description de mes modifications"
```

Enregistrer les modifications sur le dépot distant :

```
git push origin ma-branche-de-travail
```

Puis envoyer une requête de "merge" sur la branche principale qui devra être étudiée par les autres membres de l'équipe.
Cette requête peut se faire via l'interface Gitlab en créant une Merge Request.
