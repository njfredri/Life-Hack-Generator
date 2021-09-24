import gpt_2_simple as gpt2
import os
import requests
import sys
import threading
class textGenerator:
	def __init__(self):
		self.model_name = "noanimeChat"
		self.sess = gpt2.start_tf_sess()
		gpt2.load_gpt2(sess=self.sess,model_dir='checkpoint',model_name=self.model_name)

	def generateText(self):
		print("clearing text")
		tempfile = open('temp.txt','w')
		tempfile.truncate(0)
		tempfile.close()
		# model_name = "shrek"
		# sess = gpt2.start_tf_sess()
		# gpt2.load_gpt2(sess=sess,model_dir='checkpoint',model_name=model_name)
		# print("loaded. Now creating text")
		gpt2.generate(sess=self.sess, destination_path='temp.txt')
		print(sess)
		print("Ended")
	
	def generateText(self):
		print("clearing text")
		tempfile = open('temp.txt','w')
		tempfile.truncate(0)
		tempfile.close()
		print(self.sess)
		# model_name = "shrek"
		# sess = gpt2.start_tf_sess()
		# gpt2.load_gpt2(sess=sess,model_dir='checkpoint',model_name=model_name)
		# print("loaded. Now creating text")
		gpt2.generate(sess=self.sess, destination_path='temp.txt')
		print("Ended")

# if __name__== '__main__':
# 	x = textGenerator()
# 	x.generateTextInAThread()
# 	print("waiting on thread")
