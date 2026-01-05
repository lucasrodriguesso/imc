from flask import Flask, render_template, request
from app.imc import calcul_imc, categorie_imc
from app.pdf_report import generate_pdf

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    imc = None
    categorie = None

    if request.method == "POST":
        poids = float(request.form["poids"])
        taille = float(request.form["taille"])

        imc = calcul_imc(poids, taille)
        categorie = categorie_imc(imc)

        # Si bouton "Générer PDF"
        if "pdf" in request.form:
            generate_pdf(poids, taille, imc, categorie)

    return render_template("index.html", imc=imc, categorie=categorie)

if __name__ == "__main__":
    app.run(debug=True)
