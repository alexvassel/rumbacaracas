# -*- coding: utf-8 -*-
from django import template


register = template.Library()


class SetVarNode(template.Node):

    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        context[self.var_name] = self.var_value
        return ''


@register.tag(name='set')
def set_var(_, token):
    """
    {% set some_var = '123' %}
    """
    parts = token.split_contents()

    if len(parts) != 4:
        raise template.TemplateSyntaxError('''"set" tag must be of the form:
                                           {% set <var_name> = <var_value> %}''')

    return SetVarNode(parts[1], parts[3])
