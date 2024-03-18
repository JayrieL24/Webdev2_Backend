BACK END SET-UP
Requirements - Anaconda/Miniconda, Xampp , Visual Studios
Download - https://drive.google.com/drive/folders/1PYYQGlvmTB0PahlPzG_ezIqhCi6mr20p?usp=sharing (database and source code is already in this gdrive folder note!!!: I will update the files in this gdrive folder)

--Anaconda Setup-- 
1. conda create --name GearGuards python=3.9
2. press "y" then press enter key
3. conda activate GearGuards
4. pip install fastapi uvicorn mysql-connector-python
5. uvicorn main:app --reload
6. pip install bycrpt
7. uvicorn main:app --reload
8. pip install python-multipart
9. uvicorn main:app --reload
10. http://127.0.0.1:8000/docs

--Xampp Setup--
1.press start on apache and mysql
2.press admin on mysql (you will open myphpadmin)
3.create new database
4.name the database "gearguards"
5.import gearguards.sql

--done--

--STATUS OF BACKEND--

03/16/2024 - Database And BackEnd Connected
03/18/2024 - 3/5 CRUD OPERATIONS COMPLETE 



    
