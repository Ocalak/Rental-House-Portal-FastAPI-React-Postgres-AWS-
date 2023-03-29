
![final](https://user-images.githubusercontent.com/96614838/228536442-28c99eab-2a10-402e-9a62-d755429aed02.png)
![final](https://user-images.githubusercontent.com/96614838/228536433-83fddd9d-5da9-4fcb-b8f7-97902f0ebd61.png)


```bash
git clone[ https://github.com/Ocalak/world-wide-wohnung.git](https://github.com/Ocalak/World-Wide-Wohnung)

cd backend

python -m venv env 

source env\bin\activate 

pip install -r .\requirements.txt

uvicorn main:app --reload     #start server 

visit  https://127.0.0.1:8000/docs 
