main:
	pyinstaller --clean --specpath build/specs -n colour-lib -F src/main.py
	
clean:
	rm -r build/colour-lib
	rm -r src/__pycache__

pip:
	pip install .