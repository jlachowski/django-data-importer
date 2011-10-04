# coding: utf-8
# importers for tests

from data_importer import BaseImporter, ValidationError
from data_importer.tests.cpfcnpj import CPF
from django.utils.encoding import smart_unicode


class BaseImportWithFields(BaseImporter):
    """
    Just add fields so validate_class pass :)
    """
    fields = ['cpf','field3','field4','field5']

class SimpleValidationsImporter(BaseImportWithFields):
    """
    Since all tested importers will validate same data, we can write only one
    with validate methods.
    This importer doesn't implement save method that return data as dict in 
    BaseImporter.save and doesn't put any field as required.
    """
    def clean_cpf(self,val):
        # field isn't required in this class!
        if not val: return val
        try:
            val = CPF(val)
        except ValueError,msg:
            raise ValidationError,smart_unicode(msg)
        else:
            return val

class RequiredFieldValidationsImporter(SimpleValidationsImporter):
    """
    Since all tested importers will validate same data, we can write only one
    with validate methods.
    This importer doesn't implement save method that return data as dict in 
    BaseImporter.save but use CPF and FIELD3 fields as required.
    """
    required_fields = ['cpf','field3']

    def clean_cpf(self,val):
        try:
            val = CPF(val)
        except ValueError,msg:
            raise ValidationError,smart_unicode(msg)
        else:
            return val