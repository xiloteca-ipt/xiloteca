from django.test import TestCase
from . import models
from django.apps import apps

class ModelsTest(TestCase):

    def test_madeira_names_are_properly_converted_to_string(self):
        #arrange
        expected_madeira_name = 'Madeira Teste'
        madeira_instance = models.Madeira(cod_madeira=1)
        madeira = models.MadeiraNomePopular(cod_madeira=madeira_instance, nome_popular=expected_madeira_name)

        #act
        madeira_name = str(madeira)

        #assert
        self.assertIsInstance(madeira, models.MadeiraNomePopular)
        self.assertEqual(expected_madeira_name, madeira_name)

    def test_base_template_is_present(self):
        #arrange
        file_path = 'ipt/templates/base.html'

        #act
        file = None
        try:
            file = open(file_path, "r", encoding='UTF-8')

        except FileNotFoundError:
            print('Could not find file for base template')

        #assert
        self.assertIsNotNone(file)

    def test_models_are_registered(self):
        #arrange
        app_models = []

        #act
        app_models = apps.get_models()

        #assert
        self.assertTrue(models.Conteudo in app_models)
