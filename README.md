create environment:  conda create --prefix .env python=3.7 -y
Activate environment conda activate ./env

create dvc.yaml params.yaml .gitignore setup.py

create empty files:
mkdir -p src/utils config
touch src/__init__.py src/utils/__init__.py param.yaml dvc.yaml config/config.yaml src/stage_01_load_save.py src/utils/all_utils.py setup.py .gitignore