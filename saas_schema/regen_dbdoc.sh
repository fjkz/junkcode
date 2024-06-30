#!/bin/bash
set -eux -o pipefail
mysql -h $(hostname) -P 3306 -uroot -p${MYSQL_ROOT_PASSWORD} mysaas < drop_tables.sql
mysql -h $(hostname) -P 3306 -uroot -p${MYSQL_ROOT_PASSWORD} mysaas < schema.sql
tbls doc mysql://root:${MYSQL_ROOT_PASSWORD}@$(hostname):3306/mysaas --force
