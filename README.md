# biblioteczka_wsb

venv:
python -m venv venv

instalacja:
python -m pip install -r ./requirements/test.txt

uruchomienie kodu: python ./main.py
(trzeba być w katalogu src, albo z PyCharm uruchamiając moduł main.py)

uruchomienie testów: python -m pytest tests

Lintery: do czyszczenia i sprawdzania czytelności kodu:
python -m black .
python -m isort .
python -m ruff .