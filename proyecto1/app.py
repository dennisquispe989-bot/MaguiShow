from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/contacto', methods=['POST'])
def contacto():
    nombre = request.form['nombre']
    mensaje = request.form['mensaje']
    return f"¡Gracias {nombre}! Te responderemos pronto 🎉"

if __name__ == '__main__':
    app.run(debug=True)
   