#!/usr/bin/env python3
import connexion
import pandas
import os
import datetime

from optparse import OptionParser

import yaws.controllers


default_park_info_column_park_name = 'park_name'
default_park_info_column_timezone = 'timezone'
default_park_info_column_energy_type = 'energy_type'
default_production_column_datetime = 'datetime'


class Yaws:
    def __init__(self, parks):
        self._parks = {park.info()[default_park_info_column_park_name]: park for park in parks}

    def list_parks(self):
        return [name for name in self._parks.keys()], 200

    def get_park_info(self, name):
        if name not in self._parks.keys():
            return '', 404
        return self._parks[name].info(), 200

    def get_park_production(self, name, at):
        if name not in self._parks.keys():
            return '', 404
        return self._parks[name].production(at), 200


class Park:
    def __init__(self, info, production):
        self._info = info
        self._production = production

    def info(self):
        return self._info.to_dict(orient='records')[0]

    def production(self, date):
        interest_date = datetime.datetime.fromisoformat(date)
        next_date = interest_date + datetime.timedelta(1)

        return self._production.loc[
            (pandas.to_datetime(self._production[default_production_column_datetime]) >= interest_date) &
            (pandas.to_datetime(self._production[default_production_column_datetime]) < next_date)
        ].to_dict(orient='records')


def main():
    default_park_info_filename = 'park_info.csv'

    parser = OptionParser()
    parser.add_option("-d", "--datadir", dest="datadir", help="the directory containing data files")
    (options, args) = parser.parse_args()

    park_info_data = pandas.read_csv(os.path.join(options.datadir, default_park_info_filename))

    known_parks = [
        Park(
            park_info_data.loc[park_info_data[default_park_info_column_park_name] == name],
            pandas.read_csv(os.path.join(options.datadir,
                                         f'{name}.csv'))
        ) for name in park_info_data[default_park_info_column_park_name]
    ]
    app = connexion.App(__name__, specification_dir='../api/')
    app.add_api('open_api.yaml',
                arguments={'title': 'Sample API'},
                pythonic_params=True)

    yaws.controllers.pimpl = Yaws(known_parks)

    app.run(port=8080)


if __name__ == '__main__':
    main()
