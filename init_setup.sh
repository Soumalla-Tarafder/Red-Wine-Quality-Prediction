echo [$(date)]: "START"


echo [$(date)]: "creating env with python 3.8 version" 


conda create --prefix ./redWine python= 3.8 -y


echo [$(date)]: "activating the environment" 

source activate ./redWine

echo [$(date)]: "installing the dev requirements" 

pip install -r requirements.txt

echo [$(date)]: "END" 