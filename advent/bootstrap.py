import inject
import os
from yaml import load
import advent


def configure(binder):

    cfg_path = os.path.join(advent.__file__.strip("__init__.py"), "config/config.yml")
    with open(cfg_path, "r") as c:
        yml = load(c.read())
    cfg = advent.Config(**yml)

    binder.bind(advent.Config, cfg)


def bootstrap():
    inject.configure(configure)
