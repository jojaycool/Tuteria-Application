from django import template

from unobase.templatetags import unobase_tags
from unobase.templatetags.unobase_tags import register


class MySmartQueryStringNode(template.Node):
    def __init__(self, addition_pairs):
        self.addition_pairs = []
        for key, value in addition_pairs:
            self.addition_pairs.append((template.Variable(key) if key \
                    else None, template.Variable(value) if value else None))

    def render(self, context):
        q = dict([(k, v) for k, v in context['request'].GET.items()])
        for key, value in self.addition_pairs:
            if key:
                key = key.resolve(context)
                if value:
                    value = value.resolve(context)
                    q[key] = value
                else:
                    q.pop(key, None)
        # Also encode greater than sign and drop script tag
        qs = '&'.join(['%s=%s' % (str(k).replace('>', '&gt;'), str(v).replace('>', '&gt;')) for k, v in q.items() if k.find('script') == -1])
        res = '?' + qs if len(q) else ''
        return res


unobase_tags.SmartQueryStringNode = MySmartQueryStringNode
