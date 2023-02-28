backend: 
pip freeze>requirements.txt    
docker build . -t backend
docker run --name backend --rm -p 8000:8000 backend    
uvicorn main:app --reload


frontend: npm start