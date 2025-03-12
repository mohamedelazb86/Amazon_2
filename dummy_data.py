from faker import Faker
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from product.models import Product,Brand

def seed_brand(n):
    for _ in range(n):
        images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
        fake=Faker()
        Brand.objects.create(
            name=fake.name(),
            image=f'image_brand/{images[random.randint(0,9)]}'

        )
def seed_product(n):
    fake=Faker()
    flag_type=['New','Sale','Feature']
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    brand=Brand.objects.all()
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            flag=flag_type[random.randint(0,2)],
            price=round(random.uniform(5.55,99.99),2),
            image=f'image_product/{images[random.randint(0,9)]}',
            sku=random.randint(100,1000000000),
            subtitle=fake.text(max_nb_chars=4000),
            descriptions=fake.text(max_nb_chars=40000),
            brand=brand[random.randint(0,len(brand)-1)],
            quantity=random.randint(5,100)


        )
#seed_brand(200)
seed_product(1500)
