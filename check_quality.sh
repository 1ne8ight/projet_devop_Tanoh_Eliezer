echo "== Flake8 =="
flake8 application tests
echo "== Black =="
black --check application tests
echo "== isort =="
isort --check-only application tests
