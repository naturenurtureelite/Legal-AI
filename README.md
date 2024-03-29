# Legal-AI


All the datasets have been obtained from [https://github.com/Law-AI/summarization]

We have reused the IN-Ext and IN-Abs dataset from [https://github.com/Law-AI/summarization]
-------------------------------------------------------------------------------------------------------------------------------------------------

All the datasets are available in **dataset** folder. In addition to the original documents and the expert written gold standard summaries we have additionally provided the outputs of the base algorithms in the **dataset** folder

-------------------------------------------------------------------------------------------------------------------------------------------------


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


The folder **IN-Ext summaries** contains the summaries generated by the various methods. There are multiple methods namely **Simple voting**, **Borda Count**, **Reciprocal Ranking**, **Vecsim-Greedy-Length**, **Vecsim-Greedy-degree**, **Roundrobin-length**, **Roundrobin-degree**, **Pagerank**, **Node2vec**, **HITS-authority**, **HITS-hub**.
Every folder has 6 sub-folders having the summaries generated by 6 different variations namely **All methods**, **Supervised**, **unsupervised**, **unsupervised domain independent**, **unsupervised domain specific**, **Top 4**.

-----------------------------------------------------------------------------------------------------------------------------------------------



The folder **IN-Abs summaries** contains the summaries generated by the various methods. There are multiple methods namely **Simple voting**, **Borda Count**, **Reciprocal Ranking**, **Vecsim-Greedy-Length**, **Vecsim-Greedy-degree**, **Roundrobin-length**, **Roundrobin-degree**, **Pagerank**, **Node2vec**, **HITS-authority**, **HITS-hub**.
Every folder has 8 sub-folders having the summaries generated by 8 different variations namely **All methods**, **Supervised**, **unsupervised**, **unsupervised domain independent**, **unsupervised domain specific**,**Top 2**,**Top 3**,**Top 4**.

-----------------------------------------------------------------------------------------------------------------------------------------------




