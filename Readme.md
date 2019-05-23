# Mock Crud Server
This is lightweight crud service which understands rest protocal
and caters to basic rest methods: `GET` `PUT`, `POST`, `DELETE` without
any modification.

As this uses only `BaseHTTPRequestHandler` this doesn't need any
dependency.

## Installation
1. Clone the repo (or simply copy the code to python file)
2. Run `python simple_server.py` (will bind to port at 8080 by default)


## Storage
As of now it uses in memory data structure only. Which means data
will flush out on every restart.

## Examples
1. POST:
- Call
```
curl -X POST \
  http://localhost:8080/api/v1/users \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"name": "Spidey",
	"age": 1
}
```

Response: 
```
{
	"name": "Spidey",
	"age": 1,
	"id": "4738c11d-acc4-482b-b5cb-accd9ef74c75"
}
```

2. PUT:
- Call
```
curl -X PUT \
  http://localhost:8080/api/v1/users/4738c11d-acc4-482b-b5cb-accd9ef74c75 \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "name": "spidey",
    "age": 3,
    "id": "4738c11d-acc4-482b-b5cb-accd9ef74c75"
}
```

Response: 
```
{
	"name": "jayesh",
	"age": 3,
	"id": "4738c11d-acc4-482b-b5cb-accd9ef74c75"
}
```

3. GET:

- call:
```
curl -X GET \
  http://localhost:8080/api/v1/users/4738c11d-acc4-482b-b5cb-accd9ef74c75 \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "name": "jayesh",
    "age": 3,
    "id": "4738c11d-acc4-482b-b5cb-accd9ef74c75"
}'
```

- Response:
```
{
	"name": "jayesh",
	"age": 3,
	"id": "4738c11d-acc4-482b-b5cb-accd9ef74c75"
}
```

4. DELETE

- call:
```
curl -X DELETE \
  http://localhost:8080/api/v1/users/4738c11d-acc4-482b-b5cb-accd9ef74c75 \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "name": "jayesh",
    "age": 3,
    "id": "4738c11d-acc4-482b-b5cb-accd9ef74c75"
}'
```