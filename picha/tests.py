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
        self.new_picture.save_image()
        self.another_picture = Images(image_link='images/photo.jpg', title='Another title', description='sth else more random', category=self.new_category, location=self.new_location)
        self.another_picture.save_image()

    def tearDown(self):
        Categories.objects.all().delete()
        Locations.objects.all().delete()
        Images.objects.all().delete()

    def test_instances(self):
        self.assertTrue(isinstance(self.new_picture,Images))
        self.assertTrue(isinstance(self.new_category, Categories))
        self.assertTrue(isinstance(self.new_location, Locations))

    def test_save_image(self):
        self.assertTrue(len(Images.objects.all()) == 2)

    def test_delete_image(self):
        self.new_picture.delete_image()
        self.assertTrue(len(Images.objects.all()) == 1)

    @classmethod
    def test_update_image(cls):
        try:
            to_update = Images.objects.get(title = 'Another title')
            to_update.image_link = 'images/updated.png'
            to_update.save()
            print(to_update.image_link) #new image url
            print(to_update.title) #old image title
        except Images.DoesNotExist:
            print('Image you specified does not exist')


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
