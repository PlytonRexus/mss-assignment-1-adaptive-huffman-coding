import sys
from adaptive_huffman_coding import compress, extract

# 'images/mrbrain.dcm', 'images/2.dcm', 'images/3.dcm', 
# 'images/4.dcm', 'images/5.dcm', 'images/6.dcm'

def main():
    filename = 'images/' + sys.argv[1]
    alphabet_range = (0, 255)  # m = 256
    if len(sys.argv) > 2 and sys.argv[2] == 'compress':
        compress(filename, 'compressed/' + filename[7:] + '.compressed.adaptive.huffman',
                 alphabet_range=alphabet_range)
    if len(sys.argv) > 3 and sys.argv[3] == 'decompress':
        extract('compressed/' + filename[7:] + '.compressed.adaptive.huffman',
                'decompressed/' + filename[7:] + '.extracted.dcm', alphabet_range=alphabet_range)


if __name__ == '__main__':
    main()
