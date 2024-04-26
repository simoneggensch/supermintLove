import struct

class McCarthys:
    Name = ''
    Date = None
    Authors = []
    CategoryNames = []
    Categories = []
    GoogleDriveURL = ""

    
    def __init__(self, dict):
        self.Name = dict['title']
        self.Date = None
        self.Authors = []
        self.CategoryNames = dict['round_titles']
        self.Categories = dict['round_topics']
        self.GoogleDriveURL = ''

