from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

# define route
# when / return index where name == Joe
@views.route("/")
def home():
  return render_template("index.html", name="Joe")



# user goes to this url, returns this where
  # name equals the value of username
  # pass in username
# @views.route("/profile/<username>")
# def profile(username):
#   return render_template("index.html", name=username)

@views.route("/profile")
def profile():
  args = request.args
  name = args.get('name')
  return render_template("index.html", name=name)


@views.route("/json")
def get_json():
  # json dictionary
  return jsonify({'name': 'tim', 'height': 7})


@views.route("/data")
def get_data():
  data = request.data
  return jsonify(data)


# page redirect
@views.route("/go-to-home")
def go_to_home():
  return redirect(url_for("views.home"))