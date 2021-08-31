from django.template.defaultfilters import register


@register.filter(name='dictKey')
def dictKey(d, k):
    '''Returns the given key from a dictionary.'''

    return ', '.join(d[k])