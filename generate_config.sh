#!/bin/bash

case "$1" in
    local|circleci)
        STAGE=$1
        echo "Generate configs for stage: " $STAGE
        ;;
    *)
        echo
        echo "Usage:"
        echo "    $0    local | circleci"
        echo
        exit 2
        ;;
esac

if [ $STAGE == 'local' ]
then
    sed -f $PWD/config/local.sed $PWD/config/config.tmpl.yml > $PWD/config/config.yml
fi

echo "Finish to generate config file (config.yml)"
