import math
from flask import Flask, request, render_template
import os

app = Flask(__name__)
categories = {'Самосвал': 1000, 'Эскаватор': 2000, 'Погрузчик': 3000, 'Трактор': 500}

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/form')
def form():
    return render_template('form.html')  

@app.route('/submit', methods=['POST'])
def submit():
    file_details = None

    form_data = request.form
    # Get the uploaded file
    pdf_file = request.files.get('pdf')
    category_name = request.form.get('category')
    day_cost = categories[category_name]
    cost = math.ceil((1 + int(request.form.get('advance'))/100) * int(request.form.get('rental_rate')) * int(day_cost))

    if pdf_file:
        file_size = len(pdf_file.read())  
        pdf_file.seek(0)  # Reset file pointer
    
        file_details = {'name': pdf_file.filename, 'size': file_size}

    return render_template('result.html', form_data=form_data, file_details=file_details, cost=cost)

if __name__ == '__main__':
    app.run(debug=True)
