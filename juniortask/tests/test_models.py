from django.test import TestCase
from juniortask.models import Author,Note
from model_mommy import mommy

class JuniortaskTestMommy(TestCase):

    def test_note_creation_mommy(self):
        new_author = mommy.make('juniortask.Author')
        new_note = mommy.make('juniortask.Note')

        self.assertTrue(isinstance(new_author, Author))
        self.assertTrue(isinstance(new_note, Note))
        
        self.assertEqual(new_author.full_name,  new_author.first_name + " " + new_author.last_name)

        self.assertEqual(
            new_note.__str__(), 
            ("author :"+ str(new_note.author.full_name) + " ,  Note : " + str(new_note.content)) ,
            )