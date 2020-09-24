######## UPDATE BLOG AUTOMAGICALLY ########
# 
# Generate a full HTML page from a template HTML plus a completed blog. It's
# a script, so I can probably keep it procedural from start to finish.
#
# STEPS:
# 1. Check that there's exactly 1 file in ~/projects/blog/completed/
# 2. Read the entire file into memory
# 3. Read the template.html file into two variables: top and bottom
# 4. Construct a new blog file from template_top + blog + template_bottom
#
import os

def main():
    content_dir = "/home/pepijn/projects/blog/completed/"
    # check that there's exactly one file in content_dir
    if len(os.listdir(content_dir)) != 1:
        print("Please ensure " + content_dir + " contains exactly 1 file")
        quit()
    c = os.listdir(content_dir)
    content_name = c[0]
    content_file = content_dir + content_name
    # read that file into a variable and close it
    f = open(content_file)
    blog = f.read()
#    print(blog)
    f.close()
    # read both halves of template.html into separate variables
    template_file = "/home/pepijn/coding/projects/writesite/dev/lib/template.html"
    f = open(template_file)
    line = ""
    template_top = ""
    template_bottom = ""
    while "START content" not in line:
        line = f.readline()
        template_top += line
    template_top += "\n"
    template_bottom = f.read()  # read from last cursor position to end
    f.close()
    # generate a complete blog page
    new_blog = template_top + blog + template_bottom
    # create the new blog file
    blog_dir = "/home/pepijn/coding/projects/writesite/dev/blog/"
    f = open(blog_dir + content_name, "w")
    f.write(new_blog)
    f.close()

main()
