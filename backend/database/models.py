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
    !!NOTE you can change the database_filename variable to have multiple versions of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    # add one demo row which is helping in POSTMAN test
    nanodegree = Nanodegree(
        title='Introduction to Computer Basics',
        degree_path='[{"name": "Introduction to Programming Basics", "weeks": 6, "difficulty": 1}, {"name": "Understanding Those Pesky Logins", "weeks": 3, "difficulty": 1}]'
    )

    # add a demo row for Courses
    course = Course(
        name = 'Introduction to Programming Basics',
        weeks = 6, 
        difficulty = 1
    )

    nanodegree.insert()
    course.insert()


# ROUTES

'''
Nanodegree
a persistent nanodegree entity, extends the base SQLAlchemy Model
'''


class Nanodegree(db.Model):
    # Auto-incrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    
    # String Title
    title = Column(String(80), unique=True)

    # the degree_path blob - this stores a lazy json blob
    # the required datatype is [{'name': string, 'weeks': number, 'difficulty':number}]
    degree_path = Column(String(180), nullable=False)

    '''
    short()
        short form representation of the Nanodegree model
    '''

    def short(self):
        print(json.loads(self.degree_path))
        short_path = [{'name': r['name']} for r in json.loads(self.degree_path)]
        return {
            'id': self.id,
            'title': self.title,
            'degree_path': short_path
        }

    '''
    long()
        long form representation of the Nanodegree model
    '''

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'degree_path': json.loads(self.degree_path)
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            nanodegree = Nanodegree(title=req_title, degree_path=req_degree_path)
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
            nanodegree = Nanodegree(title=req_title, degree_path=req_degree_path)
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

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "degree_path": self.degree_path,
        }

    def __repr__(self):
        return json.dumps(self.short())


'''
Course

'''
class Course(db.Model):
  __tablename__ = 'courses'

  id = Column(Integer, primary_key=True)
  # nanodegree_id = Column(Integer, ForeignKey('nanodegrees.id'), nullable=True) #Nullable because not all courses go to a nanodegree
  
  name = Column(String, nullable=False)
  weeks = Column(Integer, nullable=False)
  difficulty = Column(Integer, nullable=False)



  '''
  long()
    long form representation of the Nanodegree model
  '''

  def long(self):
      return {
          'id': self.id,
          'name': self.name,
          "weeks": self.weeks,
          "difficulty": self.difficulty
      }



  '''
  insert()
      inserts a new model into a database
      the model must have a unique name
      the model must have a unique id or null id
      EXAMPLE
          nanodegree = Nanodegree(title=req_title, degree_path=req_degree_path)
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
          nanodegree = Nanodegree(title=req_title, degree_path=req_degree_path)
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

  def __init__(self, name, weeks, difficulty):
    self.name = name
    self.weeks = weeks
    self.difficulty = difficulty

  def format(self):
    return {
      'id': self.id, 
      'name': self.name,
      'weeks': self.weeks,
      'difficulty': self.difficulty
    }