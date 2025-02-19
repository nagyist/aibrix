import json
import time
from typing import List, Tuple, Dict

def save_results(self, matching_prompts: List[Tuple[str, int, int, Dict]], 
                target_input_tokens: int, min_output_tokens: int):
    """Save matching prompts to a JSON file."""
    # Only proceed if there are matching prompts to save
    if not matching_prompts:
        print("\nNo matching prompts found, skipping file creation.")
        return
        
    filename = f"result/prompts/prompt_in{target_input_tokens}_out{min_output_tokens}.json"
    
    # Create the benchmark-compatible format
    current_time = int(time.time() * 1000)  # Current timestamp in milliseconds
    benchmark_format = [{
        "Timestamp": current_time,
        "Requests": [{
            "Prompt": prompt,
            "Prompt Length": input_tokens,
            "Output Length": output_tokens,
            # Store additional metadata in a separate field
            "Metadata": {
                "model_response": response_data,
                "temperature": self.temperature
            }
        } for prompt, input_tokens, output_tokens, response_data in matching_prompts]
    }]
    
    # Write the formatted data
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(benchmark_format, f, indent=2)
    
    print(f"\nResults saved to: {filename}")