PY=python
all: figures
figures:
	$(PY) src/figure01_woelders.py
	$(PY) src/figure02_falkenstein.py
	$(PY) src/figure03_aigner_dhaliwal.py
	$(PY) src/figure04_break_even_stable_risky.py
	$(PY) src/figure05_break_even_vs_rho.py
clean:
	rm -f figures/*.png
	rm -f data/processed/*.csv

.PHONY: refs
refs:
	python scripts/generate_references.py
