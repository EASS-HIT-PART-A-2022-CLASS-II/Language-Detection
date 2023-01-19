# Language-Detection  

Language-Detection is a tool for inorder to ideanfy what languease is the text . It checks strings and texts
for now its based on 
https://www.kaggle.com/datasets/basilb2s/language-detection dataset
and supports 17 Languages
* English
* Malayalam
* Hindi
* Tamil
* Kannada
* French
* Spanish
* Portuguese
* Italian
* Russian
* Sweedish
* Dutch
* Arabic
* Turkish
* German
* Danish
* Greek

# How to use
go to the next url:
https://fastapi-test-backend.herokuapp.com/predict

send a json with the following format:
inorder to get prediction for the input

# ui update 
![img_1.png](img_1.png)
# more examples
![img_2.png](img_2.png)
# future plans:
- [x] Create backend using FASTAPI 
- [x] Connect the ML model to the FASTAPI framework
- [x] Added Dockerfile to the backend
- [x] Create frontend using the Streamlit
- [x] Added Dockerfile to the frontend
- [x] Integrate between frontend and backend
- [ ] to add docker compose 
- [ ] to deploy the project in heroku

# how to deploy
 deployment for the Backend
```
docker build -t [enter some name to the file] .
docker run -p  80:80 [the previous name]
```
deployment for the Frontend
```
docker build -t [enter some name to the file] .
docker run -p  8501:8501 [the previous name]
```
