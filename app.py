import web
import Main

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting =  (Main.getTransalation(str(form.greet)))
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()