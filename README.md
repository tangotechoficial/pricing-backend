# pricing-backend
Backend for TangoTech pricing project

## Installation
- Install latest version of docker and docker-composer and then:

```sh
docker-composer up
```
## Usage
- Use http://localhost:8000/api/login/ for login
```sh
curl -X POST -d "username=test&password=12345678" http://localhost:8000/api/login/
```
It should return a JWT Token, you will need this to use other routes from api.
You should use like this: 
```sh
curl -H "Authorization: JWT <token>" http://localhost:8000/api/diretrizesestrategica/
```