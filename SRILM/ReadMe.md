./ngram-count -text ../../../HumanSentsTrain.txt -order 1 -lm ../../../Human.1gram.lm -unk -addsmooth 1
./ngram-count -text ../../../HumanSentsTrain.txt -order 2 -lm ../../../Human.2gram.lm -unk -addsmooth 1
./ngram-count -text ../../../HumanSentsTrain.txt -order 3 -lm ../../../Human.3gram.lm -unk -addsmooth 1 
./ngram-count -text ../../../NotHumanSentsTrain.txt -order 1 -lm ../../../NotHuman.1gram.lm -unk -addsmooth 1
./ngram-count -text ../../../NotHumanSentsTrain.txt -order 2 -lm ../../../NotHuman.2gram.lm -unk -addsmooth 1
./ngram-count -text ../../../NotHumanSentsTrain.txt -order 3 -lm ../../../NotHuman.3gram.lm -unk -addsmooth 1

./ngram -ppl ../../../HumanSentsTrain.txt -lm ../../../Human.1gram.lm
  641 sentences, 4686 words, 0 OOVs
0 zeroprobs, logprob= -10913.02 ppl= 111.8471 ppl1= 213.2343
./ngram -ppl ../../../HumanSentsTrain.txt -lm ../../../Human.2gram.lm
 641 sentences, 4686 words, 0 OOVs
0 zeroprobs, logprob= -11268.64 ppl= 130.4314 ppl1= 253.9488
./ngram -ppl ../../../HumanSentsTrain.txt -lm ../../../Human.3gram.lm
 641 sentences, 4686 words, 0 OOVs
0 zeroprobs, logprob= -11606.86 ppl= 150.9643 ppl1= 299.8633
./ngram -ppl ../../../NotHumanSentsTrain.txt -lm ../../../NotHuman.1gram.lm
 625 sentences, 4184 words, 0 OOVs
0 zeroprobs, logprob= -9803.873 ppl= 109.3078 ppl1= 220.3849
./ngram -ppl ../../../NotHumanSentsTrain.txt -lm ../../../NotHuman.2gram.lm
 625 sentences, 4184 words, 0 OOVs
0 zeroprobs, logprob= -10092.25 ppl= 125.4922 ppl1= 258.2886
./ngram -ppl ../../../NotHumanSentsTrain.txt -lm ../../../NotHuman.3gram.lm
 625 sentences, 4184 words, 0 OOVs
0 zeroprobs, logprob= -10407.16 ppl= 145.9149 ppl1= 307.1636
./ngram -ppl ../../../HumanSentsTest.txt -lm ../../../Human.1gram.lm
 161 sentences, 1171 words, 0 OOVs
0 zeroprobs, logprob= -3337.532 ppl= 320.3719 ppl1= 708.1989
./ngram -ppl ../../../HumanSentsTest.txt -lm ../../../Human.2gram.lm
 161 sentences, 1171 words, 0 OOVs
0 zeroprobs, logprob= -3348.489 ppl= 326.4978 ppl1= 723.6224
./ngram -ppl ../../../HumanSentsTest.txt -lm ../../../Human.3gram.lm
 161 sentences, 1171 words, 0 OOVs
0 zeroprobs, logprob= -3356.444 ppl= 331.0188 ppl1= 735.0308
./ngram -ppl ../../../NotHumanSentsTest.txt -lm ../../../NotHuman.1gram.lm
 157 sentences, 1138 words, 0 OOVs
0 zeroprobs, logprob= -3185.954 ppl= 288.5336 ppl1= 630.3887
./ngram -ppl ../../../NotHumanSentsTest.txt -lm ../../../NotHuman.2gram.lm
 157 sentences, 1138 words, 0 OOVs
0 zeroprobs, logprob= -3194.653 ppl= 293.0309 ppl1= 641.582
./ngram -ppl ../../../NotHumanSentsTest.txt -lm ../../../NotHuman.3gram.lm
 157 sentences, 1138 words, 0 OOVs
0 zeroprobs, logprob= -3207.76 ppl= 299.9402 ppl1= 658.8244

./ngram -lm ../../../Human.1gram.lm -gen 10 -seed
./ngram -lm ../../../Human.2gram.lm -gen 10 -seed
./ngram -lm ../../../Human.3gram.lm -gen 10 -seed
./ngram -lm ../../../NotHuman.1gram.lm -gen 10 -seed
./ngram -lm ../../../NotHuman.2gram.lm -gen 10 -seed
./ngram -lm ../../../NotHuman.3gram.lm -gen 10 -seed