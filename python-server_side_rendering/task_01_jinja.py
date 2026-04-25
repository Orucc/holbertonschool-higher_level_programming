#!/usr/bin/python3
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# YENİ ƏLAVƏ EDİLƏN HİSSƏ BURADAN BAŞLAYIR
@app.route('/items')
def items_list():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items = []
        
    return render_template('items.html', items=items)
# YENİ ƏLAVƏ EDİLƏN HİSSƏ BURADA BİTİR

if __name__ == '__main__':
    app.run(debug=True, port=5000)
