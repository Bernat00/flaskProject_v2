from flask import Flask, render_template, request, url_for, redirect
import foods

app = Flask(__name__)

foods_path = foods.foods_path


@app.route('/')
def etlap():
    etelek = foods.load(foods_path)

    return render_template('home.html', etelek=etelek)


@app.route('/add', methods={'GET', 'POST'})
def uj_etel():
    if request.method == "POST":
        name = request.form["name"]
        leiras = request.form["leiras"]
        allergen = request.form["allergen"]
        valami = [name, leiras, allergen]
        foods.add(valami)
    return render_template('add.html')


@app.route('/edit', methods={'GET', 'POST'})
def edit_etel(is_add=False, etelek=None, who_is_edited=None, errors=None):
    if etelek is None:
        etelek = foods.kajak

    return render_template('edit.html', etelek=etelek, is_add=is_add, errors=errors)


@app.route('/edit/change/<int:food_id>', methods={'GET', 'POST'})
def edit_change(food_id):
    data = foods.load(foods_path)
    errors = None

    if request.method == 'POST':
        name = request.form['name']
        leiras = request.form['leiras']
        allergen = request.form['allergen']
        data = {'nev': name, 'leiras': leiras, 'allergen': allergen}
        errors = foods.error_handling(data)
        if errors is None:
            foods.change(foods_path, food_id, data)
            food_id = None

    print(url_for('etel_del', food_nev='hamburger'))

    return edit_etel(is_add=False, etelek=data, who_is_edited=food_id, errors=errors)


@app.route(f'/edit/del/<food_nev>', methods={'POST'})
def etel_del(food_nev):
    foods.delete(foods_path, food_nev)
    return redirect(url_for('edit_etel'))


@app.route('/edit/add', methods={'GET', 'POST'})
def etel_add():
    if request.method == "POST":
        nev = request.form["name"]
        leiras = request.form["leiras"]
        allergen = request.form["allergen"]
        data = [nev, leiras, allergen]
        if foods.error_handling(data) is None:
            foods.add(data)
        return edit_etel(errors=foods.error_handling(data))  # kéne ilyen több helyre is és az alert
    return edit_etel(is_add=True)


# @app.route(f'edit/{változó}')


# password,urlrandomization

if __name__ == '__main__':
    app.run()
