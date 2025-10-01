from invoke import task

@task
def lint(c):
    print("Vérification du code...")
    c.run("flake8 application")
    c.run("black --check application")
    c.run("isort --check-only application")

@task
def format(c):
    print("Formatage automatique...")
    c.run("black application")
    c.run("isort application")

@task
def test(c):
    print("Lancement des tests...")
    c.run("pytest -v")

@task(pre=[lint, test])
def build(c):
    print("Build réussi !")

@task(pre=[lint, test, build])
def all(c):
    print("Tout est OK !")
