#!/usr/bin/env python3
"""
Script to record the AI_API_KEY from environment into README.md
"""
import os
import sys

def update_readme_with_api_key():
    """Read AI_API_KEY from environment and append it to README.md"""
    # Get the API key from environment
    ai_api_key = os.environ.get('AI_API_KEY')
    
    if not ai_api_key:
        print("Warning: AI_API_KEY environment variable is not set")
        ai_api_key = "[Not set - please configure AI_API_KEY environment variable]"
    
    readme_path = 'README.md'
    
    # Read current README content
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Check if API key is already recorded
    if 'AI_API_KEY' in content:
        print("AI_API_KEY already exists in README.md")
        # Update the value if different
        if ai_api_key not in content:
            # Replace the line containing AI_API_KEY
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if 'AI_API_KEY' in line:
                    lines[i] = f"AI_API_KEY: {ai_api_key}"
            content = '\n'.join(lines)
            with open(readme_path, 'w') as f:
                f.write(content)
            print(f"Updated AI_API_KEY in README.md to: {ai_api_key}")
        return True
    
    # Append the API key to README
    if not content.endswith('\n'):
        content += '\n'
    
    content += f"\nAI_API_KEY: {ai_api_key}\n"
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"Successfully recorded AI_API_KEY in README.md: {ai_api_key}")
    return True

if __name__ == '__main__':
    success = update_readme_with_api_key()
    sys.exit(0 if success else 1)
