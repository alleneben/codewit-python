class FileReader:
    def __init__(self):
        print('this is the filereader constructor')

    
    def datareader(self,filename):
        with open(filename,'r') as file:
            for line in file:
                print(line)


    def datareader2(self, filename):
        age=[]
        height=[]
        temp=[]
        with open(filename, 'r') as file:
            for line in file:
                age.append(int(line[0]))
                height.append(int(line[2]))
                temp.append(float(line[4]))
        
        return age,height,temp