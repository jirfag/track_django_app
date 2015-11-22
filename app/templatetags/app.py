from django.template import Library

register = Library()

DOT = '.'

def build_query_string(request, new_params):
    get_params_copy = request.GET.copy()
    for k, v in new_params.items():
        del get_params_copy[k]
        get_params_copy[k] = v
    return '?{}'.format(get_params_copy.urlencode())

@register.simple_tag(takes_context=True)
def paginator_number(context, i):
    page = context['page_obj']
    if i == DOT:
        ret = '<li class="disabled"><a href="#">...</a></li>'
    elif i == page.number:
        ret = '<li class="active"><a href="#">{}</a></li>'.format(i)
    else:
        request = context['request']
        ret = '<li><a href="{}">{}</a></li>'.format(
               build_query_string(request, {'page': i}),
               i)

    return ret

@register.inclusion_tag('pagination.html', takes_context=True)
def pagination(context):
    paginator, page_obj = context['paginator'], context['page_obj']
    page_num = page_obj.number - 1
    ON_EACH_SIDE, ON_ENDS = 1, 2

    if paginator.num_pages <= 10:
        page_range = range(paginator.num_pages)
    else:
        if page_num > (ON_EACH_SIDE + ON_ENDS):
            subranges = [range(0, ON_ENDS), DOT, range(page_num - ON_EACH_SIDE, page_num + 1)]
        else:
            subranges = [range(0, page_num + 1)]
        if page_num < (paginator.num_pages - ON_EACH_SIDE - ON_ENDS - 1):
            subranges += [range(page_num + 1, page_num + ON_EACH_SIDE + 1), DOT,
                          range(paginator.num_pages - ON_ENDS, paginator.num_pages)]
        else:
            subranges.append(range(page_num + 1, paginator.num_pages))

    page_range = sum(map(list, subranges), [])
    page_range = [((pn + 1) if pn != DOT else DOT) for pn in page_range]

    return {'page_range': page_range, 'page_obj': page_obj, 'request': context['request']}
