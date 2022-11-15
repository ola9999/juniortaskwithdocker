import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from juniortask.models import Author,Note
from juniortask.serializers import AuthorSerializer , NoteDetailsSerializer

# initialize the APIClient app
# I could either use selenium to get and post data throw DRF default tempalte
client = Client()


#GET List
class ListNotesTest(TestCase):
    """ Test module for GET all notes API """

    def setUp(self):
        self.author1 =  Author.objects.create(
                                first_name='Ahmad', last_name='ms')
        self.author2 =  Author.objects.create(
                                first_name='Manal', last_name='mh')
        self.author3 =  Author.objects.create(
                                first_name='Noha', last_name='ms2')
        self.author4 =  Author.objects.create(
                                first_name='Ola', last_name='ms3')

    def test_list_notes(self):
        # get API response
        response = client.get(reverse('note_list'))
        # get data from db
        notes = Note.objects.all()
        serializer = NoteDetailsSerializer(notes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#GET #Retrieve single note
class GetSingleNoteTest(TestCase):
    """ Test module for GET single note API """

    longMessage = True

    def setUp(self):
        self.ahmad =  Note.objects.create(author = Author.objects.create(first_name='Ahmad', last_name='ms') ,
                                          content='n1 for author Ahmad')
        self.manal =  Note.objects.create(author = Author.objects.create(first_name='Manal', last_name='mh') ,
                                          content='n2 for author Manal')
        self.noha  =  Note.objects.create(author = Author.objects.create(first_name='Noha', last_name='ms2') ,
                                          content='n3 for author Noha')
        self.ola   =  Note.objects.create(author = Author.objects.create(first_name='Ola', last_name='ms3') ,
                                          content='n4 for author Ola')

    def test_get_valid_single_note(self):
        
        response = client.get(reverse('note_detail', kwargs={'pk': self.manal.pk}))

        note = Note.objects.get(pk=self.manal.pk)
        serializer = dict(NoteDetailsSerializer(note).data)
        serializer['url']= reverse('note_detail', kwargs={'pk': self.manal.pk})

        self.assertEqual(response.data, serializer)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_invalid_single_note(self):
        response = client.get(reverse('note_detail', kwargs={'pk': 40}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


#Add #Post Note
class Create2NoteTest(TestCase):
    """ Test module for inserting a new note """

    def setUp(self):
        self.valid_note = {
                                "author":Author.objects.create(first_name='Ahmad', last_name='ms').pk,
                                "content": "ahmad note content"
                            }
        self.invalid_note ={
                                "author": '',
                                "content": "luna note content"
                            }

    def test_create_valid_note(self):
        endpoint = reverse('note_create')
        data = json.dumps(self.valid_note)
        content_type = 'application/json'

        response = client.post(endpoint , self.valid_note ,content_type)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_note(self):

        endpoint = reverse('note_create')
        data = json.dumps(self.invalid_note)
        content_type = 'application/json'

        response = client.post(endpoint , data ,content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#Delete note
class DeleteSingleNoteTest(TestCase):
    """ Test module for deleting an existing note record """

    def setUp(self):
        self.ahmad =  Note.objects.create(author = Author.objects.create(first_name='Ahmad', last_name='ms') ,
                                          content='n1 for author Ahmad')
        self.manal =  Note.objects.create(author = Author.objects.create(first_name='Manal', last_name='mh') ,
                                          content='n2 for author Manal')

    def test_valid_delete_note(self):

        response = client.delete(reverse('note_delete', kwargs={'pk': self.manal.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_note(self):

        response = client.delete(reverse('note_delete', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)