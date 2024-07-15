#!/usr/bin/env bash

set -e

exec poetry run celery -A repetitor.project worker --loglevel=info --concurrency 1 -E
