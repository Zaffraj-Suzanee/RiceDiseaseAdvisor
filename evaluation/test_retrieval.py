import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)


from agents.retrieval_agent import retrieval_agent


test_queries = [

    {
        "question": "What causes rice blast disease?",
        "expected": "Magnaporthe oryzae fungus"
    },

    {
        "question": "Symptoms of bacterial leaf blight",
        "expected": "yellowing leaves and bacterial infection"
    },

    {
        "question": "How to prevent rice blast disease?",
        "expected": "fungicide, resistant varieties, sanitation"
    },

    {
        "question": "What causes brown spot disease?",
        "expected": "Bipolaris oryzae fungus"
    },

    {
        "question": "How to manage nitrogen deficiency?",
        "expected": "nitrogen fertilizer management"
    }

]


total = len(test_queries)

successful = 0


print("\n")
print("=" * 60)
print("RAG RETRIEVAL EVALUATION")
print("=" * 60)



for item in test_queries:

    question = item["question"]

    expected = item["expected"]


    state = {

        "question": question,

        "messages": []

    }


    result = retrieval_agent(state)


    documents = result["documents"]


    print("\nQUESTION")
    print(question)


    print("\nEXPECTED INFORMATION")
    print(expected)


    print("\nRETRIEVED DOCUMENT COUNT")
    print(len(documents))


    print("\nTOP RETRIEVED CONTENT")


    found = False


    for doc in documents:

        text = doc[:300]

        print("----------------")
        print(text)


        if any(
            word.lower() in doc.lower()
            for word in expected.split()
        ):

            found = True



    if found:

        successful += 1

        print("\nRESULT: Relevant ✅")

    else:

        print("\nRESULT: Needs Review ⚠️")



    print("=" * 60)



accuracy = (successful / total) * 100


print("\nFINAL EVALUATION")

print("----------------")

print("Queries Tested:", total)

print("Relevant Retrievals:", successful)

print("Retrieval Accuracy:", accuracy, "%")