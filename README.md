# xtenso

This is **xtenso**, a numeral translator.

In order to run it you must first build the [Docker](https://www.docker.com) container. On a Linux machine:

```bash
docker build --rm=true -t xtenso .
```

The HTTP server will be available at http://localhost:5000 when the container is run:

```bash
docker run -p 5000:5000 --rm -ti xtenso
```

It's also possible to run unit tests by invoking **pytest** at the end of the `docker run` command:

```bash
docker run -p 5000:5000 --rm -ti xtenso pytest -v
```
