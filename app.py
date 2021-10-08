from flask import Flask, flash, redirect, render_template, request, session, send_from_directory, Response, send_file
from cs50 import SQL
from flask_session import Session
from tempfile import mkdtemp
from datetime import datetime
import xlsxwriter
import os

app = Flask(__name__, static_folder='/project/excel')

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///database.db")


@app.route('/', methods=['GET', 'POST'])
def index():

    placas = request.form.get('placas')
    arreglo = request.form.get('arreglos')
    costo = request.form.get('costo')
    otros = request.form.get('otro')

    if request.method == 'POST':

        if not placas or not arreglo or not costo:
            flash('Ingrese todos los datos')
        else:
            db.execute("INSERT INTO arreglos (dia, placas, arreglo, otro, costo) VALUES (?,?,?,?,?)", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), placas, arreglo, otros, costo)

        arreglos = db.execute("SELECT * FROM arreglos WHERE placas = ?", placas)
        print(arreglos)

        return render_template('index.html', arreglos=arreglos)

    else:
        return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    placas = request.form.get('placas')
    if request.method == 'POST':
        arreglos = db.execute("SELECT * FROM arreglos WHERE placas = ?", placas)
        if len(arreglos) == 0:
            flash('Automovil no registrado')
            return render_template('download.html')


        workbook = xlsxwriter.Workbook('Arreglos.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', arreglos[0]['placas'])
        worksheet.write('A2', 'Dia')
        worksheet.write('B2', 'Arreglo')
        worksheet.write('C3', 'Otro')
        worksheet.write('C4', 'Costo')
        row = 1
        col = 0

        for i in arreglos:
          worksheet.write(row, col, i['dia'])
          worksheet.write(row, col+1, i['arreglo'])
          worksheet.write(row, col+2, i['otro'])
          worksheet.write(row, col+2, i['costo'])
          row += 1

        workbook.close()

        #return send_file (path, as_attachment=True)
        path = os.path.join(app.root_path)
        return send_from_directory(path, "Arreglos.xlsx")
        flash('Reporte generado')
    else:
        return render_template('download.html')
