from django.core.management.base import BaseCommand
from listing.utils import get_keyword_object
from listing.models import TemplateKeyword


class Command(BaseCommand):
    def handle(self, *args, **options):
        keyword_list = get_keyword_object()
        for keyword_object in keyword_list:
            try:
                TemplateKeyword.objects.create(
                    mystatemls_name=keyword_object["mystatemls_name"],
                    name=keyword_object["name"],
                )
            except:
                print("Could not use this object", keyword_object)
