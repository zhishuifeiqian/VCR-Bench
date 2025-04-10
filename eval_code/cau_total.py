from collections import defaultdict
import json
import sys

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_metrics(data):
    total_stats = defaultdict(lambda: {"precision_sum": 0, "precision_count": 0, 
                                      "recall_sum": 0, "recall_count": 0,
                                      "efficiency_sum": 0, "efficiency_count": 0})
    
    for item in data:
        for metric in ["Video", "logic", "overall"]:
            precision = item.get(f"{metric}_precision", '')
            recall = item.get(f"{metric}_recall", '')

            if precision != '':
                total_stats[metric]["precision_sum"] += precision
                total_stats[metric]["precision_count"] += 1

            if recall != '':
                total_stats[metric]["recall_sum"] += recall
                total_stats[metric]["recall_count"] += 1

    overall_metrics = {}
    for metric, stats in total_stats.items():
        precision = stats["precision_sum"] / stats["precision_count"] if stats["precision_count"] > 0 else 0
        recall = stats["recall_sum"] / stats["recall_count"] if stats["recall_count"] > 0 else 0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        overall_metrics[metric] = {
            "precision": precision,
            "recall": recall,
            "f1": f1
        }

    return {
        "overall_metrics": overall_metrics
    }

def format_metrics_results(results):
    def format_dict(d):
        return {k: f"{v:.3f}" if isinstance(v, (int, float)) else v for k, v in d.items()}

    return {
        "Overall Metrics": {metric: format_dict(stats) for metric, stats in results["overall_metrics"].items()}
    }

def print_results(formatted_results):
    print("===== Metrics Summary =====")
    print("Overall Metrics:")
    for metric, stats in formatted_results["Overall Metrics"].items():
        print(f"  {metric}:")
        for key, value in stats.items():
            print(f"    {key}: {value}")

if __name__ == "__main__":
    # Check if file path was provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file_path>")
        sys.exit(1)
    
    # Get file path from command line argument
    input_file = sys.argv[1]
    
    # Load and process data
    data = load_data(input_file)
    results = calculate_metrics(data)
    formatted_results = format_metrics_results(results)
    
    # Print results
    print_results(formatted_results)