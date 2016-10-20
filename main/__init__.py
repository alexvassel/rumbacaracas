
# Register the filter for every model field, that has is_active_filter == True
from django.contrib.admin.filterspecs import FilterSpec

from events.filterspecs import DateAddedFilterSpec


FilterSpec.filter_specs.insert(0, (lambda f: getattr(f, 'is_active_filter', False),
                                   DateAddedFilterSpec))
