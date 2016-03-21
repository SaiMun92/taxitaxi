import os 

# create a varName file and write into it
def serialize(vector, varName):
	print("serialize [" + varName + "]"),
	f = open('serialize/' + varName, 'w+')
	for item in vector:
		print(item, file=f)
	f.close()
	print(" ... DONE")

# put the data into a list
def unserialize(varName):
	print ("unserialize [" + varName + "]"),
	fname = 'serialize/' + varName
	with open(fname) as f:
		vector = f.readlines()
	data = []
	for item in vector:
		data.append(float(item))
	print("... DONE")
	return data

def clean_serialization_folder():
	print("Cleaning serialization folder"),
	folder = 'serialize/'
	# iterate every file in the folder and delete them
	for the_file in os.listdir(folder):
		file_path = os.path.join(folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
		except Exception as e:
			print(e)
	print("... DONE")
