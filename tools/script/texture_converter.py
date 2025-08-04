#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Standalone Texture Converter Tool
Converts PNG files to DDS format with support for different compression formats

Author: HK560
GitHub: https://github.com/HK560
"""

import os
import sys
import subprocess
import argparse


def convert_textures(texconv_path, asset_path=None, skip_existing=False, backup=False):
    """
    Convert PNG files in the specified directory to DDS format
    
    Args:
        texconv_path (str): Path to texconv.exe or None to search in PATH
        asset_path (str): Directory path to process, defaults to current directory
        skip_existing (bool): Whether to skip existing DDS files
        backup (bool): Whether to backup existing files before overwriting
    """
    if asset_path is None:
        asset_path = os.getcwd()
    
    # If texconv_path is None, search for texconv in PATH
    if texconv_path is None:
        texconv_path = "texconv"
    elif not os.path.isabs(texconv_path):
        # If relative path provided, search in PATH
        texconv_path = "texconv"
    
    # Check if texconv exists (either as full path or in PATH)
    if os.path.isabs(texconv_path):
        if not os.path.exists(texconv_path):
            print(f"Error: texconv path does not exist: {texconv_path}")
            return False
    else:
        # Check if texconv is available in PATH
        try:
            subprocess.run([texconv_path, "-h"], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"Error: texconv not found in PATH. Please ensure texconv.exe is available in your system PATH or provide the full path.")
            return False
    
    if not os.path.exists(asset_path):
        print(f"Error: Asset directory does not exist: {asset_path}")
        return False
    
    print(f"Processing directory: {asset_path}")
    print(f"Using texconv: {texconv_path}")
    print(f"Overwrite mode: {'No (skip existing files)' if skip_existing else 'Yes'}")
    if backup and not skip_existing:
        print(f"Backup mode: Yes")
    print("-" * 50)
    
    converted_count = 0
    error_count = 0
    skipped_count = 0
    
    # Scan for PNG files in directory
    for filename in os.listdir(asset_path):
        if not filename.lower().endswith('.png'):
            continue
            
        file_path = os.path.join(asset_path, filename)
        if not os.path.isfile(file_path):
            continue
            
        # Generate corresponding DDS filename
        dds_filename = os.path.splitext(filename)[0] + '.dds'
        dds_path = os.path.join(asset_path, dds_filename)
        
        print(f"Processing file: {filename}")
        
        # Check if DDS file already exists
        if os.path.exists(dds_path):
            if skip_existing:
                print(f"  ⚠️  DDS file already exists, skipping: {dds_filename}")
                skipped_count += 1
                continue
            else:
                if backup:
                    # Create backup
                    backup_path = dds_path + '.backup'
                    try:
                        if os.path.exists(backup_path):
                            os.remove(backup_path)
                        os.rename(dds_path, backup_path)
                        print(f"  📦  Backed up existing file: {dds_filename}.backup")
                    except Exception as e:
                        print(f"  ⚠️  Backup failed: {e}")
                else:
                    print(f"  🔄  Overwriting existing file: {dds_filename}")
        
        # Determine compression format based on filename
        if filename.lower().endswith("nml.png"):
            # Normal maps use BC5_UNORM
            tex_conv_args_list = [
                texconv_path, 
                "-f", "BC5_UNORM", 
                "-srgb", 
                "-ft", "dds", 
                file_path, 
                "-o", asset_path,
                "-y"  # Auto-overwrite files
            ]
            print(f"  → Using BC5_UNORM format (Normal map)")
            
        elif filename.lower().endswith(("gls.png", "msk.png","ao.png")):
            # Glossiness and mask maps use BC4_UNORM
            tex_conv_args_list = [
                texconv_path, 
                "-f", "BC4_UNORM", 
                "-srgbi", 
                "-ft", "dds", 
                file_path, 
                "-o", asset_path,
                "-y"  # Auto-overwrite files
            ]
            print(f"  → Using BC4_UNORM format (Glossiness/Mask map/AO map)")
        else:
            # Other textures use BC7_UNORM_SRGB
            tex_conv_args_list = [
                texconv_path, 
                "-f", "BC7_UNORM_SRGB", 
                "-srgbi", 
                "-ft", "dds", 
                file_path, 
                "-o", asset_path,
                "-y"  # Auto-overwrite files
            ]
            print(f"  → Using BC7_UNORM_SRGB format (Standard texture)")

        try:
            # Execute conversion
            result = subprocess.run(tex_conv_args_list, 
                                  capture_output=True, 
                                  text=True, 
                                  shell=True)
            
            if result.returncode == 0:
                print(f"  ✓ Conversion successful")
                converted_count += 1
            else:
                print(f"  ✗ Conversion failed: {result.stderr.strip()}")
                if result.stdout:
                    print(f"     Output: {result.stdout.strip()}")
                error_count += 1
                
        except Exception as e:
            print(f"  ✗ Texture conversion error: {e}")
            error_count += 1
    
    print("-" * 50)
    print(f"Conversion completed!")
    print(f"Successfully converted: {converted_count} files")
    print(f"Conversion failed: {error_count} files")
    if skipped_count > 0:
        print(f"Skipped files: {skipped_count} files (DDS already exists)")
    
    return error_count == 0


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="PNG to DDS Texture Converter Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
DESCRIPTION:
This tool converts PNG texture files to DDS format using Microsoft's texconv utility.
It automatically selects the appropriate compression format based on the texture type:

• Normal maps (*nml.png) → BC5_UNORM (best for normal data)
• Glossiness/Mask maps (*gls.png, *msk.png) → BC4_UNORM (grayscale compression)
• Standard textures (*.png) → BC7_UNORM_SRGB (high quality color compression)

USAGE EXAMPLES:
  python texture_converter.py                    # Use texconv from PATH
  python texture_converter.py "C:/Program Files/texconv.exe"  # Use specific texconv path
  python texture_converter.py --path "D:/textures"
  python texture_converter.py --backup
  python texture_converter.py --skip-existing

REQUIREMENTS:
• Microsoft DirectX Texture Converter (texconv.exe)
• PNG files in the target directory
• Windows operating system

COMPRESSION FORMATS:
  BC5_UNORM:     8:1 compression, ideal for normal maps
  BC4_UNORM:     8:1 compression, grayscale data
  BC7_UNORM_SRGB: 3:1 compression, high quality color with sRGB
        """
    )
    
    parser.add_argument(
        "texconv_path",
        nargs='?',
        default=None,
        help="Full path to texconv.exe (default: search in PATH environment variable)"
    )
    
    parser.add_argument(
        "--path", "-p",
        default=None,
        help="Directory path to process (default: current directory)"
    )
    
    parser.add_argument(
        "--skip-existing", "-s",
        action="store_true",
        help="Skip existing DDS files (default: overwrite)"
    )
    
    parser.add_argument(
        "--backup", "-b",
        action="store_true",
        help="Backup existing DDS files before overwriting"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output"
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.backup and args.skip_existing:
        print("Warning: --backup option is invalid in skip mode")
        args.backup = False
    
    # Validate texconv path
    if args.texconv_path is not None and os.path.isabs(args.texconv_path):
        if not os.path.exists(args.texconv_path):
            print(f"Error: texconv path does not exist: {args.texconv_path}")
            print("Please ensure you provide the correct path to texconv.exe")
            sys.exit(1)
    
    # Set processing path
    process_path = args.path if args.path else os.getcwd()
    
    print("=== PNG to DDS Texture Converter Tool ===")
    print("Author: HK560 | GitHub: https://github.com/HK560")
    print("=" * 50)
    if args.texconv_path:
        print(f"texconv path: {args.texconv_path}")
    else:
        print("texconv: Using system PATH")
    print(f"Processing directory: {process_path}")
    if args.skip_existing:
        print("Mode: Skip existing DDS files")
    else:
        print("Mode: Overwrite existing DDS files (default)")
        if args.backup:
            print("Backup: Yes")
    print()
    
    # Execute conversion
    success = convert_textures(args.texconv_path, process_path, args.skip_existing, args.backup)
    
    if success:
        print("\nAll files converted successfully!")
        print("=" * 50)
        print("Author: HK560 | GitHub: https://github.com/HK560")
        sys.exit(0)
    else:
        print("\nSome files failed to convert, please check error messages")
        print("=" * 50)
        print("Author: HK560 | GitHub: https://github.com/HK560")
        sys.exit(1)


if __name__ == "__main__":
    main() 