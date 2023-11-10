from flask import render_template , redirect , request , session

from recipes_app import app

from recipes_app.models.user_model import User
from recipes_app.models.recipe_model import Recipe





@app.route('/dashboard')
def welcome():
    if not 'user_id' in session:
        return redirect('/')
    user = User.show_name(session['user_id'])
    all_recipes = Recipe.show_all()
    return render_template('dashboard.html' , user = user, all_recipes = all_recipes )


@app.route('/recipe/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('recipes_new.html')

@app.route('/recipe/create', methods = ['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.is_valid(request.form):
        return redirect('/recipe/new')
    recipe_data = {
        **request.form,
        'user_id': session['user_id']
    }
    
    Recipe.create(recipe_data)
    return redirect('/dashboard')

@app.route('/recipe/<int:id>/delete')
def delete_recipe(id):
    data = {
        ** request.form,
        'id' : id
    }
    Recipe.delete(data)
    return redirect('/dashboard')

@app.route('/recipe/<int:id>/edit')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        'id' :id  
    }
    user = User.show_name(id)
    return render_template('recipes_edit.html', recipe = Recipe.get_one(data), user = user)

@app.route('/recipe/<int:id>/update', methods=['POST'])
def edit_recipe(id):
    data = {
        **request.form,
        'id' : id
    }
    if not Recipe.is_valid(request.form):
        return redirect(f'/recipe/{id}/edit')
        
    Recipe.save(data)
    
    return redirect('/dashboard')



@app.route('/recipe/<int:id>/view')
def view(id):
    if 'user_id' not in session:
        return redirect('/dashboard')
    
    data = {
        'id' : id
    }
    user = User.show_name(session['user_id'])
    recipe = Recipe.get_one(data)
    return render_template('recipes_view.html',recipe = recipe , user = user)