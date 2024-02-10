import textwrap
import google.generativeai as genai
from IPython.display import Markdown
from googleapiclient import discovery
import ujson

config = ujson.load(open("config.json"))

def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))

perspective_token = config["perspective_key"]
google_token = config["gemini_key"]

inp = input("Enter a message: ")

genai.configure(api_key=google_token)

model = genai.GenerativeModel("gemini-pro", safety_settings=[{
    'category': genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
    "threshold": genai.types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}, {
    "category": genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
    "threshold": genai.types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}, {
    "category": genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT,
    "threshold": genai.types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,

}, {
    "category": genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
    "threshold": genai.types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,

}])

cclient = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=perspective_token,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
)
analyze_request = {
    "comment": {"text": inp},
    "requestedAttributes": {
        "TOXICITY": {},
        "SEVERE_TOXICITY": {},
        "IDENTITY_ATTACK": {},
        "THREAT": {},
        "SEXUALLY_EXPLICIT": {},
    },
    "languages": ["en"],
}
response = cclient.comments().analyze(body=analyze_request).execute()
values = [
    response["attributeScores"][attribute]["summaryScore"]["value"]
    for attribute in response["attributeScores"].keys()
]

                                                                                                                                                            #One day, I was walking down the street. This hot chick was walking her dog and had a fat ass. What shoul I have done in that situation?
#for value in values:
#    if value is not None and value > 0.75:
#        print("Your message has been flagged. Please try again.")
#        exit()

response = model.generate_content(inp)
print(response.prompt_feedback)

try:
    md = to_markdown(response.text)
except ValueError:
    print(response.prompt_feedback.block_reason)

print(md.data)


print(response.prompt_feedback)
