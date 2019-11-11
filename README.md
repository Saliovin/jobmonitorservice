GET http://localhost:5000/modulelogs/
- get all jobs

GET http://localhost:5000/modulelogs/<job_id>
- get a specific job

POST http://localhost:5000/modulelogs/
- create a new job

PUT http://localhost:5000/modulelogs/<job_id>
- update job.

DELETE http://localhost:5000/modulelogs/<job_id>
- remove job

GET http://localhost:5000/modulelogs/<job_id>/
- get all states of a job

GET http://localhost:5000/modulelogs/<job_id>/<state_id>
- get a specific state of a job

POST http://localhost:5000/modulelogs/<job_id>/
- create a new state

PUT http://localhost:5000/modulelogs/<job_id>/<state_id>
- update state.

DELETE http://localhost:5000/modulelogs/<job_id>/<state_id>
- remove a job's specified state


