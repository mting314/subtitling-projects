import json
import re
import argparse
from pathlib import Path

def time_to_ass_format(time_str):
    """Convert 'XXX.XXXs' to 'H:MM:SS.CC' format"""
    # Remove the 's' and convert to float
    seconds = float(time_str.rstrip('s'))
    
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    centisecs = int((seconds % 1) * 100)
    
    return f"{hours}:{minutes:02d}:{secs:02d}.{centisecs:02d}"

def json_to_ass(json_path, output_path, title=None):
    """Convert Google Cloud Speech-to-Text JSON to ASS subtitle format"""
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Derive title from input file name if not provided
    if title is None:
        title = Path(json_path).stem + " Transcript"
    
    # ASS file header
    ass_content = f"""[Script Info]
; Generated from speech-to-text transcript
Title: {title}
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Lato ExtraBold,72,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,4,1.33,2,200,200,60,1
Style: JP,Lato ExtraBold,72,&H00FFFFFF,&H000000FF,&H006381A1,&H00000000,0,0,0,0,100,100,0,0,1,4,1.33,2,200,200,60,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    
    # Process transcripts
    for i, result in enumerate(data['results']):
        if not result['alternatives']:
            continue
        
        # Get the first (highest confidence) alternative
        alt = result['alternatives'][0]
        transcript = alt['transcript'].strip()
        
        if not transcript:
            continue
        
        # Get start time from first word, end time from result
        if alt['words']:
            start_time = alt['words'][0]['startOffset']
        else:
            start_time = "0s"
        
        end_time = result['resultEndOffset']
        
        # Convert to ASS format
        start_ass = time_to_ass_format(start_time)
        end_ass = time_to_ass_format(end_time)
        
        # Determine style based on language
        style = "JP" if result.get('languageCode') == 'ja-jp' else "Default"
        
        # Create dialogue line
        dialogue = f"Dialogue: 0,{start_ass},{end_ass},{style},,0,0,0,,{transcript}\n"
        ass_content += dialogue
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(ass_content)
    
    print(f"Generated ASS file: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Google Cloud Speech-to-Text JSON to ASS subtitle format")
    parser.add_argument("input", help="Path to the input JSON transcript file")
    parser.add_argument("output", help="Path to the output ASS file")
    parser.add_argument("--title", help="Title for the ASS file (optional, defaults to input filename)")
    
    args = parser.parse_args()
    
    json_to_ass(args.input, args.output, args.title)
