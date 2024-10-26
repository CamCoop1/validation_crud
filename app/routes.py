from flask import render_template, request
from app import app, models

@app.route('/')
@app.route('/index')
def index():
    campaigns = models.Campaign.query.all()
    datasets = models.Dataset.query.all()
    return render_template("index.html", campaigns = campaigns, datasets=datasets)

@app.route("/campaigns/<id>")
@app.route("/campaigns")
def campaigns(id=None):
    if id:
        campaigns = models.Campaign.query.filter_by(id=id).all()
        return render_template("campaigns.html", campaigns=campaigns, single_view = True)
    
    campaigns = models.Campaign.query.all()
    return render_template("campaigns.html", campaigns=campaigns)

@app.route("/datasets/<id>")
@app.route("/datasets")
def datasets(id=None):
    campaigns = models.Campaign.query.all()
    if id:
        datasets = models.Dataset.query.filter_by(id=id).all()
        return render_template("datasets.html", datasets=datasets, campaigns = campaigns)
    
    datasets = models.Dataset.query.all()
    return render_template("datasets.html", datasets=datasets, campaigns=campaigns)