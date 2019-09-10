import grpc
import json

from django import template
from django.utils.safestring import mark_safe
from django.conf import settings
from render_service import render_service_pb2_grpc, render_service_pb2

connection_string = "{host}:{port}".format(
    host=getattr(settings, "RENDER_SERVICE_HOST", "localhost"),
    port=getattr(settings, "RENDER_SERVICE_PORT", "50051"),
)
register = template.Library()
channel = grpc.insecure_channel(connection_string)
stub = render_service_pb2_grpc.RenderServiceStub(channel)


@register.simple_tag(takes_context=True)
def render_component(context, _component_name, **kwargs):
    serialized_props = json.dumps(kwargs)
    request = render_service_pb2.RenderRequest(
        name=_component_name, props=serialized_props
    )
    render_id = "svc_render_root_{}".format(
        len(context["render_service_data"].items()) + 1
    )
    context["render_service_data"][render_id] = {
        "name": _component_name,
        "props": kwargs,
    }

    try:
        response = stub.Render(request)
        return mark_safe(
            """<div id="{}">{}</div>""".format(render_id, response.content)
        )
    except grpc.RpcError as e:
        return "Render failed: {}".format(e.details())


@register.simple_tag(takes_context=True)
def dump_render_data(context):
    json_data = json.dumps(context["render_service_data"])

    # Mark safe messes with the escaped characters in the JSON so we'll add
    # it back like this for now
    return mark_safe(json_data.replace("\\", "\\\\"))

