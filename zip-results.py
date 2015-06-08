import os, zipfile, requests

def download_project_commit():
	master_commit = requests.get('https://github.com/larissaleite/HamptonsBank/archive/master.zip')

	output = open("results/master_code.zip", "w")
	output.write(master_commit.content)
	output.close()

def zipdir(path, ziph):
	for root, dirs, files in os.walk(path):
		for file in files:
			ziph.write(os.path.join(root, file))

if __name__ == '__main__':
	download_project_commit()

	zipf = zipfile.ZipFile('build-result.zip', 'w')
	zipdir('results', zipf)
	zipf.close()