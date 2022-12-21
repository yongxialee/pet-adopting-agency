from flask import Flask,request ,render_template,redirect,session,flash,url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db,Pet
from forms import AddPetForm,EditPetForm
# from forms import 

app = Flask(__name__)
# i need you to talk to postgresql using database movies_example
app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///employees_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "ThisisHappyyuy123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
debug = DebugToolbarExtension(app)
app.debug = True
app.app_context().push()
# call connect_db
connect_db(app)
db.create_all()
# toolbar=DebugToolbarExtension(app)
@app.route('/')
def home_page():
    """show a page of the list of pets"""
    pets=Pet.query.all()
    
    return render_template('list_pets.html',pets=pets)
@app.route('/add', methods=["GET","POST"])
def add_pets():
    form = AddPetForm()
    
    
    # if it's a post request? and is a valid token
    if form.validate_on_submit():
        # data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        # new_pet = Pet(**data)
        name=form.name.data
        species= form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data
        new_pet =Pet(name=name,species=species,photo_url=photo_url,
                     age=age,notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} is added")
        return redirect(url_for('home_page'))
    
    else: 
        return render_template('add_pet_form.html', form =form)
    
@app.route('/<int:pet_id>', methods=["GET","POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('home_page'))

    else:
        # failed; re-present form for editing
        return render_template("pet_edit_form.html", form=form, pet=pet)
    
    
