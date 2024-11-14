import os
import re
import sys


# Fonction pour vérifier la syntaxe d'un nom de fichier PDF
def is_valid_pdf_filename(filename):
    # Vérification de la taille du nom de fichier (au moins un caractère avant la version et l'extension)
    if not filename or len(filename) < 7:  # "vX.pdf" minimum
        print(f"Erreur : Le nom de fichier '{filename}' est trop court.")
        return False

    # Expression régulière pour la partie début (alphanumérique + underscores)
    # Cette partie s'applique au début du nom du fichier jusqu'à juste avant la version
    pattern_start = r'^[a-zA-Z0-9_]+'

    # Expression régulière pour la partie version à la fin du nom de fichier (ex. v1, v2, v3, ...)
    pattern_end = r'v\d+$'

    # Vérifier que la fin du fichier se termine bien par une version et une extension .pdf
    if not filename.endswith('.pdf'):
        print(f"Erreur : Le fichier '{filename}' doit se terminer par .pdf.")
        return False

    # Trouver la position de la version (avant .pdf)
    version_pos = filename.rfind('v')
    if version_pos == -1 or not re.match(pattern_end, filename[version_pos:]):
        print(f"Erreur : Le fichier '{filename}' doit contenir une version valide (ex. v1, v2, ...).")
        return False

    # Vérification du début du fichier avec l'expression régulière
    start_part = filename[:version_pos]  # Exclut la version
    if not re.match(pattern_start, start_part):
        print(
            f"Erreur : Le début du nom de fichier '{filename}' ne respecte pas la syntaxe (doit être alphanumérique et underscores).")
        return False

    # Vérification si le fichier existe réellement (facultatif)
    if not os.path.isfile(filename):
        print(f"Erreur : Le fichier '{filename}' n'existe pas.")
        return False

    return True


# Fonction principale qui vérifie la syntaxe des noms de fichiers
def check_filenames(filenames):
    invalid_files = []

    for filename in filenames:
        if not is_valid_pdf_filename(filename):
            invalid_files.append(filename)

    if invalid_files:
        print("\nFichiers invalides :")
        for file in invalid_files:
            print(f"- {file}")
    else:
        print("\nTous les fichiers ont une syntaxe valide.")


# Exemple d'utilisation
if __name__ == "__main__":
    # Liste des fichiers à vérifier
    files_to_check = [
        "rapport_2023_v1.pdf",  # Nom valide
        "document_important_v2.pdf",  # Nom valide
        "fichier_invalide_v@.pdf",  # Caractère non autorisé (@)
        "123_rapport_v.pdf",  # Pas de numéro de version
        "fichier_sans_extension",  # Pas d'extension .pdf
        "rapport_v3.pdf",  # Fichier valide mais sans préfixe
        "documentation_2024_vX.pdf",  # Version avec 'X' non valide (doit être un nombre)
        "",  # Fichier vide
        "document_v2.pdf"  # Correct
    ]

    # Vérifier la syntaxe des fichiers
    check_filenames(files_to_check)
#faire ta verif7
# lister les fichier
# vérifier leurs nom
# si qlq ne va pas, ok = False

    #sauvegarder un message d'erreur dans un fichier Hoks/message_erreur.txt
    #afficher ce que tu veux
    #raise Exception("Ca a pas marché")

