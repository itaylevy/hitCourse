from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import string
import re


class UniqueSymbolsValidator:
    def __init__(self, special_symbols=('~', '!', '@', '#', '$', '%', '^', '&', '*')):
        self.special_symbols = special_symbols

    def validate(self, password, user=None):
        have_special_symbol = False
        for symbol in self.special_symbols:
            if symbol in password:
                have_special_symbol = True
        if not have_special_symbol:
            raise ValidationError(message="This password must contain at least one special symbol(~,!,@,#,$,%,^,&,*)")

    def get_help_text(self):
        return _(
            "Your password must contain at least one special symbol(~,!,@,#,$,%,^,&,*)"
        )


class LetterCaseValidator:
    def __init__(self, upper_case_letters=string.ascii_uppercase[:26], lower_case_letters=string.ascii_lowercase[:26]):
        self.upper_case_letters = upper_case_letters
        self.lower_case_letters = lower_case_letters

    def validate(self, password, user=None):
        if re.search(self.lower_case_letters, password) is None:
            print("Visit first")
            raise ValidationError(message="Password must contain at least one lowercase letter")
        if re.search(self.upper_case_letters, password) is None:
            print("Visit second")
            raise ValidationError(message="Password must contain at least one uppercase letter")




    def get_help_text(self):
        return _(
            "Password must contain at least one uppercase letter and one lower case letter"
        )