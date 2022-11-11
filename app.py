from flask import Flask, render_template, request, redirect, flash
from forms import AddPetForm, EditPetForm
from models import Pet, db, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)
connect_db(app)



@app.route('/')
def show_all_available_pets():
    """Shows all available pets"""

    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)

@app.route('/add', methods=["POST", "GET"])
def add_pet_form():
    """Shows edit form and save a new pet in DB"""

    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(name = form.name.data,
                    species = form.species.data,
                    photo = form.photo.data,
                    age = form.age.data,
                    notes = form.notes.data)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')
    else:
        flash('Could not validate')
        return render_template('add_pet.html', form = form)

@app.route('/<int:id>', methods=["POST", "GET"])
def pet_details(id):
    """Shows details about the pet"""

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    print(pet.notes)

    if form.validate_on_submit():
        print("----------Yes___________")
        pet.photo = form.photo.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        print(f'-----------------{pet.notes}')
        db.session.commit()

        return redirect('/')
    else:
        print("------no-------")
        return render_template('details.html', pet=pet, form=form)

