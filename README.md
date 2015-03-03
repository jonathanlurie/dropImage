# DropImage

## What does it do?
It sends a file to your dropbox account, in a subfolder system that is automatically arranged by year/month/day.  
When you drop the image, it returns a direct link to it as a *raw* data (meaning, you can embed it to a website).

## Why would I do that?
You might be interested to drop an image and get a link if you blog with a system using Dropbox instead of a database. Among them:

- [Scriptogr.am](http://scriptogr.am)
- [Calepin.co](http://calepin.co)
- [JustWriting](https://github.com/hjue/JustWriting)

The two first are free online services and the last must be hosted on you own server.  
On those three plateforms, your blog is hosted on your Dropbox (a subfolder of it), so you might not want to deal with uploading your images on a diferent service of server. In order to stay with Dropbox only, lets upload the images on your Dropbox!

> **« Yep, but I can do it manually! »**

You can. Or you can use DropImage and quickly upload + get a link + copy to clipboard a Markdown sentence for displaying your image in your blog post.

## What do I need?
- Python 2.7.x installed on your computer
- A Dropbox account
- To register your own Dropbox App [(here)](https://www.dropbox.com/developers/apps/create) 

The second will create a dedicated subfolder in your Dropbox, where you will put your images (and posts if you use *JustWriting*)

## How I set it up

The file **settings.ini** need to be updated according to your Dropbox App. Here is its original content:

```
[dropbox]
appkey = YOUR_APPKEY
appsecret = YOUR_APP_SECRET
accesstoken = LEAVE_BLANK_IT_WILL_BE_UPDATED_AUTOMATICALLY
```

You need to replace `YOUR_APPKEY` and `YOUR_APP_SECRET`. You can find those informations [on your App page](https://www.dropbox.com/developers/apps).

The last field is the `accesstoken`. It's automatically updated during the first launch.

## How do I use it?

After you've updated the setting file, you launch it with a double-click on **launcher.sh**.  
A terminal windows splashes:

```

--------------------------- DropImage -----------------------------------------

The access token is not valid anymore, generate another one

1. Go to: https://www.dropbox.com/1/oauth2/authorize?response_type=code&client_id=XXXXXXXXXXXXXXX
2. Click "Allow" (you might have to log in first)
3. Copy the authorization code.
Enter the authorization code here: 
```

Off course, it does not display `XXXXXXXXXXXX` , instead it should be you *APP_KEY*.  
So, you go to this URL you are asked to go, where a Dropbox page gives you a number. You *copy* it and *paste* it in your console.  
At this moment, another (even-longer) code is generated and written in the **setting.ini** file. THIS STEP WILL HAPPEN ONLY AT THE FIRST LAUNCH!

Then, the prompt asks you to write the local address of an image file. On most Unix systems you can drag-and-drop the file to the console and it will write its own address into it.

- Press `ENTER`
- It uploads the file to Dropbox
- It creates a sharable link.
- It generates a Mardown sentence that means *« I will display this image »*
- It copies it automatically into your clipboard
- Asks you for another file... and so on...

*Note:* the file will be updated to a subfolder of your App named `images` and then to 3 other levels of hierarchy: *year*, *month* and *day*. Just like that:

`Dropbox/MyAppName/images/2015/01/31/myPicture.jpg`

*Note 2:* this folder nesting stuff will not appear on the Dropbox sharing link.


## Will it work on my plateform?
DropImage was developped on MacOSX Yosemite, and uses only pure Python libraries, thus it should work on any Unix environement without changing anything.

Windows users should just replace the *launcher.sh* to its *.bat* equivalent. The rest should be ok.


## Dependancies
DropImage comes with its own dependancies (*Dropbox* and *Urllib3*), located in the *lib* folder.

## TODO

- Add a Markdown link to image
- Add auto copy Mardown to clipboard
