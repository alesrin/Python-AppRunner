from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")

        numero1 = float(request.form.get("numero1"))
        numero2 = float(request.form.get("numero2"))

        suma = numero1 + numero2
        resta = numero1 - numero2
        producto = numero1 * numero2
        division = numero1 / numero2 if numero2 != 0 else "Error: División por cero"

        saludo = f"Hola, {nombre} {apellido}! Es un placer saludarte."

        return render_template("resultado.html", saludo=saludo, suma=suma, resta=resta, producto=producto, division=division)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
