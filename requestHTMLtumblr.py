from requests_html import HTML, HTMLSession
session = HTMLSession()

payload = {
	'determine_email': 'myaher@gmail.com',
	'user[email]': 'myaher@gmail.com',
	'user[password]': '123456789',
	'http_referer': 'https://www.tumblr.com/privacy/consent?redirect=https%3A%2F%2Fthefandometrics.tumblr.com%2F',}
	'form_key': 
}

p = session.post('https://www.tumblr.com/login', data=payload)
r = session.get('https://fandom.tumblr.com/tagged/week%20in%20review', timeout=3)
r.html.render()

consulta  = r.html.find('.caption ol li a')

print(p.html.find('.error'))