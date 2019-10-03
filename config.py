"""
Store variables needed across the project
"""

import os
import dash_html_components as html


# Where images will be served from
STATIC_IMAGE_ROUTE = '/'

# Define the maximal grid dimensions
ROWS_MAX, COLS_MAX = 7, 7
N_GRID = ROWS_MAX * COLS_MAX


# Allowed file extension for image types
IMAGE_TYPES = ['.JPG', '.jpg', '.JPEG', '.jpeg', '.png']

# Globals for the images
img_fname = 'job_done.jpg' # Default image
IMG_PATH = STATIC_IMAGE_ROUTE + img_fname

IMG_STYLE = {'display': 'block', 'height': 'auto', 'max-width': '100%'} # Applies to grid images
#IMG_STYLE = {'display': 'block', 'height': 'auto', 'width': 'auto'}
IMG_STYLE_ZOOM = {'display': 'block', 'height': 'auto', 'max-width': '100%'} # Applies to zoomed image


# Assumes that images are stored in the img/ directory for now
IMAGE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'img')
# List of image objects - pre-load here to avoid re-loading on every grid re-sizing
IMAGE_SRCS = [STATIC_IMAGE_ROUTE + fname for fname in sorted(os.listdir(IMAGE_DIR))]
IMAGE_SRCS = IMAGE_SRCS + [IMG_PATH]*(ROWS_MAX*COLS_MAX - len(IMAGE_SRCS))

# Where the image folders should be copied to before deleting images in the original location
IMAGE_BACKUP_PATH = os.path.join(os.path.expanduser('~'), 'Pictures', '_deduplicate_backup')
# Default image
EMPTY_IMAGE = html.Img(src=IMG_PATH, style=IMG_STYLE)