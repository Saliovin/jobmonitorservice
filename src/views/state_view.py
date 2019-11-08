from flask import request, json, Response, Blueprint, g
from ..models.state_model import StateModel, StateSchema

state_api = Blueprint('state_api', __name__)
state_schema = StateSchema()


@state_api.url_value_preprocessor
def get_profile_owner(endpoint, values):
    g.owner_id = values.pop('job_id')


@state_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    req_data['owner_id'] = g.owner_id
    data = state_schema.load(req_data)
    state = StateModel(data)
    state.save()
    data = state_schema.dump(state)
    return custom_response(data, 201)


@state_api.route('/', methods=['GET'])
def get_all():
    states = StateModel.get_all_states_of_job(g.owner_id)
    ser_jobs = state_schema.dump(states, many=True)
    return custom_response(ser_jobs, 200)


def custom_response(res, status_code):
    print(res)
    return Response(

        mimetype="application/json",
        response=json.dumps(res),

        status=status_code
    )
