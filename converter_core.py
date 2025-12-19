#!/usr/bin/env python3
# © 2025 HEIC Converter

from typing import Union
from pathlib import Path
import io
from PIL import Image
from pillow_heif import register_heif_opener

# Register the HEIF opener with Pillow
register_heif_opener()

class HeicConverter:
    """Core converter class for handling HEIC/HEIF image conversions."""
    
    @staticmethod
    def convert_heic(input_data: Union[bytes, Path], output_format: str = "JPEG") -> bytes:
        """Convert HEIC/HEIF image to the specified format.
        
        Args:
            input_data: Either a Path object pointing to the input file or bytes containing the image data
            output_format: Target format (JPEG, PNG, WEBP, BMP, HEIC)
            
        Returns:
            bytes: Converted image data
            
        Raises:
            ValueError: If the input format is invalid or conversion fails
        """
        try:
            # Handle both file path and bytes input
            if isinstance(input_data, Path):
                image = Image.open(input_data)
            else:
                image = Image.open(io.BytesIO(input_data))
            
            # Normalize HEIC to HEIF for Pillow compatibility
            save_format = "HEIF" if output_format.upper() == "HEIC" else output_format
            
            # Determine if the target format supports alpha channel
            supports_alpha = save_format.upper() in ('PNG', 'WEBP', 'HEIF')
            
            # Convert image mode based on alpha channel support
            if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
                # Image has transparency
                if supports_alpha:
                    image = image.convert('RGBA')
                else:
                    # Formats like JPEG and BMP don't support alpha, convert to RGB
                    image = image.convert('RGB')
            else:
                image = image.convert('RGB')
            
            # Save to bytes
            output = io.BytesIO()
            image.save(output, format=save_format)
            return output.getvalue()
            
        except Exception as e:
            raise ValueError(f"Failed to convert image: {str(e)}")
    
    @staticmethod
    def get_extension_for_format(format_name: str) -> str:
        """Get the appropriate file extension for the specified format.
        
        Args:
            format_name: The format name (JPEG, PNG, WEBP, BMP, HEIC)
            
        Returns:
            str: The file extension (without dot)
        """
        format_extensions = {
            "JPEG": "jpg",
            "PNG": "png",
            "WEBP": "webp",
            "BMP": "bmp",
            "HEIC": "heic",
            "HEIF": "heif"
        }
        return format_extensions.get(format_name.upper(), "jpg") 