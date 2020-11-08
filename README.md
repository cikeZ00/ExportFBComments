# ExportFBComments
 An app for exporting facebook page comments


### Setup
0) Install requirements from requirements.txt file using (pip install -r requirements.txt)

1) Run "fbot.py" once
2) Create a facebook application from here: https://developers.facebook.com
3) Setup application so it has Access to pages you are admin to
4) Generate the token with said permission and enter it into the config
5) Grab the page ID and post ID and enter it into the config using this format (PageID_PostID)
6) Run "fbot.py" file again, comments from defined post will be exported into "data.json"
