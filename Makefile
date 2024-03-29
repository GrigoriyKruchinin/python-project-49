install:
	poetry install

brain-games:
	poetry run brain-games

brain-calc:
	poetry run brain-calc

brain-even:
	poetry run brain-even

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain_prime:
	poetry run brain-prime

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall  --user dist/*.whl

lint:
	poetry run flake8 brain_games

.PHONY: install brain-games brain-calc brain-even brain-gcd brain-progression brain-prime build publish package-inistall lint
