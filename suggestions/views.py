from .models import ObjectView, ObjectViewDictionary
from django.contrib.contenttypes.models import ContentType


def update_suggestions_dictionary(request, object):
    """
    Updates the suggestions' dictionary for an object upon visiting its page
    """
    content_type = ContentType.objects.get_for_model(type(object))
    if request.user.is_authenticated():
        user = request.user
        try:
            # Check if the user has visited this page before
            ObjectView.objects.get(
                user=user, object_id=object.id, content_type=content_type)
        except:
            ObjectView.objects.create(user=user, content_object=object)
        # Get a list of all the objects a user has visited
        viewed = ObjectView.objects.filter(user=user)
        if viewed:
            for obj in viewed:
                if not exists_in_dictionary(obj, obj.content_type, object, content_type, True):
                    # Create an entry if it's non existent
                    if object.id != obj.object_id:
                        if content_type == obj.content_type:
                            ObjectViewDictionary.objects.create(
                                current_object=object,
                                visited_before_object=obj.content_object)
                        if not exists_in_dictionary(obj, obj.content_type, object, content_type, False):
                            ObjectViewDictionary.objects.create(
                                current_object=obj.content_object,
                                visited_before_object=object)

    # else:
    #     try:
    #         visited = request.session['visited']
    #     except:
    #         visited = []
    #         request.session = visited
    return


def exists_in_dictionary(object, content_type, obj, obj_content_type, update):
    try:
        visited = ObjectViewDictionary.objects.get(
                current_object_id=object.id,
                current_content_type=content_type,
                visited_before_object_id=obj.object_id,
                visited_before_content_type=obj_content_type)
        if update:
            count = visited.visits + 1
            visited.visits = count
            visited.save()
        return True
    except:
        return False


def get_suggestions_with_size(object, size):
    """ Gets a list with a certain size of suggestions for an object """
    content_type = ContentType.objects.get_for_model(type(object))
    try:
        return ObjectViewDictionary.objects.filter(
            current_object_id=object.id,
            current_content_type=content_type).extra(
            order_by=['-visits'])[:size]
    except:
        return ObjectViewDictionary.objects.filter(
            current_object_id=object.id,
            current_content_type=content_type).extra(order_by=['-visits'])


def get_suggestions(object):
    """ Gets a list of all suggestions for an object """
    content_type = ContentType.objects.get_for_model(type(object))
    return ObjectViewDictionary.objects.filter(
        current_object_id=object.id,
        current_content_type=content_type).extra(order_by=['-visits'])
