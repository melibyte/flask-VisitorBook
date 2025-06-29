from flask import Flask , request , render_template
import json
from datetime import datetime
import uuid

app = Flask(__name__)   

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    entry = {
        "id": str(uuid.uuid4()),       #Unique id for each record
        "name": request.form['name'],
        "email": request.form['email'],
        "location": request.form['location'],
        "subject": request.form['subject'],
        "message": request.form['message'],
        "rating": request.form['rating'],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)

    return render_template('greet.html', name=entry["name"])

@app.route('/history')
def history():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    return render_template('history.html', data=data)

@app.route('/delete/<id>')
def delete_entry(id):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    # Find the record to delete.
    deleted_entry = None
    new_data = []
    for entry in data:
        if entry['id'] == id:
            deleted_entry = entry
        else:
            new_data.append(entry)

    # Save current list.
    with open('data.json', 'w') as f:
        json.dump(new_data, f, indent=2)

    # Write deleted record to trash.
    if deleted_entry:
        try:
            with open('trash.json', 'r') as f:
                trash = json.load(f)
        except FileNotFoundError:
            trash = []
        trash.append(deleted_entry)
        with open('trash.json', 'w') as f:
            json.dump(trash, f, indent=2)

    return render_template('deleted.html', entry=deleted_entry)

@app.route('/undo/<id>')
def undo(id):
    try:
        with open('trash.json', 'r') as f:
            trash = json.load(f)
    except FileNotFoundError:
        trash = []

    restored = None
    new_trash = []
    for entry in trash:
        if entry['id'] == id:
            restored = entry
        else:
            new_trash.append(entry)

    if restored:
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        data.append(restored)
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=2)

    # Update trash.
    with open('trash.json', 'w') as f:
        json.dump(new_trash, f, indent=2)

    return render_template('greet.html', name=restored['name'] if restored else 'Ziyaretçi')

if __name__ == '__main__':
    app.run(debug=True)

















#Flask(__name__): Uygulamayı başlatır ve dosyanın yol bilgisini verir.
# @app.route('/'): Tarayıcıda http://localhost:5000/ isteği geldiğinde hello() fonksiyonunu çalıştırır.
# app.run(debug=True): Geliştirme sunucusunu debug modda ayağa kaldırır (kod değişince otomatik yeniden başlatma ve hata sayfası).
# “Bu kod, gelen HTTP GET isteklerini yakalar ve ona karşılık olarak ekrana ‘Merhaba, Flask!’ yazdırır.” Debug modu, geliştirme sürecini hızlandıran – ancak prod’da (canlıda) kapatılması gereken – bir kolaylıktır.
