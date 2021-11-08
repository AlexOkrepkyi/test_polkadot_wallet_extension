# test_polkadot_wallet_extension

1. Install python:
```
sudo apt-get install python3
```
2. Install pip3:
```
sudo apt-get -y install python3-pip
```
3. Clone the project and navigate to the folder with that cloned project.

4. Install pipenv:
```
pip3 install pipenv
```
5a. If the virtualenv is already activated, use:
```
pipenv sync --dev
```
5b. If the virtualenv is NOT activated, use:
```
pipenv install --dev
```
6. Run all tests:
```
pytest
```
