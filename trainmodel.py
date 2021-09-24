# from gpt2_client import GPT2Client
# import os
# gpt2 = GPT2Client('117M') # This could also be `345M`, `774M`, or `1558M`

# my_corpus = './data/steps.txt' # path to corpus
# if os.path.exists(my_corpus):
# 	print("heje")
# custom_text = gpt2.finetune(my_corpus, return_text=True, steps=1) # Load your custom dataset

import gpt_2_simple as gpt2
import os
import requests

model_name = "117M"
if not os.path.isdir(os.path.join("models", model_name)) and not os.path.isdir(os.path.join("checkpoint", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/


file_name = "data/steps.txt"
if not os.path.isfile(file_name):
	url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
	data = requests.get(url)
	
	with open(file_name, 'w') as f:
		f.write(data.text)
    

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              file_name,
              model_name=model_name,
              steps=20,
			  save_every=10,
			  model_dir='models',
			  run_name='lifehacks'
			  ) 