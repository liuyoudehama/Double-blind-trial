import os;
import csv;

class DownloadList(object):
	def __init__(self):
		self.len = 0
		self.NameList = []
		self.SourceList = []
		self.StartList = []
		self.EndList = []

	def ReadFromFile(self):
		with open('sourcelink.csv', newline='') as f:
			reader = csv.reader(f)
			print("header_begin")
			row = reader.__next__()
			print(row)
			print("header_end")
			while True:
				try:
					row = reader.__next__()
					print(row)
					
					#Todo: handle index exceed exception
					assert(len(row) == 4)

					self.NameList.append(row[0])
					self.SourceList.append(row[1])
					self.StartList.append(row[2])
					self.EndList.append(row[3])
					self.len = self.len + 1 

				except StopIteration:
					break

	def GetDownloadCommand(self, index):
		#Todo: handle index exceed exception
		assert(index < len(self.SourceList))
		assert(index < len(self.NameList))

		cmd_string = "youtube-dl -x --audio-format mp3 "
		cmd_string = cmd_string + self.SourceList[index]
		return cmd_string
		
	def GetLen(self):
		return self.len

class Download(object):
	def __init__(self, dl_list):
		self.dl_list = dl_list

	def download(self):
		for source_index in range(self.dl_list.GetLen()):
			os.system(self.dl_list.GetDownloadCommand(source_index));

def main():
	dl_list = DownloadList()
	dl_list.ReadFromFile()
	dl = Download(dl_list)
	dl.download()

if __name__ == '__main__':
	main()