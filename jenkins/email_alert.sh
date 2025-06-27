#!/bin/bash

TO="admin@mh-cybersolutions.de"
SUBJECT=" Jenkins Alert: Suspicious Activity Detected"
BODY="Suspicious login or failed build detected in CI/CD pipeline. Please review alert_report.csv."

echo "$BODY" | mail -s "$SUBJECT" "$TO"
