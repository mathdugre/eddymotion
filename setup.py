"""EMC's setup script."""
import sys

from setuptools import setup

# Give setuptools a hint to complain if it's too old a version
# 30.3.0 allows us to put most metadata in setup.cfg
# Should match pyproject.toml
# Not going to help us much without numpy or new pip, but gives us a shot
SETUP_REQUIRES = ["setuptools >= 40.8", "setuptools_scm", "setuptools_scm_git_archive"]
# This enables setuptools to install wheel on-the-fly
SETUP_REQUIRES += ["wheel"] if "bdist_wheel" in sys.argv else []


if __name__ == "__main__":
    setup(
        name="eddymotion",
        use_scm_version=True,
        setup_requires=SETUP_REQUIRES,
    )
