from invoke import task

@task
def lint(c):
    """Vérifie le code sans le corriger."""
    print("Vérification du code...")
    c.run("flake8 application")  # signale les erreurs restantes
    c.run("black --check application")
    c.run("isort --check-only application")

@task
def format(c):
    """Corrige automatiquement le code et les imports."""
    print("Formatage automatique...")
    c.run("black application")       # reformate le code
    c.run("isort application")       # réorganise les imports

@task
def test(c):
    """Lance les tests pytest."""
    print("Lancement des tests...")
    c.run("pytest -v")

@task(pre=[format, test])
def build(c):
    """Build (fictif) après correction et tests."""
    print("Build réussi !")

@task(pre=[format, test, build])
def all(c):
    """Tout corriger, tester et build."""
    print("Tout est OK !")
