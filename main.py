from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('progetto2.html')

@app.route('/cart')
def cart():
    return render_template('cart2.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/ordine')
def ordine():
    return render_template('Ordine.html')

if __name__ == '__main__':
    app.run(debug=True, port=5038)