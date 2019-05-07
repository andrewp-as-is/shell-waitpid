#!/usr/bin/env bash
{ set +x; } 2>/dev/null

sleep 5 & pid1=$!
sleep 10 & pid2=$!
set -- "$pid1" "$pid2"
waitpid "$@"
