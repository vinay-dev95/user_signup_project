from fastapi import FastAPI,HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import UserSignup,Userlogin, User, Base
from auth import authenticate_user, create_access_token
# from models import UserLogin

from utils import hash_password


app = FastAPI()

#create DB tables
Base.metadata.create_all(bind=engine)


#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):
    #check if user already exists
    
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    #create a new user
    new_user = User(name=user.name, 
                    email=user.email, 
                    password=hash_password(user.password))
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "Signup successful", "user": user.email}
        

@app.post("/login")
def login(user:Userlogin, db:Session = Depends(get_db)):
    auth_user = authenticate_user(user.email, user.password, db)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid emial or password")
    
    token = create_access_token(data={"sub":auth_user.email})
    return {"access_token":token, "token_type":"bearer"}
    