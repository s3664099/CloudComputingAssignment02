from googletrans import Translator

translate_client = Translator()

text = translate_client.translate("Das ist gut, das ist sehr gut mein Schweinhund",dest = 'sw')

lang = translate_client.detect("Das ist gut, das ist sehr gut mein Schweinhund")

print(text)
print(text.text)
print(lang.lang)

text.text = "yep, it worked"

print(text.text)

stuff = {
	"One": "1",
	"Two": "2",
	"Three": "3"
}

print(stuff["One"])
print(stuff["Two"])