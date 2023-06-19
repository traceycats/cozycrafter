import json

class Project :
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stitch_count = 0
        self.notes = ""

    def update_stitch(self, newStitchCount) :
        stitchCount = newStitchCount

    def add_note(self, note) :
        notes = note

    def save_project_data(self) :
        #  do not use pickle - not readable outside of python, can be dangerous. json is fine
        jsonify = {
            "name" : self.name,
            "type" : self.type,
            "stitch count" : self.stitch_count,
            "notes" : self.notes
        }
        with open("projects.json", "w") as file :
            json.dump(jsonify, file) 