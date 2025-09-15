from fastapi import FastAPI
from src.api.v1.endpoints import  resume
from src.core.database import create_db_and_tables

app = FastAPI()


    
    
create_db_and_tables()
print("Database tables created. Including routers...")

# app.include_router(company.router, tags=['company'])
# app.include_router(education.router, tags=['education'])
# app.include_router(profile.router, tags=['profile'])
# app.include_router(project.router, tags=['project'])
# app.include_router(skill.router, tags=['skill'])
# app.include_router(professional_experience.router, tags=['professional_experience'])
# app.include_router(project_category.router, tags=['project_category'])
# app.include_router(tech_profile.router, tags=['tech_profile'])
# app.include_router(language.router, tags=['language'])


print("All routers included. Starting uvicorn server...")

app.include_router(resume.router, tags=['resume'] )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
