import pandas as pd
import os

class Data_Preprocessor:
    
    
    def __init__(self, filename):
        
        self.current_directory = os.getcwd()
        self.csv_file = os.path.join(self.current_directory, filename)
        self.data = self.load_data()

    def load_data(self):
        
        df = pd.read_csv(self.csv_file)
                
        return df
    
    
    def data_formatter(self, data):
        
        
            
        
