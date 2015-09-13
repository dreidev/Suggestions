from .models import ObjectView, ObjectViewDictionary
from django.contrib.contenttypes.models import ContentType


def update_suggestions_dictionary(request, object):
    if request.user.is_authenticated():
        user = request.user
        content_type = ContentType.objects.get_for_model(type(object))
        try:
            ObjectView.objects.get(
                user=user, object_id=object.id, content_type=content_type)
        except:
            ObjectView.objects.create(user=user, content_object=object)
        viewed = ObjectView.objects.filter(user=user)
        if viewed:
            for obj in viewed:
                try:
                    visited = ObjectViewDictionary.objects.get(
                        current_object_id=object.id,
                        current_content_type=content_type,
                        visited_before_object_id=obj.object_id,
                        visited_before_content_type=obj.content_type)
                    count = visited.visits + 1
                    visited.visits = count
                    visited.save()
                except:
                    if object.id != obj.object_id:
                        ObjectViewDictionary.objects.create(
                            current_object=object,
                            visited_before_object=obj.content_object)
    return


def get_suggestions_with_size(object, size):
    try:
        return ObjectViewDictionary.objects.filter(
            current_object=object).extra(order_by=['-visits'])[:size]
    except:
        return ObjectViewDictionary.objects.filter(
            current_object=object).extra(order_by=['-visits'])


def get_suggestions(object):
    return ObjectViewDictionary.objects.filter(
        current_object=object).extra(order_by=['-visits'])
