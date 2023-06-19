import json

class Project :
    id_counter = 0
    def __init__(self, name:str, type:str):
        self.name = name
        self.type = type
        self.stitch_count = 0
        self.notes = ""
        self.active = True
        self.id = Project.id_counter
        Project.id_counter += 1

    def update_stitch(self, new_stitch_count:int) :
        stitchCount = new_stitch_count

    def set_active(self) :
        self.active = True
        
    def set_nonactive(self) : 
        self.active = False

    def add_note(self, note: str) :
        notes = note

    def save_project_data(self) -> dict :
        #  do not use pickle - not readable outside of python, can be dangerous. json is fine
        jsonify = {
            "name" : self.name,
            "id" : self.id,
            "type" : self.type,
            "stitch count" : self.stitch_count,
            "notes" : self.notes
        }
        with open("projects.json", "a") as file :
            json.dump(jsonify, file) 