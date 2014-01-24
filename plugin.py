import sublime, sublime_plugin

class HtmltemplateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		template = '<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n\t\t<meta name="description" content="" />\n\t\t<title>Title</title>\n\t\t<link rel="icon" type="image/png" href="">\n\t\t<link rel="stylesheet" type="text/css" href="">\n\t\t<script type="text/javascript" src=""></script>\n\t</head>\n\t\t<body>\n\n\t\t</body>\n</html>'
		self.view.insert(edit, 0, template)
