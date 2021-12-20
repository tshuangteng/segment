#!/bin/bash

supervisord -c /opt/app/supervisor/supervisord.conf
# tail -f /etc/profile