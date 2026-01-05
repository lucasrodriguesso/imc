from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date


def generate_pdf(output_path="rapport_imc.pdf"):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Rapport de suivi minceur")
    y -= 40

    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Généré le : {date.today()}")
    y -= 40

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Journal de suivi")
    y -= 25

    journal = [
        ("2025-03-01", 80, 26.12, "Surpoids"),
        ("2025-04-01", 78, 25.47, "Surpoids"),
        ("2025-05-01", 75, 24.49, "Poids normal"),
    ]

    c.setFont("Helvetica", 10)
    for d, poids, imc, cat in journal:
        c.drawString(60, y, f"{d} | {poids} kg | IMC {imc} | {cat}")
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Synthèse calories")
    y -= 20

    calories = {
        "2025-03-01": 1300,
        "2025-04-01": 650,
        "2025-05-01": 550
    }

    c.setFont("Helvetica", 10)
    for d, cal in calories.items():
        c.drawString(60, y, f"{d} : {cal} kcal")
        y -= 15

    c.save()
    print(f"PDF généré : {output_path}")


if __name__ == "__main__":
    generate_pdf()
