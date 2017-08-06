"""

This file is the place to write solutions for the
practice part of skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes by just their
class name (and not model.ClassName).

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter(Brand.brand_id == 'ram').first()
# shorter alternative -- Brand.query.get('ram')
# another alternative -- db.session.query(Brand).filter(Brand.brand_id == 'ram').first()
# sticking with .filter because statement more explicit (I like Brand.brand_id vs. brand_id)

# Get all models with the name ``Corvette`` and the brand_id ``che``.
# chose & because it looks cleaner vs. , separation
q2 = Model.query.filter((Model.name == 'Corvette') & (Model.brand_id == 'che')).all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
# Used .is_(None) vs. == None to avoid "!" warning in Sublime even though != looks nicer
q6 = Brand.query.filter((Brand.founded == 1903) & (Brand.discontinued.is_(None))).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded before 1950.
# Used .isNot(None) vs. != None to avoid "!" warning in Sublime even though != looks nicer
q7 = Brand.query.filter((Brand.discontinued.isnot(None)) | (Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != 'for').all()

# -------------------------------------------------------------------
# Part 3: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    #--- layout example ---
    # Model name | Brand name | Brand HQ

    # get all model objects of that particular year
    models_info = Model.query.filter(Model.year == year).all()

    for model in models_info:
        print "Model name: {} | Brand name: {} | Brand HQ: {}".format(
            model.name, model.brand.name, model.brand.headquarters)


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    #--- layout example ---
    #brand name: (new line)
        #(tab) model name | model year (new line)
    #brand2 name: (new line)
        #(tab) model name | model year (new line)

    brands_summary = Brand.query.all()  # get all brand objects

    for brand in brands_summary:
        print "Brand name: {} \n\t".format(brand.name)  # get each brand name
        #possibly more than 1 model per brand; need to loop through each model
        for model in brand.models:
            #get each model's name and year
            print "Model name: {} | Year: {} \n".format(model.name, model.year)


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    # reformat input to be used inside query filter
    mystr = '%' + mystr + '%'

    return Brand.query.filter(Brand.name.like(mystr)).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter((Model.year > start_year) & (Model.year < end_year)).all()
