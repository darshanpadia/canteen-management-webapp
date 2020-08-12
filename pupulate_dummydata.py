import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')


import django
django.setup()


from MyApp.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
     for entry in range(N):
         fake_fname = fakegen.first_name()
         fake_lname = fakegen.last_name()
         fake_email = fakegen.email()

         user = User.objects.get_or_create(fname=fake_fname, lname=fake_lname, email=fake_email)


if __name__ == "__main__":
    print("populating users")
    populate(20)
    print("Done populating")
