from flask import Flask, render_template, request, url_for, redirect
import foods

app = Flask(__name__)

foods_path = 'templates/foods.csv'


@app.route('/')
def etlap():
    etelek = foods.load(foods_path)

    return render_template('home.html', etelek=etelek)


@app.route('/add', methods={'GET', 'POST'})
def uj_etel():
    if request.method == "POST":
        nev = request.form["name"]
        leiras = request.form["leiras"]
        allergen = request.form["allergen"]
        valami = [nev, leiras, allergen]
        foods.add(foods_path, valami)
    return render_template('add.html')


@app.route('/edit', methods={'GET', 'POST'})
def edit_etel(is_add=False, is_edit=False, etelek=None):
    if etelek is None:
        etelek = foods.load(foods_path)

    for etel in etelek:
        etel['is_edit'] = False

    if request.method == "POST":
        try:
            for etel in etelek:
                if etel['id'] == int(request.form["edit.change"]):        #ez még mindig nem túl jó
                    etel['is_edit'] = True

        except:...
        try:
            edit_change()
            return redirect(url_for('edit_etel'))
        except:...
    # return render_template(url_for(etel_add))

    return render_template('edit.html', etelek=etelek, is_add=is_add, is_edit=is_edit)


def edit_change():
    save_id = request.form['id']
    name = request.form['name']
    leiras = request.form['leiras']
    allergen = request.form['allergen']
    data = [name, leiras, allergen]

    foods.change(foods_path, save_id, data)


@app.route('/edit/add', methods={'GET', 'POST'})
def etel_add():
    if request.method == "POST":
        nev = request.form["name"]
        leiras = request.form["leiras"]
        allergen = request.form["allergen"]
        data = {'name':nev,
                  'leiras': leiras,
                  'allergen': allergen}
        if foods.error_handling(data) is None:
            foods.add(foods_path, data)
        return edit_etel(error=foods.error_handling(data)) #kéne ilyen több helyre is és az alert
    return edit_etel(True)


# @app.route(f'edit/{változó}')


# password,urlrandomization

if __name__ == '__main__':
    app.run()
