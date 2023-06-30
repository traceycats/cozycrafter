import sqlite3 
from sqlalchemy import Column, String, Integer, Boolean 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProjectLibrary(Base) : # project inherits from Base - declarative base
    __tablename__ = "projects"
    project_id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    active_project = Column("active", Boolean)

    def __init__(self, project: Project) :
        self.project_id = project.get_project_id