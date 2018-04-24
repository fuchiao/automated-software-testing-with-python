from blog import Blog

PROMPT='''
c) create a blog
l) list blogs
r) read a blogs
p) write a post
q) quit
plz choose an option
'''

POSTS_TEMPLATE='''
--- {} ---
{}
'''

blogs = dict()

def create_blog():
    blog_title = input('blog title?')
    if blog_title not in blogs:
        blog_author = input('blog author?')
        blogs[blog_title] = Blog(blog_title, blog_author)

def list_blogs():
    for _, blog in blogs.items():
        print('- {}'.format(repr(blog)))

def read_blog():
    blog_title = input('blog title?')
    if blog_title in blogs:
        for p in blogs[blog_title].posts:
            print(POSTS_TEMPLATE.format(p.title, p.content))

def write_post():
    blog_title = input('blog title?')

    if blog_title in blogs:
        post_title = input('post title?')
        post_content = input('post content?')
        blogs[blog_title].create_post(post_title, post_content)

def menu():
    opt = input(PROMPT)
    while True:
        if opt == 'c':
            create_blog()
        elif opt == 'l':
            list_blogs()
        elif opt == 'r':
            read_blog()
        elif opt == 'p':
            write_post()
        elif opt == 'q':
            break
        opt = input(PROMPT)

def main():
    menu()

if __name__=='__main__':
    main()
