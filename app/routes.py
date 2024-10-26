from flask import render_template, request, flash, redirect, url_for
from app import app, db, models
from app.forms import AddCampaign, DeleteCampaign
import sqlalchemy as sa
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    campaigns = models.Campaign.query.all()
    datasets = models.Dataset.query.all()
    return render_template("index.html", campaigns = campaigns, datasets=datasets)

@app.route("/campaigns/<id>")
@app.route("/campaigns", methods = ["GET", "POST"] )
def campaigns(id=None):
    form = AddCampaign()
    if form.validate_on_submit():
        print(form.start_date.data)
        campaign = models.Campaign(name=form.name.data, exp_range = form.exp_range.data, start_date=form.start_date.data)
        db.session.add(campaign)
        db.session.commit()
        flash("New campaign added")
        return redirect(url_for("campaigns"))
    if id:
        campaigns = models.Campaign.query.filter_by(id=id).all()
        return render_template("campaigns.html", campaigns=campaigns, form=form, campaign_group=False)
    
    campaigns = models.Campaign.query.all()
    return render_template("campaigns.html", campaigns=campaigns, form=form, campaign_group=True)

@app.route("/datasets/<id>")
@app.route("/datasets")
def datasets(id=None):
    campaigns = models.Campaign.query.all()
    if id:
        datasets = models.Dataset.query.filter_by(id=id).all()
        return render_template("datasets.html", datasets=datasets, campaigns = campaigns)
    
    datasets = models.Dataset.query.all()
    return render_template("datasets.html", datasets=datasets, campaigns=campaigns)