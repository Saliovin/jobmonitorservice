GET http://localhost:5000/modulelogs/
- get all jobs

GET http://localhost:5000/modulelogs/<job_id>
- get a specific job

POST http://localhost:5000/modulelogs/
- create a new job

PUT http://localhost:5000/modulelogs/<job_id>
- update state of job. creates a new state record.

DELETE http://localhost:5000/modulelogs/<job_id>
- remove job

DELETE http://localhost:5000/modulelogs/<job_id>/<state_id>
- remove a job's specified state


