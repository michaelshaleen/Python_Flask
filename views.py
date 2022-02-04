from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

# define route
# when / return index where name == Joe
@views.route("/")
def home():
  return render_template("index.html", name="Joe")



# user goes to this url, returns this where
  # name equals the value of username
@views.route("/profile/<username>")
def profile(username):
  return render_template("index.html", name=username)
