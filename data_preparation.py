import pandas as pd
import json
import os
from typing import Dict, List, Any

def load_and_process_json_files() -> pd.DataFrame:
    """
    Load all five JSON files, flatten the nested structure, and combine into one DataFrame.
    
    Returns:
        pd.DataFrame: Combined DataFrame with all comments from all AI sources
    """
    
    # Define the file mappings
    file_mappings = {
        'pr_review_comments_Cursor.json': 'Cursor',
        'pr_review_comments_Devin.json': 'Devin', 
        'pr_review_comments_OpenAI_Codex.json': 'OpenAI_Codex',
        'pr_review_comments_Claude_Code.json': 'Claude_Code',
        'pr_review_comments_Copilot.json': 'Copilot'
    }
    
    all_comments = []
    
    for filename, ai_source in file_mappings.items():
        print(f"Processing {filename}...")
        
        # Load JSON file
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Process each PR and its comments
        for pr_id, comments_list in data.items():
            # Skip empty comment lists
            if not comments_list:
                continue
                
            # Add each comment to our list
            for comment in comments_list:
                # Create a copy of the comment and add metadata
                comment_data = comment.copy()
                comment_data['ai_source'] = ai_source
                comment_data['pr_id'] = pr_id
                all_comments.append(comment_data)
        
        print(f"  - Found {len([c for c in all_comments if c['ai_source'] == ai_source])} comments from {ai_source}")
    
    # Convert to DataFrame
    all_comments_df = pd.DataFrame(all_comments)
    
    print(f"\nTotal comments processed: {len(all_comments_df)}")
    return all_comments_df

def main():
    """Main function to run the data preparation process."""
    
    print("Starting Phase 1: Data Preparation")
    print("=" * 50)
    
    # Load and process all JSON files
    all_comments_df = load_and_process_json_files()
    
    # Display basic information about the dataset
    print("\nDataset Information:")
    print("=" * 30)
    all_comments_df.info()
    
    print("\nFirst 5 rows:")
    print("=" * 20)
    print(all_comments_df.head())
    
    print("\nColumn names:")
    print("=" * 15)
    print(list(all_comments_df.columns))
    
    print("\nAI Source distribution:")
    print("=" * 25)
    print(all_comments_df['ai_source'].value_counts())
    
    # Save the processed data for future use
    output_filename = 'all_comments_processed.csv'
    all_comments_df.to_csv(output_filename, index=False)
    print(f"\nProcessed data saved to: {output_filename}")
    
    return all_comments_df

if __name__ == "__main__":
    all_comments_df = main()
