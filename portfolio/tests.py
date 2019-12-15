
from django.test import TestCase

# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):

        # Creating a new category
        self.new_category = Category(name='travel')
        self.new_category.save()

        # Creating a new location
        self.new_location = Location(name='nairobi')
        self.new_location.save()

        # Creating new Image
        self.new_image = Image(title='Image1',
        description='Thisis my first image to upload')
        self.new_image.save()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

        