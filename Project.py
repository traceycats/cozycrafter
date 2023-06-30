## TODO : finish making getters/setters

class Project :
    id_counter = 0
    def __init__(self, name:str, type:str):
        self.name = name
        self.type = type
        self.pattern = None
        self.stitch_count = 0
        self.notes = None
        self.active = True
        self.id = Project.id_counter
        Project.id_counter += 1

    # name of the project - eventually might want to make this default to name of the pattern
    @property 
    def name(self) :
        return self.name
    
    @name.setter
    def name(self, new_name) :
        self.name = new_name
    
    # type- crochet or knit    
    @property 
    def type(self) :
        return self.type
    
    @type.setter
    def type(self, new_type) :
        self.type = new_type
        
    # pattern - eventually want to be able to read pdf patterns but need to do a lot more research on that
    @property 
    def pattern(self) :
        return self.pattern
    
    @pattern.setter
    def pattern(self, new_pattern) :
        self.pattern = new_pattern
    
    def update_stitch(self, new_stitch_count:int) :
        stitchCount = new_stitch_count

    def set_active(self) :
        self.active = True
        
    def set_nonactive(self) : 
        self.active = False

    def add_note(self, note: str) :
        notes = note
    