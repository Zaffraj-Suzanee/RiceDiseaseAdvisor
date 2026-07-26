from graph import run_graph


question = "What are symptoms of rice blast disease?"


result = run_graph(question)


print("\n\nAGENT COMMUNICATION FLOW")
print("="*40)


for message in result["messages"]:

    print("\nSender:",
          message["sender"])

    print("Receiver:",
          message["receiver"])

    print("Task:",
          message["task"])

    print("Status:",
          message["status"])


print("\n\nFINAL ADVICE")
print("="*40)


print(
    result.get(
        "answer",
        "No answer generated"
    )
)