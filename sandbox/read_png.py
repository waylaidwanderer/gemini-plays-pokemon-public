import zlib
import struct

def read_png_pixels(path):
    with open(path, "rb") as f:
        signature = f.read(8)
        if signature != b"\x89PNG\r\n\x1a\n":
            print("Not a valid PNG file!")
            return
            
        width, height = 0, 0
        idat_data = b""
        
        while True:
            header = f.read(8)
            if not header or len(header) < 8:
                break
            length, chunk_type = struct.unpack(">I4s", header)
            data = f.read(length)
            crc = f.read(4)
            
            if chunk_type == b"IHDR":
                width, height, bit_depth, color_type, compression, filter_method, interlace = struct.unpack(">IIBBBBB", data)
                print(f"PNG Image size: {width}x{height}, Bit depth: {bit_depth}, Color type: {color_type}")
            elif chunk_type == b"IDAT":
                idat_data += data
            elif chunk_type == b"IEND":
                break
                
        if not idat_data:
            print("No IDAT chunk found!")
            return
            
        # Decompress pixel data
        try:
            decompressed = zlib.decompress(idat_data)
        except Exception as e:
            print(f"Failed to decompress IDAT data: {e}")
            return
            
        print(f"Decompressed data size: {len(decompressed)} bytes")
        
        # PNG has a 1-byte filter type at the start of each row
        # Let's reconstruct the image
        bytes_per_pixel = 3 if color_type == 2 else 4 if color_type == 6 else 1
        print(f"Bytes per pixel: {bytes_per_pixel}")
        
        row_stride = 1 + width * bytes_per_pixel
        pixels = []
        prev_row = [0] * (width * bytes_per_pixel)
        
        for r in range(height):
            row_data = decompressed[r * row_stride : (r + 1) * row_stride]
            if not row_data:
                break
            filter_type = row_data[0]
            scanline = list(row_data[1:])
            
            recon_row = []
            for c in range(width * bytes_per_pixel):
                x = scanline[c]
                a = recon_row[c - bytes_per_pixel] if c >= bytes_per_pixel else 0
                b = prev_row[c]
                c_val = prev_row[c - bytes_per_pixel] if c >= bytes_per_pixel else 0
                
                # Apply filter reconstruction
                if filter_type == 0: # None
                    val = x
                elif filter_type == 1: # Sub
                    val = (x + a) & 255
                elif filter_type == 2: # Up
                    val = (x + b) & 255
                elif filter_type == 3: # Average
                    val = (x + (a + b) // 2) & 255
                elif filter_type == 4: # Paeth
                    p = a + b - c_val
                    pa = abs(p - a)
                    pb = abs(p - b)
                    pc = abs(p - c_val)
                    if pa <= pb and pa <= pc:
                        pr = a
                    elif pb <= pc:
                        pr = b
                    else:
                        pr = c_val
                    val = (x + pr) & 255
                else:
                    val = x
                recon_row.append(val)
                
            prev_row = recon_row
            pixels.append(recon_row)
            
        print(f"Reconstructed {len(pixels)} scanlines.")
        
        # Downsample and print a 2D ASCII art of average brightness
        cols, rows = 60, 20
        cell_w = width // cols
        cell_h = height // rows
        
        for r in range(rows):
            line = ""
            for c in range(cols):
                tot = 0
                count = 0
                for dy in range(cell_h):
                    for dx in range(cell_w):
                        py = r * cell_h + dy
                        px = c * cell_w + dx
                        idx = px * bytes_per_pixel
                        if py < len(pixels) and idx < len(pixels[py]):
                            # Calculate average of RGB
                            if bytes_per_pixel >= 3:
                                val = (pixels[py][idx] + pixels[py][idx+1] + pixels[py][idx+2]) // 3
                            else:
                                val = pixels[py][idx]
                            tot += val
                            count += 1
                avg = tot // count if count > 0 else 255
                # Map to ASCII
                if avg < 60:
                    line += "#"
                elif avg < 110:
                    line += "o"
                elif avg < 160:
                    line += "+"
                elif avg < 210:
                    line += "."
                else:
                    line += " "
            print(line)

print("Decoding area3_row25_fence_gap.png...")
read_png_pixels("screenshots/cropped/area3_row25_fence_gap.png")
