from django import template


register = template.Library()

@register.filter(is_safe=True)
def publisher_link(publisher):
    url = 'https://www.testurl.com/'
    if publisher == 'admin':
        return '{} ({})'.format(publisher, url)
    else:
        return publisher
    # use it like this: {{ book.publisher|publisher_link }}


@register.filter(is_safe=True)
def youtube_embed(url, hd=False):
    if hd:
        return get_youtube_hd_embed(url)
    else:
        return get_youtube_sd_embed(url)
    # use it like this: {{ youtube_link|youtube_embed:"True" }}
