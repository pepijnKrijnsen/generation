######## UPDATE BLOG AUTOMAGICALLY ########
# 
# Generate a full HTML page from a template HTML plus a completed blog. It's
# a script, so I can probably keep it procedural from start to finish.
# Script takes the completed blog file as the only argument.
#
# STEPS:
# 1. Check if the provided argument is a valid file
# 2. Read the entire file into memory
# 3. Read the template.html file up to a placeholder point
# 4. Move cursor position to that point
# 5. Paste the contents of the blog at that location
#
import sys

def main():
    f = open("blog_date.html", "x")
    f.close()
