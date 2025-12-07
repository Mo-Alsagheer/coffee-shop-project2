from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database connection
def get_db():
    conn = sqlite3.connect("cafe.db")
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn


# ----- Home Page ----- #
@app.route("/")
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM food_menu")
    food_menu = cursor.fetchall()
    db.close()
    return render_template("index.html", foodMenu=food_menu)


# ----- Food Details Page ----- #
@app.route("/foodDetails/<int:id>")
def foodDetails(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM food_menu WHERE id = ?", (id,))
    food = cursor.fetchone()
    db.close()

    if food:
        return render_template("foodDetails.html", food=food)
    return "Can't found this meal."


# ---- Admin Food List Page ----- #
@app.route("/admin/foodList")
def foodList():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM food_menu")
    foodMenu = cursor.fetchall()
    db.close()
    return render_template("foodList.html", foodMenu=foodMenu)


# ----- Admin Add Food Page ----- #
@app.route("/admin/addFood", methods=["GET", "POST"])
def addFood():
    if request.method == "GET":
        return render_template("addFood.html")

    elif request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        description = request.form["description"]
        image_url = request.form["image_url"]

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO food_menu (name, price, description, image_url) VALUES (?, ?, ?, ?)",
            (name, price, description, image_url),
        )

        db.commit()
        db.close()
        return redirect("/admin/foodList")

# ----- Admin Edit Food Page ----- #
@app.route("/admin/editFood/<int:foodID>", methods=["GET", "POST"])
def editFood(foodID):
    db = get_db()
    cursor = db.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM food_menu WHERE id = ?", [foodID])
        food = cursor.fetchone()
        db.close()
        return render_template("editFood.html", food=food)

    elif request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        description = request.form["description"]
        image_url = request.form["image_url"]

        cursor.execute(
            """
            UPDATE food_menu 
            SET name = ?, 
            price = ?, 
            description = ?, 
            image_url = ? 
            WHERE id = ?
        """,
            [name, price, description, image_url, foodID],
        )
        db.commit()
        db.close()
        return redirect("/admin/foodList")


# ----- Delete Food ----- #
@app.route("/admin/deleteFood/<int:foodID>")
def deleteFood(foodID):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM food_menu WHERE id = ?", [foodID])
    db.commit()
    db.close()
    return redirect("/admin/foodList")


if __name__ == "__main__":
    app.run(debug=True, port=5000)













