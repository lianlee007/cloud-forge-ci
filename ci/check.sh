#!/usr/bin/env bash
set -euo pipefail
mkdir -p reports
control="${1:?Indique lint, tests, sast, secrets o sca}"
case "$control" in
  lint) python -m ruff check app tests --output-format concise > reports/lint.txt 2>&1 ;;
  tests) python -m pytest -q --junitxml=reports/tests.xml > reports/tests.txt 2>&1 ;;
  sast) python -m bandit -r app -f txt -o reports/sast.txt ;;
  secrets|sca)
    scanners=secret
    extra=(--secret-config security/trivy-secret.yaml)
    if [[ "$control" == sca ]]; then
      scanners=vuln
      extra=(--severity HIGH,CRITICAL)
    fi
    docker run --rm -v "$PWD:/work" -w /work       aquasec/trivy:0.61.1 fs --scanners "$scanners"       --exit-code 1 --skip-dirs .git,.venv,reports,dist       --skip-files requirements-dev.txt       "${extra[@]}" --format table --output "reports/$control.txt" .
    ;;
  *) echo "Control no reconocido"; exit 2 ;;
esac
