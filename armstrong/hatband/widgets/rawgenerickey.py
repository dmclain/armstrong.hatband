from django.core.urlresolvers import reverse
from django.forms import Widget
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from ..utils import static_url


class RawGenericKeyWidget(Widget):
    template = "admin/hatband/widgets/rawgenerickey.html"

    class Media:
        js = (
              static_url("hatband/js/rawgenerickey.js"),
             )

    def __init__(self, object_id_name="object_id",
                 content_type_name="content_type",
                 facet_url=None,
                 query_lookup_url=None,
                 base_lookup_url=None,
                 *args, **kwargs):
        super(RawGenericKeyWidget, self).__init__(*args, **kwargs)
        self.object_id_name = object_id_name
        self.content_type_name = content_type_name
        self.facet_url = facet_url
        self.base_lookup_url = base_lookup_url

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        final_attrs.update({
            "value": value,
            "is_templated": final_attrs["id"].find("__prefix__") > -1,
            "object_id_name": self.object_id_name,
            "content_type_name": self.content_type_name,
            "content_type_id": final_attrs["id"].replace(self.object_id_name, self.content_type_name),
            "facet_url": self.facet_url or
                    reverse("admin:generic_key_facets"),
            "admin_media_prefix": settings.ADMIN_MEDIA_PREFIX,
            "content_types": ContentType.objects.all(),
            "base_lookup_url": (self.base_lookup_url or
                    reverse("admin:index"))
        })
        return render_to_string(self.template, final_attrs)
