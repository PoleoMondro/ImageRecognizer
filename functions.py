import pickle
import os

# To save a dic "dic" to the path "pathToDic"
def saveDic(pathToDic, dic):
    with open(pathToDic, 'wb') as f:
        pickle.dump(dic, f, protocol=pickle.HIGHEST_PROTOCOL)

# To load a dic from the path "pathToDic"
def loadDic(pathToDic):
    with open(pathToDic, 'rb') as f:
        return pickle.load(f)

# to get all folder's name into into path "path"
def getAllDirNames(path):
    return [name for name in os.listdir(path) if os.path.isdir(path+'/'+name)]

# Get all file names into a folder
def getAllFilenames(path):
    return os.listdir(path)
