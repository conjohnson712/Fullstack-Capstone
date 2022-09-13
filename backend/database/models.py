import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    # add one demo row which is helping in POSTMAN test
    nanodegree = Nanodegree(
        title='Introduction to Computer Basics',
        path='[{"name": "Introduction to Programming Basics", "courses": "3", "weeks": 6, "difficulty": 1}]'
    )


    nanodegree.insert()


# ROUTES

'''
Nanodegree
a persistent nanodegree entity, extends the base SQLAlchemy Model
'''


class Nanodegree(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    # String Title
    title = Column(String(80), unique=True)
    # the ingredients blob - this stores a lazy json blob
    # the required datatype is [{'color': string, 'name':string, 'parts':number}]
    path = Column(String(180), nullable=False)

    courses = Column(Integer)
    weeks = Column(Integer)
    difficulty = Column(Integer)

    '''
    short()
        short form representation of the Nanodegree model
    '''

    def short(self):
        print(json.loads(self.path))
        short_path = [{'name': r['name'], 'weeks': r['weeks']} for r in json.loads(self.path)]
        return {
            'id': self.id,
            'title': self.title,
            'path': short_path
        }

    '''
    long()
        long form representation of the Nanodegree model
    '''

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'path': json.loads(self.path)
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            nanodegree = Nanodegree(title=req_title, path=req_path)
            nanodegree.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            nanodegree = Nanodegree(title=req_title, path=req_path)
            nanodegree.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            nanodegree = Nanodegree.query.filter(Nanodegree.id == id).one_or_none()
            nanodegree.title = 'Introduction to Computer Basics'
            nanodegree.update()
    '''

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())


'''
Category

'''
class Category(db.Model):  
  __tablename__ = 'categories'

  id = Column(Integer, primary_key=True)
  type = Column(String)
  

  def __init__(self, type, paid):
    self.type = type
    self.paid = paid

  def format(self):
    return {
      'id': self.id,
      'type': self.type,
      'paid': self.paid
    }