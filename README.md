# SearX Unit Conversion

A simple [SearXNG](https://docs.searxng.org/) plugin to convert units using [Pint](https://pint.readthedocs.io/)

## Installation

Install the plugin by running:
```console
$ sudo utils/searxng.sh instance cmd bash -c
(searxng-pyenv)$ pip install pint git+https://github.com/onscreenproton/searx-unit-conversion
```
or install in a docker container by
```console
$ docker exec -it foo sh
/usr/local/searxng # pip install pint git+https://github.com/onscreenproton/searx-unit-conversion
```

## Usage

Convert units by searching (for example) `convert 1kg to lbs`` in SearXNG