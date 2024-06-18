from ext import app
from models import User, db, Product , Delivery
from flask import Flask, redirect, render_template
from forms import DeliveryForm, ProductForm, LoginForm, RegisterForm
from flask_login import login_user
from flask_login.mixins import AnonymousUserMixin


@app.route("/")
def index():
        return render_template("index.html")

@app.route("/main")
def main():
        return render_template("main.html")

@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
        user = User.query.get(user_id)

        db.session.delete(user)
        db.session.commit()

        return redirect("/register")


@app.route("/log_in", methods = ["GET", "POST"])
def login():
        form = LoginForm()
        if form.validate_on_submit():
                user = User.query.filter(User.username == form.username.data).first()
                if user and user.password == form.password.data:
                        login_user(user)
                        print('123')
                        return redirect("main")
        return render_template("log_in.html", form=form)

@app.route("/register", methods = ["GET", "POST"])
def register():
        form = RegisterForm()
        if form.validate_on_submit():
                new_users = User(username = form.username.data, password = form.password.data,birthday = form.birthday.data)

                db.session.add(new_users)
                db.session.commit()
                current_user = new_users
                print(current_user)
                return redirect("/main")
        print(form.errors)
        return render_template("register.html", form= form)

@app.route("/delivery", methods = ["GET", "POST"])
def delivery():
        form = DeliveryForm()
        if form.validate_on_submit():
                delivery_users = Delivery(name = form.name.data, lastname = form.lastname.data, email = form.email.data, phone_number = form.phone_number.data, country = form.country.data, city = form.city.data, address = form.address.data, post_code = form.post_code.data)

                db.session.add(delivery_users)
                db.session.commit()

                print(form.errors)
        return render_template("delivery.html", form=form)






@app.route("/register_users")
def register_users():
        register_users = User.query.all()
        return render_template("users.html", register_users = register_users)




@app.route("/add_products", methods = ["GET", "POST"])
def add_products():
        form = ProductForm()
        if form.validate_on_submit():
                new_product = Product(name = form.name.data, price = form.price.data, country = form.country.data)

                db.session.add(new_product)
                db.session.commit()
        print(form.errors)
        return render_template("products.html", form=form)









@app.route("/products")
def new_products():
        new_products = Product.query.all()
        return render_template("index.html", new_products = new_products)

@app.route("/delete_product/<int:new_product_id>")
def delete_product(new_product_id):
        product = Product.query.get(new_product_id)

        db.session.delete(product)
        db.session.commit()

        return redirect("/products")