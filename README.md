
## ECOMMERCE APPLICATION

The application is containerized in a docker-compose.yaml file.

Tools: `podman` and `python`

To get started:
-
- Setup and Activate virtual environment
```shell
    python3 -m venv venv/
    source venv/bin/activate
```

- Install dependencies
```shell
    pip install -r requirements.txt
```

- Run `podman-compose up --build`

NOTE: The setup process also works for `docker`.