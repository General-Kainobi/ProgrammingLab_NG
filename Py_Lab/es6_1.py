class CsvFile():
        def __init__(self, name, start, end):
            if type(name)!= str:
                raise Exception(f"Error: File name must be of string type: you provided file name of type: {type(name)}\n")
            else: 
                self.name=name
            if type(int(start))==int and type(int(end))==int:
                self.start=int(start)
                self.end=int(end)
            else:
                raise Exception(f"Invalid type of start or end range input, Expected Int or convertible, was given {type(start)} and {type(end)}")                       
        def getdata(self, start=2, end=None):
            try:
                d_list=[]
                with open(self.name, 'r') as filed:
                        try:
                            if filed:    
                                lines=filed.readlines()
                                mas=len(lines)
                                if end==None: end=mas
                                if end<=mas and start>0 and start<end:
                                    for line in lines:
                                        d_list = [line.strip().split(',') for line in lines[start-1:end]]
                                else:
                                        raise Exception(f"Error: Invalid number of lines, provided range from {start} to {end} but file only has 0-{mas} lines")     
                            else:
                                raise Exception(f"Error: File {self.name} is empty")
                        except Exception as e:
                            print (f"Error {e} \n")
            except Exception as e:
                print("Errore: {}", format(e))
            finally: 
                return d_list
        def __str__(self):
            return(self.name)