# Vérifier si le répertoire .git/hooks existe
$gitHooksDir = ".git\hooks"
if (-Not (Test-Path $gitHooksDir)) {
    Write-Host "Le répertoire .git\hooks n'existe pas. Créez-le d'abord."
    exit 1
}

# Copier le fichier hooks.sh dans .git/hooks sous le nom pre-commit.sh
$sourcePath = "Hooks\hooks.sh"
$destPath = "$gitHooksDir\pre-commit"

# Vérifier si le fichier source existe
if (-Not (Test-Path $sourcePath)) {
    Write-Host "Le fichier source $sourcePath n'existe pas."
    exit 1
}

# Copier le fichier
Copy-Item -Path $sourcePath -Destination $destPath -Force

Write-Host "Le fichier a été copié avec succès à : $destPath"

