from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Promoción de la Tienda</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .promo-img {
            width: 100%;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        h1, p {
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <img class="promo-img" src="https://edit.org/img/blog/hrr-plantillas-moda-ropa-complementos-diseno-editar-editable-editor-carteles-marketing-comunicacion-personalizable.webp" alt="Promoción de la Tienda">
        <h1>¡Gran Promoción en Nuestra Tienda!</h1>
        <p>Aprovecha nuestros descuentos especiales en una amplia variedad de productos. Solo por tiempo limitado, ¡no te lo pierdas!</p>
        <p>Visítanos en nuestra tienda física o realiza tu compra en línea.</p>
        <p>¡Te esperamos!</p>
    </div>
</body>
</html>
    '''


if __name__ == "__main__":
    app.run(debug=True)
