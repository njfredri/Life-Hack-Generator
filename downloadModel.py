from gpt2_client import GPT2Client

gpt2 = GPT2Client('345M')
gpt2.load_model(force_download=False)
