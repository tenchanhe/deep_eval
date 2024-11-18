from deepeval.benchmarks import MMLU
from deepeval.benchmarks.tasks import MMLUTask

from llm import LLM
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Evaluate LLM on Traditional Chinese + English datasets using litellm")
parser.add_argument("--model", type=str, default="ollama/llama3.1:8b", help="Model name for litellm API")
parser.add_argument("--response_file", type=str, required=False, help="Path to save response")
parser.add_argument("--score_file", type=str, required=True, help="Path to save evaluation results")
args = parser.parse_args()

if __name__ == "__main__":
    model = LLM(model=args.model)

    benchmark = MMLU(
        tasks=[MMLUTask.HIGH_SCHOOL_COMPUTER_SCIENCE],
        n_shots=0
    )

    benchmark.evaluate(model=model)
    print(benchmark.overall_score)
    print("Task-specific Scores: ", benchmark.task_scores)
    # print("Detailed Predictions: ", benchmark.predictions)
    benchmark.task_scores.to_csv(args.score_file, index=False)
    if args.response_file:
        benchmark.predictions.to_csv(args.response_file, index=False)
