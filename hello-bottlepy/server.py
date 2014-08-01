# Copyright (c) 2011-2014 Paul Nelson (Pablosan@SalientBlue.com)
# All Rights Reserved.
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""HTTP (REST API) Server."""

import logging

import bottle
from configargparse import configargparse

LOG = logging.getLogger(__name__)


@bottle.route('/')
def index():
  return "<h1>Hello from bottlepy!</h1>"


def start(options):
    """Start the server. Called by __main__."""
    LOG.info("*** hello-bottlepy v%s ***", '0.0.1')

    host = options.host or '0.0.0.0'
    port = options.port or 80

    # Start listening. Enable reload by default to pick up file changes
    bottle.run(server='tornado', host=host, port=port, reloader=options.reloader)


def main():
    """Entrypoint for __main__."""

    # Configuration options: config file, command line params, environment vars
    parser = configargparse.ArgParser(default_config_files=['/etc/settings.ini'])
    parser.add('--host',
               help='host name (e.g. "mydomain.com", defaults to "0.0.0.0")',
               env_var='HOST')
    parser.add('-p', '--port', help='TCP port for the server. Defaults to 80',
               env_var='PORT', type=int)
    parser.add('-r', '--reload', dest='reloader', action='store_true',
               help='Set auto-reload to True to automatically pick up file '
               'changes. Defaults to False.',
               env_var='RELOAD')
    parser.set_defaults(reloader=False)

    options = parser.parse_args()

    # Output config info for easier setup and debugging
    print(parser.format_help())
    print("-----")
    print(options)
    print("-----")
    parser.print_values()

    # Start the server
    start(options)


if __name__ == "__main__":
    main()
