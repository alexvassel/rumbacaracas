# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from django.contrib.admin.filterspecs import DateFieldFilterSpec
from django.utils.translation import ugettext as _


class DateAddedFilterSpec(DateFieldFilterSpec):
    def __init__(self, f, request, params, model, model_admin, field_path=None):
        super(DateAddedFilterSpec, self).__init__(f, request, params, model, model_admin,
                                                  field_path)

        previous_month = {'end': (datetime.now().replace(day=1) - timedelta(days=1)).date()}

        previous_month['start'] = previous_month['end'].replace(day=1)

        self.links += (
            (_('Previous month'),
             {'%s__gte' % self.field.name: str(previous_month['start']),
              '%s__lte' % self.field.name: str(previous_month['end'])}),)

        self.custom_filter_checked = (True if str(previous_month['start'])
                                      in request.GET.values() and str(previous_month['end'])
                                      in request.GET.values() else False)

    def choices(self, cl):
        for title, param_dict in self.links:
            yield {'selected': self.custom_filter_checked or self.date_params == param_dict,
                   'query_string': cl.get_query_string(
                                   param_dict,
                                   [self.field_generic]),
                   'display': title}
