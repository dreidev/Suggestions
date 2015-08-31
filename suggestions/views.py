from .models import ObjectView, ObjectViewDictionary


def update_suggestions_dictionary(request, object):
    if request.user.is_authenticated():
        user = request.user
        try:
            ObjectView.objects.get(user=user, object=object)
        except:
            ObjectView.objects.create(user=user, object=object)
        viewed = ObjectView.objects.filter(user=user).exclude(
            content_object=object)
        if viewed:
            for obj in viewed:
                if type(object) == type(obj):
                    try:
                        visited = ObjectViewDictionary.objects.get(
                            current_object=object,
                            visited_before_object=obj.content_object)
                        count = visited.visits + 1
                        visited.visits = count
                        visited.save()
                    except:
                        ObjectViewDictionary.objects.create(
                            current_recipe=object,
                            visited_before=obj.content_object)
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
