'''Examples of CRUD
from models import db, Puppy

## create
my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

## read
all_puppies = Puppy.query.all()
print(all_puppies)

#select by Id
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

#filters
#produces some SQL code
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())

####Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


###delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()


all_puppies = Puppy.query.all()
print(all_puppies)
'''