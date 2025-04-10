import json
import os
from collections import defaultdict
import sys

def calculate_accuracy(data):
    total_correct = 0
    total_items = len(data)
    
    dimension_stats = defaultdict(lambda: {"correct": 0, "total": 0})
    duration_stats = {
        "0-60": {"correct": 0, "total": 0},
        "60-300": {"correct": 0, "total": 0},
        "300+": {"correct": 0, "total": 0}
    }
    
    for item in data:
        if item.get("answer_scoring") == '1':
            total_correct += 1
        
        dimension = item.get("dimension")
        if dimension:
            dimension_stats[dimension]["total"] += 1
            if item.get("answer_scoring") == '1':
                dimension_stats[dimension]["correct"] += 1
        
        duration = item.get("duration", 0)
        if duration <= 60:
            key = "0-60"
        elif duration <= 300:
            key = "60-300"
        else:
            key = "300+"
        
        duration_stats[key]["total"] += 1
        if item.get("answer_scoring") == '1':
            duration_stats[key]["correct"] += 1
    
    overall_accuracy = total_correct / total_items if total_items > 0 else 0

    dimension_accuracy = {}
    for dimension, stats in dimension_stats.items():
        dimension_accuracy[dimension] = stats["correct"] / stats["total"] if stats["total"] > 0 else 0

    duration_accuracy = {}
    for key, stats in duration_stats.items():
        duration_accuracy[key] = stats["correct"] / stats["total"] if stats["total"] > 0 else 0
    
    return {
        "overall_accuracy": overall_accuracy,
        "dimension_accuracy": dimension_accuracy,
        "duration_accuracy": duration_accuracy
    }

def format_results(results):
    formatted_results = {}

    formatted_results["Overall Accuracy"] = f"{results['overall_accuracy']:.3f}"

    formatted_results["Accuracy by Dimension"] = {
        dimension: f"{accuracy:.3f}" for dimension, accuracy in results["dimension_accuracy"].items()
    }

    formatted_results["Accuracy by Duration"] = {
        duration: f"{accuracy:.3f}" for duration, accuracy in results["duration_accuracy"].items()
    }
    
    return formatted_results

def main(file_path):
    # Load data from the provided file path
    data = json.load(open(file_path, 'r', encoding='utf-8'))
    
    results = calculate_accuracy(data)
    formatted_results = format_results(results)

    print("===== Statistics =====")
    print("Overall Accuracy:", formatted_results["Overall Accuracy"])
    print("\nAccuracy by Dimension:")
    for dimension, accuracy in formatted_results["Accuracy by Dimension"].items():
        print(f"  {dimension}: {accuracy}")
    print("\nAccuracy by Duration:")
    for duration, accuracy in formatted_results["Accuracy by Duration"].items():
        print(f"  {duration}: {accuracy}")

    print('\n\n')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    
    input_file = sys.argv[1]
    main(input_file)