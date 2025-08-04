#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DDS File Scanner
Scans all .dds files in the current directory and generates JSON files in specified format

Author: HK560
GitHub: https://github.com/HK560
"""

import os
import json
import argparse
import glob
from pathlib import Path


def scan_dds_files(path_prefix="", output_file="output.json", verbose=False):
    """
    Scan all .dds files in the current directory and generate JSON file
    
    Args:
        path_prefix (str): Path prefix, e.g. "texture\\models\\weapons\\r99zeropoint\\"
        output_file (str): Output JSON filename
        verbose (bool): Show detailed output
    """
    # Get all .dds files in current directory
    dds_files = glob.glob("*.dds")
    dds_files.sort()  # Sort by filename
    
    if not dds_files:
        print("No .dds files found in current directory")
        return False
    
    if verbose:
        print(f"Found {len(dds_files)} .dds files:")
        for dds_file in dds_files:
            print(f"  - {dds_file}")
        print()
    
    # Build JSON data structure
    json_data = {
        "files": []
    }
    
    processed_count = 0
    error_count = 0
    
    for dds_file in dds_files:
        try:
            # Get filename without extension
            file_name = Path(dds_file).stem
            
            # Build full path
            if path_prefix:
                full_path = path_prefix + '\\' + file_name
            else:
                full_path = file_name
            
            # Add to JSON data
            file_entry = {
                "$type": "txtr",
                "path": full_path,
                # "saveDebugName": True,
                "disableStreaming": True
            }
            
            json_data["files"].append(file_entry)
            processed_count += 1
            
            if verbose:
                print(f"Processed: {dds_file} → {full_path}")
                
        except Exception as e:
            print(f"Error processing {dds_file}: {e}")
            error_count += 1
    
    # Write JSON file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent='\t', ensure_ascii=False)
        
        print(f"Successfully processed {processed_count} .dds files")
        if error_count > 0:
            print(f"Failed to process {error_count} files")
        print(f"JSON file generated: {output_file}")
        
        return True
        
    except Exception as e:
        print(f"Error writing JSON file: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="DDS File Scanner - Generate JSON files from .dds files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
DESCRIPTION:
This tool scans all .dds files in the current directory and generates a JSON file
with the specified format for game asset management systems.

The generated JSON contains file entries with the following structure:
{
    "$type": "txtr",
    "path": "texture\\models\\weapons\\weapon_name",
    "disableStreaming": true
}

USAGE EXAMPLES:
  python scan_dds_files.py
  python scan_dds_files.py --prefix "texture\\models\\weapons\\r99zeropoint\\"
  python scan_dds_files.py --output "weapon_textures.json"
  python scan_dds_files.py --verbose
  python scan_dds_files.py --prefix "texture\\models\\weapons\\" --output "weapons.json"

OUTPUT FORMAT:
The tool generates a JSON file with an array of file entries, each containing:
• $type: Always "txtr" for texture files
• path: Full path to the texture (without .dds extension)
• disableStreaming: Set to true to prevent streaming
        """
    )
    
    parser.add_argument(
        "--prefix", "-p", 
        default="", 
        help="Path prefix for the texture files (e.g., texture\\models\\weapons\\r99zeropoint\\)"
    )
    
    parser.add_argument(
        "--output", "-o", 
        default="output.json", 
        help="Output JSON filename (default: output.json)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed processing information"
    )
    
    args = parser.parse_args()
    
    print("=== DDS File Scanner ===")
    print("Author: HK560 | GitHub: https://github.com/HK560")
    print("=" * 50)
    print(f"Scanning directory: {os.getcwd()}")
    print(f"Path prefix: {args.prefix if args.prefix else '(none)'}")
    print(f"Output file: {args.output}")
    if args.verbose:
        print("Verbose mode: Enabled")
    print("-" * 50)
    
    success = scan_dds_files(args.prefix, args.output, args.verbose)
    
    if success:
        print("\nScan completed successfully!")
        print("=" * 50)
        print("Author: HK560 | GitHub: https://github.com/HK560")
        return 0
    else:
        print("\nScan completed with errors!")
        print("=" * 50)
        print("Author: HK560 | GitHub: https://github.com/HK560")
        return 1


if __name__ == "__main__":
    exit(main()) 