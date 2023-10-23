from setuptools import setup, find_packages

setup(
    name="searx-unit-conversion",
    description="Converts units using pypi library",
    version="0.1",
    author="onscreenproton",
    url="https://github.com/onscreenproton/searx-unit-conversion",
    py_modules=["unit_conversion"],
    entry_points={
        'searxng.plugins' : [
            'onscreenproton.unit-conversion = unit_conversion',
        ]
    },
    zip_safe = False,
)
