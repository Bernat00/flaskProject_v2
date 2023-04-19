data = ['no']
        for key in request.form:
            if key == 'edit.change':
                for etel in etelek:
                    if etel['id'] == int(request.form["edit.change"]):
                        etel['is_edit'] = True

        for a in request.form:
            if a == 'edit.del':
                for etel in etelek:
                    if etel['id'] == int(request.form["edit.del"]):
                        foods.delete(foods_path, etel['nev'])

        for b in request.form:
            if b.startswith('save.'):
                if b == 'save.id':
                    data = ['yes', request.form[b]]
                if b == 'save.name':
                    data.append(request.form[b])
                if b == 'save.leiras':
                    data.append(request.form[b])
                if b == 'save.allergen':
                    data.append(request.form[b])

        if data[0] == 'yes':
            del data[0]
            food_id = data.pop(0)
            foods.change(foods_path, food_id, data)