from flask import request, json, Response, Blueprint, g
from ..models.state_model import StateModel, StateSchema

state_api = Blueprint('state_api', __name__)
state_schema = StateSchema()


@state_api.url_value_preprocessor
def get_profile_owner(endpoint, values):
    g.job_id = values.pop('job_id')


@state_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    req_data['job_id'] = g.job_id
    data = state_schema.load(req_data)
    state = StateModel(data)
    state.save()
    data = state_schema.dump(state)
    return custom_response(data, 201)


@state_api.route('/', methods=['GET'])
def get_all():
    states = StateModel.get_all_states(g.job_id)
    ser_state = state_schema.dump(states, many=True)
    return custom_response(ser_state, 200)


@state_api.route('/<string:state_id>', methods=['PUT'])
def update(state_id):
    req_data = request.get_json()
    data = state_schema.load(req_data, partial=True)
    state = StateModel.get_one_state(state_id)
    state.update(data)
    ser_state = state_schema.dump(state)
    return custom_response(ser_state, 200)


@state_api.route('/<string:state_id>', methods=['DELETE'])
def delete(state_id):
    state = StateModel.get_one_state(state_id)
    if not state:
        return custom_response({'Error': 'State not found'}, 404)
    state.delete()
    return custom_response({'Message': 'State deleted'}, 201)


def custom_response(res, status_code):
    return Response(

        mimetype="application/json",
        response=json.dumps(res),

        status=status_code
    )
