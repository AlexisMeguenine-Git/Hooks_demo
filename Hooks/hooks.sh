#!/bin/sh

# Exécution d'un script Python
python Hooks/script.py

# Si le script échoue (retourne un code non zéro), annulez le commit
if [ $? -ne 0 ]; then
  echo "Le script Python a échoué. Commit annulé."
  exit 1
fi