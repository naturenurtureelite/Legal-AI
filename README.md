# Legal-AI


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

The various ensembling techniques tried are- **Simple Voting, Borda Count, Reciprocal Ranking, Vecsim-Greedy-Length, Vecsim-Greedy-Degree.**





---------------------------------------------------------------------------------------------------------------------------------------------
**SIMPLE VOTING**

------------------------------------------------------------------------------------

For ensembling the **supervised algorithms** using **simple voting** please run,

**python tead25.py supervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------

For ensembling the **unsupervised domain independent algorithms** using **simple voting** please run,

**python tead25.py unsupervised_domain_independent**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------


For ensembling the **unsupervised_domain_specific algorithms** using **simple voting** please run,

**python tead25.py unsupervised_domain_specific**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the **unsupervised algorithms** using **simple voting** please run,

**python tead25.py unsupervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the **Top 4 best performing summarization algorithms** using simple voting please run,

**python tead25.py top_4**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **all 15 summarization algorithms** using **simple voting** please run,

**python tead25.py all_methods**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------


**BORDA COUNT**

-----------------------------------------------------------------------------------------------------------------------
For running Borda Count the instructions are as follows:-

For ensembling the **supervised algorithms** using **borda count** please run,

**python tead25_borda.py supervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the **unsupervised domain independent algorithms** using **borda count** please run,

**python tead25_borda.py unsupervised_domain_independent**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the unsupervised_domain_specific algorithms using borda count please run,

**python tead25_borda.py unsupervised_domain_specific**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the **unsupervised algorithms** using **borda count** please run,

**python tead25_borda.py unsupervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **Top 4 best performing summarization algorithms** using **borda count** please run,

**python tead25_borda.py top_4**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **all 15 summarization algorithms** using **borda count**  please run,

**python tead25_borda.py all_methods**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------


**RECIPROCAL RANKING**

-------------------------------------------------------------------------------------


For running **Reciprocal ranking** the instructions are as follows:-

For ensembling the **supervised algorithms** using **reciprocal ranking** please run,

**python tead25_reciprocal.py supervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------





For ensembling the **unsupervised domain independent algorithms** using **reciprocal ranking** please run,

**python tead25_reciprocal.py unsupervised_domain_independent**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **unsupervised_domain_specific algorithms** using **reciprocal ranking** please run,

**python tead25_reciprocal.py unsupervised_domain_specific**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **unsupervised algorithms** using **reciprocal ranking** please run,

**python tead25_reciprocal.py unsupervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **Top 4 best performing summarization algorithms** using **reciprocal ranking** please run,

**python tead25_reciprocal.py top_4**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------





For ensembling the **all 15 summarization algorithms** using **reciprocal ranking** please run,

**python tead25_reciprocal.py all_methods**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------


**VECSIM_GREEDY_LENGTH**

-------------------------------------------------------------------------------------------------------------------------
For running **Vecsim Greedy length** the instructions are as follows:-

For ensembling the **supervised algorithms** using **Vecsim Greedy Length** please run,

**python tead_graph_greedylength.py supervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **unsupervised domain independent algorithms** using **Vecsim Greedy Length** please run,

**python tead_graph_greedylength.py unsupervised_domain_independent**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------





For ensembling the **unsupervised_domain_specific algorithms** using **Vecsim Greedy Length** please run,

**python tead_graph_greedylength.py unsupervised_domain_specific**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **unsupervised algorithms** using **Vecsim Greedy Length** please run,

**python tead_graph_greedylength.py unsupervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------





For ensembling the **Top 4 best performing summarization algorithms** using **Vecsim Greedy Length** please run,

**python tead_graph_greedylength.py top_4**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the **all 15 summarization algorithms** using **Vecsim Greedy Length** please run,

**python tead_graph_greedylength.py all_methods**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------


**VECSIM_ROUNDROBIN_LENGTH**

---------------------------------------------------------------------------------------------------------------------------
For running **Vecsim Roundrobin length** the instructions are as follows:-

For ensembling the **supervised algorithms** using **Vecsim Roundrobin Length** please run,

**python tead_graph_roundrobin_length.py supervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **unsupervised domain independent algorithms** using **Vecsim Roundrobin Length** please run,

**python tead_graph_roundrobin_length.py unsupervised_domain_independent**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the **unsupervised_domain_specific algorithms** using **Vecsim Roundrobin Length** please run,

**python tead_graph_roundrobin_length.py unsupervised_domain_specific**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **unsupervised algorithms** using **Vecsim Roundrobin Length** please run,

**python tead_graph_roundrobin_length.py unsupervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **Top 4 best performing summarization algorithms** using **Vecsim Roundrobin Length** please run,

**python tead_graph_roundrobin_length.py top_4**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the **all 15 summarization algorithms** using **Vecsim Roundrobin Length** please run,

**python tead_graph_roundrobin_length.py all_methods**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------
**VECSIM_ROUNDROBIN_DEGREE**

---------------------------------------------------------------------------------------------------------------------------
For running **Vecsim Roundrobin degree** the instructions are as follows:-

For ensembling the **supervised algorithms** using **Vecsim Roundrobin degree** please run,

**python tead_graph_roundrobindegree.py supervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **unsupervised domain independent algorithms** using **Vecsim Roundrobin degree** please run,

**python tead_graph_roundrobindegree.py unsupervised_domain_independent**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the **unsupervised_domain_specific algorithms** using **Vecsim Roundrobin Degree** please run,

**python tead_graph_roundrobindegree.py unsupervised_domain_specific**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **unsupervised algorithms** using **Vecsim Roundrobin Degree** please run,

**python tead_graph_roundrobindegree.py unsupervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **Top 4 best performing summarization algorithms** using **Vecsim Roundrobin Degree** please run,

**python tead_graph_roundrobindegree.py top_4**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the **all 15 summarization algorithms** using **Vecsim Roundrobin Degree** please run,

**python tead_graph_roundrobindegree.py all_methods**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------
**VECSIM_GREEDY_DEGREE**

---------------------------------------------------------------------------------------------------------------------------
For running **Vecsim Greedy degree** the instructions are as follows:-

For ensembling the **supervised algorithms** using **Vecsim Greedy degree** please run,

**python tead_graph_greedydegree.py supervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **unsupervised domain independent algorithms** using **Vecsim Greedy degree** please run,

**python tead_graph_greedydegree.py unsupervised_domain_independent**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the **unsupervised_domain_specific algorithms** using **Vecsim Greedy Degree** please run,

**python tead_graph_greedydegree.py unsupervised_domain_specific**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **unsupervised algorithms** using **Vecsim Greedy Degree** please run,

**python tead_graph_greedydegree.py unsupervised**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------




For ensembling the **Top 4 best performing summarization algorithms** using **Vecsim Greedy Degree** please run,

**python tead_graph_greedydegree.py top_4**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------



For ensembling the **all 15 summarization algorithms** using **Vecsim Greedy Degree** please run,

**python tead_graph_greedydegree.py all_methods**

**python ranking_summaries.py unordered**

The results will be generated in **ordered** folder


------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------
