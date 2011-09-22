from django.template.defaultfilters import slugify

def SlugifyUniquely(value, model, slugfield="slug", maxlength=50):
    """Returns a slug on a name which is unique within a model's table

    This code suffers a race condition between when a unique
    slug is determined and when the object with that slug is saved.
    It's also not exactly database friendly if there is a high
    likelyhood of common slugs being attempted.

    A good usage pattern for this code would be to add a custom save()
    method to a model with a slug field along the lines of:



            def save(self):
                if not self.id:
                    # replace self.name with your prepopulate_from field
                    self.slug = SlugifyUniquely(self.name, self.__class__)
            super(self.__class__, self).save()

    Original pattern discussed at
    http://www.b-list.org/weblog/2006/11/02/django-tips-auto-populated-fields
    """
    suffix = 0
    potential = base = slugify(value)
    while True:
        if suffix:
            calculated_max_length = maxlength - 1 - len(str(suffix))
            potential = "-".join([base[:calculated_max_length], str(suffix)])
        if not model.objects.filter(**{slugfield: potential}).count():
            return potential
        # we hit a conflicting slug, so bump the suffix & try again
        suffix += 1
