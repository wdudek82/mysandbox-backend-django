from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag
def bootstrap_css():
    tags = [
        '''
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" 
        integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" 
        crossorigin="anonymous">
        ''',
        '''
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" 
        integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" 
        crossorigin="anonymous"></script>
        '''
    ]
    return mark_safe(''.join(tags))


@register.inclusion_tag('bootstrap_button.html')
def bootstrap_button(text, style='default'):
    return {
        'style': style.lower(),
        'text': text
    }
