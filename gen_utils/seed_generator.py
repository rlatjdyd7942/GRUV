import numpy as np

#A very simple seed generator
#Copies a random example's first seed_length sequences as input to the generation algorithm
def generate_copy_seed_sequence(seed_length, training_data):
	num_examples = training_data.shape[0]
	example_len = training_data.shape[1]
	randIdx = np.random.randint(num_examples - seed_length, size=1)[0]
	print(len(training_data[randIdx]))
	print(len(training_data[randIdx][0]))
	randSeed = np.concatenate(tuple([training_data[randIdx + i] for i in range(seed_length)]), axis=0)
	print(randSeed.shape)
	seedSeq = np.reshape(randSeed, (1, randSeed.shape[0], randSeed.shape[1]))
	return seedSeq