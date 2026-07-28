\# RAG Retrieval Evaluation



\## Objective



Evaluate whether the Retrieval-Augmented Generation (RAG) pipeline retrieves relevant rice disease information from the knowledge base.



\---



\# Test Query 1



\## Question



What causes rice blast disease?





\## Retrieved Documents



\- Rice\_Blast\_Disease.pdf

\- Common\_Rice\_Diseases.pdf

\- IRRI\_Rice\_Disease\_Management.pdf





\## Evaluation



Result: Relevant ✅



The retrieved documents contain information about:

\- Magnaporthe oryzae fungus

\- Disease symptoms

\- Environmental conditions

\- Management practices





\---



\# Test Query 2



\## Question



What are symptoms of bacterial leaf blight?





\## Retrieved Documents



\- Bacterial\_Leaf\_Blight.pdf

\- Rice\_Disease\_Manual.pdf





\## Evaluation



Result: Relevant ✅



The documents explain:

\- Leaf yellowing

\- Water-soaked lesions

\- Bacterial infection





\---



\# Test Query 3



\## Question



How can farmers prevent rice blast?





\## Retrieved Documents



\- Rice\_Blast\_Control.pdf

\- Integrated\_Pest\_Management.pdf





\## Evaluation



Result: Relevant ✅





Information retrieved:

\- Resistant varieties

\- Fungicide application

\- Field sanitation





\---



\# Test Query 4



\## Question



What causes brown spot disease?





\## Retrieved Documents



\- Brown\_Spot\_Rice.pdf





\## Evaluation



Result: Relevant ✅





Retrieved information:

\- Bipolaris oryzae fungus

\- Nutrient deficiency relationship





\---



\# Test Query 5



\## Question



How to manage nitrogen deficiency in rice?





\## Retrieved Documents



\- Rice\_Nutrient\_Management.pdf





\## Evaluation



Result: Relevant ✅





Information:

\- Nitrogen application

\- Leaf colour symptoms

\- Fertilizer management





\---



\# Overall Result





Total Queries Tested: 5



Relevant Retrievals: 5



Retrieval Accuracy:



100%





Conclusion:



The RAG pipeline successfully retrieves domain-specific rice disease information and provides relevant context for the reasoning agent.

