from flask import request, json, Response, Blueprint
from ..models.job_model import JobModel, JobSchema

job_api = Blueprint('jobs', __name__)
job_schema = JobSchema()


@job_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    data = job_schema.load(req_data)
    job = JobModel(data)
    job.save()

    return custom_response({'Message': 'Job created'}, 201)


@job_api.route('/', methods=['GET'])
def get_all():
    jobs = JobModel.get_all_jobs()
    ser_jobs = job_schema.dump(jobs, many=True)
    return custom_response(ser_jobs, 200)


@job_api.route('/<string:job_id>', methods=['GET'])
def get_one(job_id):
    job = JobModel.get_one_job(job_id)
    if not job:
        return custom_response({'error': 'job not found'}, 404)
    ser_job = job_schema.dump(job)
    return custom_response(ser_job, 200)


@job_api.route('/<string:job_id>', methods=['PUT'])
def update(job_id):
    req_data = request.get_json()
    data = job_schema.load(req_data, partial=True)
    job = JobModel.get_one_job(job_id)
    job.update(data)
    ser_job = job_schema.dump(job)
    return custom_response(ser_job, 200)


@job_api.route('/<string:job_id>', methods=['DELETE'])
def delete(job_id):
    job = JobModel.get_one_job(job_id)
    if not job:
        return custom_response({'Error': 'Job not found'}, 404)
    job.delete()
    return custom_response({'Message': 'Job deleted'}, 201)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
