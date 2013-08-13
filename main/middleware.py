# -*- coding: utf-8 -*-

import urlparse
import datetime
from main.models import MostViewed
from events.models import Event
from zinnia.models import Entry
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

class MostViewedMiddleware(object):

    def process_request(self, request):
        try:
            parsed_url = request.path.split('/')
            if len(parsed_url) == 7:
                type = parsed_url[1]
                year = parsed_url[2]
                month = parsed_url[3]
                day = parsed_url[4]
                slug = parsed_url[5]
                
                if type == 'noticias' and len(year) == 4 and len(month) == 2 and len(day) == 2:
                    create_date = datetime.datetime(year=int(year), month=int(month), day=int(day))
                    news_item = Entry.objects.get(creation_date__year=create_date.year, 
                                                  creation_date__month=create_date.month, 
                                                  creation_date__day=create_date.day, 
                                                  slug=slug)
                    if "blog" in news_item.categories.all():
                        return
                    if news_item != None:
                        content_type_id = ContentType.objects.get_for_model(news_item)
                        try:
                            most_viewed = MostViewed.objects.get(content_type=content_type_id, content_type_object_id=news_item.id)
                            most_viewed.no_of_views = most_viewed.no_of_views + 1
                        except ObjectDoesNotExist:
                            most_viewed = MostViewed(content_type = content_type_id, content_type_object_id=news_item.id, no_of_views=1 )
                        
                        most_viewed.save()
            elif len(parsed_url) == 4:
                type = parsed_url[1]
                slug = parsed_url[2]
                
                if type == 'eventos':
                    event_item = Event.objects.get(slug=slug)
                    if event_item != None:
                        content_type_id = ContentType.objects.get_for_model(event_item)
                        try:
                            most_viewed = MostViewed.objects.get(content_type=content_type_id, content_type_object_id=event_item.id)
                            most_viewed.no_of_views = most_viewed.no_of_views + 1
                        except ObjectDoesNotExist:
                            most_viewed = MostViewed(content_type = content_type_id, content_type_object_id=event_item.id, no_of_views=1 )
                        
                        most_viewed.save()
        except:
            return
        
        
        