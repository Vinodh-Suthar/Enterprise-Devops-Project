from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
def home():
    return {
            "message": "Devops App is running"
            "Timestamp" : str(datetime.datetime.now())
            }

@app.get("/health")
def health():
    return {
            "Status" : "Healthy",
            "Service" : "User-Service",
            "Version" : "1.0"
            "Time" : str(datetime.datetime.now())

            }

@app.get("/users")
def get_user():
    return {
            "users" : [
                {"id" : 1 ,"Name" : "Vinodh"},
                {"id" : 2 ,"Name" : "Devops Learner"}
            ]
    }

