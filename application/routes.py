from flask import render_template

from application import app


def addition(a: int, b: int) -> int:
    """Retourne la somme de deux nombres."""
    # return a - b
    return a + b


def soustraction(a: int, b: int) -> int:
    """Retourne la difference entre deux nombres."""
    return a - b
    # return a + b


@app.route("/")
def index():
    result = addition(2, 5)
    result_sous = soustraction(2, 5)
    # app.logger.info(f"Résultat du calcul : {result}")

    return render_template("index.html", result=result, result_sous=result_sous)
