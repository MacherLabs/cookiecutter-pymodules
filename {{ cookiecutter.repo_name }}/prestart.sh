#!/bin/sh

echo "Running inside /app/prestart.sh, you could add migrations and checks to this file."

if [ $? -ne 0 ]
then
        exit 1
else
        echo "Pre-start check ran successfully"
fi
