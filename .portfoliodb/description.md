---
made with: [python]
tags: [automation, program, cli]
created: 2021-04-14
layout:
  - p1
  - [m1, m2]
  - [m3, p2]
  - p3
  - m4
  - [p4, l1]
colors:
  primary: black
  secondary: white
thumbnail: ../demo.gif
---

# wikitrad

:: fr

Parfois, un nom propre, un terme technique échappe aux algorithmes de [Google Traduction](https://translate.google.com) ou [DeepL](https://deepl.com).

![interface de Google Traduction, montrant Spirited Away traduit en enlevée comme par enchantement](google-translate.png "Google Traduction ne traduit pas les noms de films par leur version dans la langue cible")

![interface de DeepL, montrant spirited away traduit en emmené loin et Spirited Away (avec des majuscules) laissé tel quel](deepl.png "DeepL ne traduit pas les noms propres non plus")

J'ai trouvé un autre moyen de traduires ces termes: Wikipédia: des millions d'articles dans des centaines de langues, avec un lien pour changer celle-ci sur chaque page.

![article du Wikipédia anglais sur Spirited Away, ainsi qu'un lien vers la version française de l'article, montrant Le Voyage de Chihiro — French comme titre](wikipedia.png "Wikipédia possède des liens vers d'autres articles sur le même sujet dans d'autres langues")

J'ai donc créer ce petit outil pour automatiser la tâche: chercher un article dans la langue source, récupérer le lien vers ce même article dans la langue cible, et enfin récupérer le titre du nouvel article.

![Un utilisateur tape dans un terminal “wikitrad "spirited away" fr”, et reçoit en réponse “Le Voyage de Chihiro”](../demo.gif "Exemple d'utilisation pour la traduction d'un titre de film")

Il utilise aussi [langdetect](https://pypi.org/project/langdetect) pour détecter la langue source, si celle-ci n'est pas explicitement donnée.

[Code source](https://github.com/ewen-lbh/wikitrad)

:: en

Sometimes, a proper noun or a technical term fails to be translated using [Google Translate](https://translate.google.com) or [DeepL](https://deepl.com).

![Google Translate's interface, showing Spirited Away translated as enlevée comme par enchantement](google-translate.png "Google Traduction doesn't translate movie titles to their versions in the target language")

![DeepL's interface, showing spirited away translated as emmené loin and Spirited Away (with uppercase letters) left untranslated](deepl.png "DeepL does not translate proper nouns either")

I found another way to translate those terms: Wikipedia, which has millions of articles in hundreds of languages, all with links to read the page in another language.

![English Wikipedia article on Spirited Away, as well as a link to the article's french version, showing Le Voyage de Chihiro — French as a title](wikipedia.png "Wikipedia has links to other articles on the same topic in other languages")

I therefore created this little command-line program to automate the task: look for a page in the source language, get the link to the target language's article, get that article's title.

![A user types in a terminal window “wikitrad "spirited away" fr” and receives as an answer “Le Voyage de Chihiro”](../demo.gif "Example use case for the translation of a movie’s title")

I also used [langdetect](https://pypi.org/project/langdetect) to determine the source language, in case it isn't provided by the user.

[Source code](https://github.com/ewen-lbh/wikitrad)
