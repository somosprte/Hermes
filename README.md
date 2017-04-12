# Hermes
![alt tag](https://raw.githubusercontent.com/somosprte/projectname/Hermes/img.png)
## Install

The Python version should be >= 3.4. Anaconda `[1]` or Miniconda `[2]` (python distribution offered by Continuum) can be used.

To install required packages do:

```sh
pip install -r requirements.txt
```

## Start API

To start the api do:


```sh
python api.py
```

And to test it:

```sh
$ curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
{"todo1": "Remember the milk"}
$ curl http://localhost:5000/todo1
{"todo1": "Remember the milk"}
$ curl http://localhost:5000/todo2 -d "data=Change my brakepads" -X PUT
{"todo2": "Change my brakepads"}
$ curl http://localhost:5000/todo2
{"todo2": "Change my brakepads"}
```
(resource: `[3]`)


## References

[1] https://www.continuum.io/downloads

[2] https://conda.io/miniconda.html

[3] http://flask-restful-cn.readthedocs.io/en/0.3.5/quickstart.html
