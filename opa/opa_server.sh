#!/bin/bash

opa run --server \
  --addr localhost:8181 \
  --set=decision_logs.console=true \
  --log-level debug \
  policies/
