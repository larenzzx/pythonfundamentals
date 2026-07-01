import os
import json
import re

def compile_lessons():
    lessons = []
    # Find all lesson python files
    lesson_files = [f for f in os.listdir('.') if f.startswith('lesson') and f.endswith('.py') and f != 'compile_lessons.py']
    
    # Sort files by the numeric ID in their name (e.g. lesson1 -> 1, lesson10 -> 10)
    def extract_id(filename):
        match = re.search(r'lesson(\d+)', filename)
        return int(match.group(1)) if match else 999
        
    lesson_files.sort(key=extract_id)
    
    for filename in lesson_files:
        lesson_id = extract_id(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract title from the file
        title = filename
        for line in content.split('\n'):
            match = re.search(r'# Lesson \d+:\s*(.*)', line)
            if match:
                title = match.group(1).strip()
                break
                
        # Split code into legacy section slices for type-checking compliance
        lines = content.split('\n')
        tutorial_lines = []
        activity_lines = []
        challenge_lines = []
        
        current_section = 'tutorial'
        
        for line in lines:
            trimmed = line.strip()
            # Detect section dividers
            if 'Activity' in trimmed and ('Section' in trimmed or '============' in trimmed):
                current_section = 'activity'
                continue
            elif 'Mini Challenge' in trimmed or '============Mini Challenge==========' in trimmed:
                current_section = 'challenge'
                continue
                
            if current_section == 'tutorial':
                tutorial_lines.append(line)
            elif current_section == 'activity':
                activity_lines.append(line)
            elif current_section == 'challenge':
                challenge_lines.append(line)
                
        lessons.append({
            "id": lesson_id,
            "filename": filename,
            "title": title,
            "content": content,
            "sections": {
                "tutorial": '\n'.join(tutorial_lines).strip(),
                "activity": '\n'.join(activity_lines).strip(),
                "challenge": '\n'.join(challenge_lines).strip()
            }
        })
        
    # Write to src/data/lessons.json
    output_path_src = os.path.join('src', 'data', 'lessons.json')
    with open(output_path_src, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)
        
    # Write to lessons_data.json at root
    output_path_root = 'lessons_data.json'
    with open(output_path_root, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)
        
    print(f"Successfully compiled {len(lessons)} lessons to {output_path_src} and {output_path_root}")

if __name__ == '__main__':
    compile_lessons()
