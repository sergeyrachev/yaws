
pimpl = None


def list_parks():
    return pimpl.list_parks()


def get_park_info(name):
    return pimpl.get_park_info(name)


def get_park_production(name, at):
    return pimpl.get_park_production(name, at)
