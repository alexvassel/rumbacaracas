# -*- coding: utf-8 -*-
def set_model_field_attr(model, field, attr, val):
    setattr(model._meta.get_field(field), attr, val)
