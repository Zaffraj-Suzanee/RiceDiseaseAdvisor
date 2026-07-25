from graph import run_graph

result = run_graph(
    "What are the symptoms of rice blast disease?"
)

print("\nFINAL ADVICE\n")
print(result["final_answer"])