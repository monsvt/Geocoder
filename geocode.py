
from flask import Flask, render_template, request,send_file
#from flask_sqlalchemy import SQLAlchemy
#from locate import coordenadas #coordenadas, df
import pandas
from geopy.geocoders import ArcGIS
from werkzeug import secure_filename


app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST','GET'])
def success():
    global archivo
    if request.method=='POST':
        archivo=request.files["Myfile"]
        archivo.save(secure_filename(archivo.filename))
        df=pandas.read_csv(archivo.filename)
        try:
            if df.address.all:
                df.rename(columns={'address':'Address'},inplace=True)
        except:
            pass
      
        nom=ArcGIS()
        df["Coordinates"]= df["Address"].apply(nom.geocode)
        df["Latitude"]=df["Coordinates"].apply(lambda x:x.latitude if x != None else None)
        df["Longitude"]=df["Coordinates"].apply(lambda x:x.latitude if x != None else None)
        df.drop(columns="Coordinates",inplace=True)
        return render_template("success.html", tables=[df.to_html(classes='data')], titles=df.columns.values, btn="download.html")
    #return render_template("index.html", text= "Sorry, seems like something went wrong!")
        if df.Address == None:
            print("Please make sure you have a column name Address or address")

@app.route("/download")
def download():
    return send_file(archivo.filename, attachment_filename="yourfile.xlsx", as_attachment=True)

if __name__=='__main__':
    app.debug= True
    app.run()
