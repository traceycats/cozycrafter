from ProjectClass import Project

class ProjectLibrary : 
    id_counter = 0
    def __init__(self) :
        self.library = dict()
        self.active_project = None
        
    def get_project_data(self, project_id: int, project_name: str) :
        pass