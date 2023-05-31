template = open('template.txt')
pages = {
    'MainPage': {
        'title': 'Main Page',
        'body': 'This is my site'
    },
    'LoginPage':{
        'title': 'Login page',
        'body': 'Please login'
    }
}
page = 'LoginPage'
print(template.read().format(TITLE=pages[page]['title'],BODY=pages[page]['body']))
