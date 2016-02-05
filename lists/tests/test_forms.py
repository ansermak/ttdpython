from django.test import TestCase

from lists.models import Item, List
from lists.forms import ItemForm, EMPTY_LIST_ERROR


class ItemFormTest(TestCase):
    def test_from_renders_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'], [EMPTY_LIST_ERROR]
        )

    def test_form_save_hanles_saving_to_a_list(self):
        list_ = List.objects.create()
        form = ItemForm(data={'text': 'Say hello'})
        new_item = form.save(for_list=list_)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'Say hello')
        self.assertEqual(new_item.list, list_)
