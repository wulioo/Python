
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml'],
    environments=True

)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.
if __name__ == '__main__':
    print(settings.get('tor.proxy'))