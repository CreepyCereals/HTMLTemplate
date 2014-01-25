import sublime, sublime_plugin, json

class HtmltemplateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.set_syntax_file('Packages/HTML/HTML.tmLanguage') # Sets the syntax to html
		template = json.loads(open('preferences.json').read())['template'] # Loads the template saved in 'preferences.json'
		self.view.insert(edit, 0, template) # Insertes the content of 'template'
