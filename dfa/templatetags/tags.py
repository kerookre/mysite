from django import template


register = template.Library()


@register.filter()
def get_value_by_key(dictionary, key):
    error = "KeyError on a dictionary: {} of a key: {}".format(dictionary, key)
    return dictionary.get(key, error)


