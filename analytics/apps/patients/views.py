from django.http import JsonResponse


def query(request):
    data = {}

    # TODO: query the DB and return results

    return JsonResponse(data, json_dumps_params=dict(indent=4, sort_keys=True))
