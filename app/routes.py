from app import app
from app.chords import *
from flask import render_template, flash, request
from app.calculator import Calculator

# @app.route('/index')
# def index():
# 	return render_template("base.html")

@app.route('/chords', methods=["GET", "POST"])
def chords():
	form = Chords()
	if request.method == "POST":
		result = cleanSong(searchSong(request.form.get("song", ""), request.form.get("artist", "")))
		return render_template("base.html", form=form, result=result)
	else:
		return render_template("base.html", form=form)
	
# def calculate():
# 	form = Calculator()
# 	result = int(request.form.get("number", 0)) + 2
# 	return render_template("base.html", form=form, result=result)
	