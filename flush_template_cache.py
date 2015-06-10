#!/usr/bin/env python
from django.template.loader import template_source_loaders

def reset_template_cache():
    print("123")
    if not template_source_loaders:
        return

    for loader in template_source_loaders:	
	print(loader)
        loader.reset()

reset_template_cache()

