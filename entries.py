
'''Example of entries
from models import db,Puppy,Owner,Toy

#ran this code to prevent error "no tables seen"
db.create_all()

rufus = Puppy('Rufus')
fido = Puppy('Fido')

#add puppies to db


db.session.add_all([rufus,fido])
db.session.commit()


print(Puppy.query.all())


rufus = Puppy.query.filter_by(name='Rufus').first()

#create Owner

jose = Owner('Jose', rufus.id)

#give rufus some toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)


db.session.add_all([jose, toy1, toy2])
db.session.commit()

#grab rufus after additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

print(rufus.report_toys())'''