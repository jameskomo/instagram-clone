from django.test import TestCase
from .models import Image

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.image1=Image.objects.create(image_name="test_image", image_caption="just trying", image_comments="best ever", profile="komo", pub_date="May 17, 2019", photo_image="/media/images/page-background2.jpg")
    # Testing  instance
    Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image1,Image))

     def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_image.image_name, "test_image")
        self.assertEqual(self.new_image.image_caption, "just trying")
        self.assertEqual(self.new_image.image_comments, "best ever")
        self.assertEqual(self.new_image.profile, "komo")
        self.assertEqual(self.new_image.pub_date, "May 17, 2019")
        self.assertEqual(self.new_image.photo_image, "/media/images/page-background2.jpg")

     def test_delete_method(self):
        self.new_image.save_image()
        test_image = Image(test_image", "just trying", "best ever", "komo", "May 17, 2019", "/media/images/page-background2.jpg")  # new image
        test_image.save_image()

        self.new_image.delete_image()  # Deleting a contact object
        self.assertEqual(len(Image.image_list), 1)0)

    def test_save_method(self):
        self.image1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        
   
