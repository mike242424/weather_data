import pandas

dog_dict = {
    "name": ['Rocco', "Coffee"],
    "breed" : ['Treeing Walker Coonhound', 'American English Coonhound']
}

data = pandas.DataFrame(dog_dict)
data.to_csv('new_data.csv')
print(data)