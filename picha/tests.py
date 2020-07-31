from django.test import TestCase
from .models import Images, Categories, Locations

# Create your tests here.
class ImagesTest(TestCase):
    '''
    '''
    def setUp(self):
        self.new_category = Categories(name='testing')
        self.new_category.save_category()

        self.new_location = Locations(city='Nairobi', country='Kenya')
        self.new_location.save_location()

        self.new_picture = Images(image_link='images/picture.jpeg', title='Image title', description='sth random', category=self.new_category, location=self.new_location)

    def tearDown(self):
        Categories.objects.all().delete()
        Locations.objects.all().delete()
        Images.objects.all().delete()

    def test_instances(self):
        self.assertTrue(isinstance(self.new_picture,Images))
        self.assertTrue(isinstance(self.new_category, Categories))
        self.assertTrue(isinstance(self.new_location, Locations))

    def test_save_image(self):
        self.new_picture.save_image()
        self.assertTrue(len(Images.objects.all()) > 0)     


class CategoryTest(TestCase):
    def setUp(self):
        self.new_category = Categories(name='categoryA')

    def test_save_category(self):
        self.new_category.save_category()
        self.assertTrue(len(Categories.objects.all()) > 0)     


class LocationTest(TestCase):
    def setUp(self):
        self.new_location = Locations(city='lost city', country='unknown')

    def test_save_location(self):
        self.new_location.save_location()
        self.assertTrue(len(Locations.objects.all()) > 0)     
