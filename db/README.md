-Create Virtual Environment
python -m venv ./venv/

here is my workflow after creating a folder and cd'ing into it:


python
===//
cd venv/bin/
source ./activate
Or just go to the directory:

cd /python_env/bin/
and then

source ./activate
====//

-Create Main app

==============
 uvicorn main:app --reload       
http://127.0.0.1:8000/tuser/