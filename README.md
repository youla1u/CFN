# CFN-

Le fichier Python 'YOULA_Parse_CNF.py' fournit les informations suivates: 

le nom d'une instance, le nombre de variables, le nombre de clauses, le nombre 
et la proportion de clauses binaires, de Horn, reverse horn.

Aussi il permet de convertir une formule en forme CNF puis l'affiche au format Dimacs.

----------------------------
Les formule à analyser est écrite en en utilisant ~ pour la négation, | pour la disjonction 
et & pour la conjonction. Exemple: (~a | b)& (~b | c) & (~c | ~ a) & (a | ~d | f)
où les ltetres représentent les variables.
----------------------------

Pour lancer une analyse d'une formule il suffit d'exécuter l'ensemble du fichier YOULA_Parse_CNF .py
,car il contient une foncition main, puis de saisire la fonction que l'on souhaite  analyser.
Nb: saisir unique ment la formule sans la mettre entre " " ou sair l'espace à la fin de lasaisie.  
