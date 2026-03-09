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
    def convert_heic(input_data: Union[bytes, Path], output_format: str = "JPEG", quality: int = 85) -> bytes:
        """Convert HEIC/HEIF image to the specified format.
        
        Args:
            input_data: Either a Path object pointing to the input file or bytes containing the image data
            output_format: Target format (JPEG, PNG, WEBP, BMP, HEIC)
            quality: Output quality for lossy formats (1-100, default 85)
            
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

            # Convert image mode based on alpha support and current mode
            has_transparency = (
                image.mode in ('RGBA', 'LA') or
                (image.mode == 'P' and 'transparency' in image.info)
            )
            if has_transparency:
                image = image.convert('RGBA' if supports_alpha else 'RGB')
            elif image.mode not in ('RGB', 'L'):
                # Preserve grayscale; convert palette/other modes to RGB
                image = image.convert('RGB')
            
            # Save to bytes, passing quality for lossy formats
            output = io.BytesIO()
            save_kwargs: dict = {"format": save_format}
            if save_format.upper() in ('JPEG', 'WEBP', 'HEIF'):
                save_kwargs["quality"] = quality
            image.save(output, **save_kwargs)
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