import csv
import io
from .serializers import UserSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User.
    """

    return {
        'token': token,
        'user': UserSerializer(user).data
    }

def parse_csv_model(csvfile, model):
    reader = csv.DictReader(io.StringIO(csvfile))
    model_instances = []
    for row in reader:
        model_instance = model()
        for field in row.keys():
            setattr(model_instance, field, row[field])
        model_instances.append(model_instance)
    return model_instances
