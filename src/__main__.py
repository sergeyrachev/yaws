#!/usr/bin/env python3
import connexion


def main():
    app = connexion.App(__name__, specification_dir='../api/')
    app.add_api('open_api.yaml',
                arguments={'title': 'Sample API'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()