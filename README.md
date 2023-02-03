# Legal-AI


All the datasets have been obtained from [https://github.com/Law-AI/summarization]

We have reused the IN-Ext and IN-Abs dataset from [https://github.com/Law-AI/summarization]

---------------------------------------------------------------------------------------------------------------------------------------------
**DATASET for IN-Ext dataset**

The 50 Original documents in the IN-Ext dataset is available in Full-Text/India.

The Expert written gold standard summaries is available in Expert-Summaries/India.

There are two expert written summaries corresponding to every original document in two folders named A1 and A2 written by two independent legal experts.

The Algorithm generated summaries is available at Algo-Summaries/India. 

The expert written summaries are of length atmost 1/3rd of the length of the original documents.

---------------------------------------------------------------------------------------------------------------------------------------------



---------------------------------------------------------------------------------------------------------------------------------------------
**DATASET for IN-Abs dataset**

The 100 Original documents in the IN-Abs dataset is available in test-data/judgement.

The Expert written gold standard summaries is available in test-data/summary.

There is one abstractive gold standard summary corresponding to every document.

The first column in test-data/Stats-IN-test.txt gives filename, second column gives no of words in original document, third column gives no of words in the expert written summary.


---------------------------------------------------------------------------------------------------------------------------------------------

The are 15 summarization algorithms namely Lexrank,LSA, Luhn, Reduction, DSDR, LetSum, KMM, DSDR, DELSumm, Case Summarizer, SummaRunner/Attn_RNN, SummaRunner/CNN_RNN, SummaRunner/RNN_RNN, BERTSUM, Chinese Gist

The supervised summarization algorithms are:-  SummaRunner/Attn_RNN, SummaRunner/CNN_RNN, SummaRunner/RNN_RNN, BERTSUM, Chinese Gist

The unsupervised domain independent algorithms are:- Lexrank,LSA, Luhn, Reduction, DSDR

The unsupervised domain specific algorithms are:-  LetSum, KMM, DSDR, DELSumm, Case Summarizer

The unsupervised algorithms are:- Lexrank,LSA, Luhn, Reduction, DSDR, LetSum, KMM, DSDR, DELSumm, Case Summarizer

The supervised algorithms are:-SummaRunner/Attn_RNN, SummaRunner/CNN_RNN, SummaRunner/RNN_RNN, BERTSUM, Chinese Gist

The top 4 summarization algorithms are:- BERTSUM, SummaRunner/Attn_RNN, SummaRunner/RNN_RNN and DELSumm

The various ensembling techniques tried are- **Simple Voting, Borda Count, Reciprocal Ranking, Vecsim-Greedy-Length, Vecsim-Greedy-Degree, Vecsim-Roundrobin-Length, Vecsim-Roundrobin-degree, Pagerank, Hits authority, HITS hub, Node2vec, Deepwalk.**

----------------------------------------------------------------------------------------------------------------------------------------------


 All the codes are available in **codes** folder 



-----------------------------------------------------------------------------------------------------------------------------------------------

