#!usr/bin/python
#-*- coding: utf-8 -*-
#Facebook : suhandi ID

import os
import time
import sys

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan


mess = """\033[96m==========================================================\033[0m
           \033[33mHYPERTEXT MARKUP LANGUAGE BULDING TOOLS\033[0m
\033[96m==========================================================\033[0m
                  \033[36mTools Design By suhandi ID\033[0m
       \033[34mcreated your HTML file in my tools so easy steps\033[0m
                \033[31mCIREBON PROGRAMMER CREATIVITY\033[0m
\033[96m==========================================================\033[0m"""
os.system("clear")
print GG+"TOOLS INI DIRANCANG LANGSUNG OLEH [suhandi ID]"
print GG+"Jika Ada kesalahan Kinerja atau hasil silakan hubungi Admin!"
time.sleep(8)
os.system("clear")
print mess
print wd+" "
title = raw_input("subs title ")
print wd+" "
heading = raw_input("nickname: ")
print wd+" "
imagelink = raw_input("link images (center): ")
print wd+" "
messagein = raw_input("Message loading : " )
print wd+" "
message = raw_input("message : ")
print wd+" "
message2 = raw_input("contact you (example : nitfound@yahoo.com : " )
print wd+" "

print wd+" "
youtubeid = raw_input("youtube code (MUSIC): ")

#Open the index
fo = open("scriptku.html","w")

messagescript1 = """<DOCTIPEhtml>
<html>
<head>
<title>"""

messagescript2 = title

messagescript3 = """</title>
<link rel="SHORTCUT ICON" href="https://i68.tinypic.com/65si9x.jpg" type="image/x-icon"/>
<link href='https://fonts.googleapis.com/css?family=Nosifer' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Iceland' rel='stylesheet' type='text/css'>
<link href="https://fonts.googleapis.com/css?family=Sarpanch:700" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=play" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="https://csshake.surge.sh/csshake.min.css">
<link rel="stylesheet" href="css/style.css">

<script>
alert(" """
messagescript4 = messagein

messagescript5 = """ ");
</script>
</head>
<body>
<center>
<h1>"""

messagescript6 = heading

messagescript7 = """</h1>
<img src=" """

messagescript8 = imagelink

messagescript9 = """ " width=450px height=340px>
<h2>"""

messagescript10 = message

messagescript11 = """ </h2>"""

messagescript12 = """<h3> """

messagescript13 = message2

messagescript14 = """</h3>
<div class="clouds">
</div>
<style>
* {
    margin: 0;
    padding: 0;
}

body{
    background-color: #000;
}

header {
    background-color:rgba(33, 33, 33, 0.9);
    color:#ffffff;
    display:block;
    font: 14px/1.3 Arial,sans-serif;
    height:50px;
    position:relative;
    z-index:5;
}
h1{
    margin-top: 30px;
    text-align: center;
    color: white;
    font-family: Nosifer;
    text-shadow: 0 0 0.5em red, 0 0 0.5em red;
}
h2{
    margin-top: 30px;
    text-align: center;
    color: white;
    font-family: Nosifer;
    text-shadow: 0 0 0.5em red, 0 0 0.5em red;
}

h3{
    margin-top: 30px;
    text-align: center;
    color: white;
    font-family: Nosifer;
    text-shadow: 0 0 0.5em red, 0 0 0.5em blue;
}
.we-are {
    color: red;
    font-size: 20px;
    text-shadow: #000 2px 2px 2px;
    letter-spacing: 2px;
}

.message {
    color: white;
    -webkit-animation: fadeIn 1s ease-in;
    animation: fadeIn 1s ease-in;
}

.cn {
    color: white;
    font-size: 14px;
    text-shadow: #000 2px 2px 2px;
    letter-spacing: 2px;
    -webkit-animation: fadeIn 3s ease-in;
    animation: fadeIn 1s ease-in;
}

-webkit-@keyframes we-are {
    from {scale: 1.1;}
    to {scale: 0;}
}

@keyframes we-are {
    from {scale: 1.1;}
    to {scale: 0;}
}

-webkit-@keyframes fadeIn {
   0% {opacity: 0;}
   100% {opacity: 1;}
} 

@keyframes fadeIn {
   0% {opacity: 0;}
   100% {opacity: 1;}
} 

@keyframes move-twink-back {
    from {background-position:0 0;}
    to {background-position:-10000px 5000px;}
}
@-webkit-keyframes move-twink-back {
    from {background-position:0 0;}
    to {background-position:-10000px 5000px;}
}
@-moz-keyframes move-twink-back {
    from {background-position:0 0;}
    to {background-position:-10000px 5000px;}
}
@-ms-keyframes move-twink-back {
    from {background-position:0 0;}
    to {background-position:-10000px 5000px;}
}

@keyframes move-clouds-back {
    from {background-position:0 0;}
    to {background-position:10000px 0;}
}
@-webkit-keyframes move-clouds-back {
    from {background-position:0 0;}
    to {background-position:10000px 0;}
}
@-moz-keyframes move-clouds-back {
    from {background-position:0 0;}
    to {background-position:10000px 0;}
}
@-ms-keyframes move-clouds-back {
    from {background-position: 0;}
    to {background-position:10000px 0;}
}

.stars, .twinkling, .clouds {
  position:absolute;
  top:0;
  left:0;
  right:0;
  bottom:0;
  width:100%;
  height:100%;
  display:block;
}

.stars {
  background:#000 url(http://www.script-tutorials.com/demos/360/images/stars.png) repeat top center;
  z-index:0;
}

.twinkling{
  background:transparent url(http://www.script-tutorials.com/demos/360/images/twinkling.png) repeat top center;
  z-index:1;

  -moz-animation:move-twink-back 200s linear infinite;
  -ms-animation:move-twink-back 200s linear infinite;
  -o-animation:move-twink-back 200s linear infinite;
  -webkit-animation:move-twink-back 200s linear infinite;
  animation:move-twink-back 200s linear infinite;
}

.clouds{
    background:transparent url(http://www.script-tutorials.com/demos/360/images/clouds3.png) repeat top center;
    background-repeat: no-repeat;
    z-index:3;

  -moz-animation:move-clouds-back 200s linear infinite;
  -ms-animation:move-clouds-back 200s linear infinite;
  -o-animation:move-clouds-back 200s linear infinite;
  -webkit-animation:move-clouds-back 200s linear infinite;
  animation:move-clouds-back 200s linear infinite;
}

.container {
  height: 100%;
  width: 100%;
  justify-content: center;
  align-items: center;
  display: flex;
}
.text {
  font-weight: 100;
  font-size: 28px;
  color: #FAFAFA;
  font-family: Iceland;
  text-shadow: 0 0 0.5em cyan, 0 0 0.5em cyan;
  
}
.dud {
  color: #757575;
}

.animation-container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
}

.animation-container span {
  color: whitesmoke;
  display: block;
  font-size: 18px;
  font-family: 'Helvetica';
  text-shadow: 0 0 1px white;
  position: absolute;
  user-select: none;
  pointer-events: none;
  cursor: default;
  z-index: 1;
  opacity: 0;
  will-change: transform, opacity;
  animation-timing-function: ease-out;
  animation-name: move;
}

@keyframes move {
  0% {
    opacity: 0;
    transform: translateY(100vh);
  }
  25% {
    opacity: 1;
  }
  50% {
    opacity: 1;
  }
  75% {
    opacity: 0;
  }
  100% {
    opacity: 0;
    transform: none;
  }
}
.buzz_wrapper{
  position:relative;
  width:100%;
  margin:180px auto;
  background-attachment: fixed;
        background-image: url(http://i.imgur.com/9QpJPlG.jpg);
    background-position: 0 0; 
        background-repeat: no-repeat ;  
        background-size:cover;
        overflow : hidden;
  overflow:hidden;
  padding:100px;
}
.scanline{
  width:100%;
  display:block;
  background:#000;
  height:4px;
  position:relative;
  z-index:3;
  margin-bottom:5px;
  opacity:0.1;
}
.buzz_wrapper span{
  position:absolute;
  -webkit-filter: blur(1px);
  font-size:30px;
  font-family:'Courier new', fixed;
  font-weight:bold;
}
.buzz_wrapper span:nth-child(1){
  color:red;
  margin-left:-2px;
  -webkit-filter: blur(2px);
}
.buzz_wrapper span:nth-child(2){
  color:green;
  margin-left:2px;
  -webkit-filter: blur(2px);
}
.buzz_wrapper span:nth-child(3){
  color:blue;
  position:20px 0;
  -webkit-filter: blur(1px);
}
.buzz_wrapper span:nth-child(4){
  color:#fff;
  -webkit-filter: blur(1px);
  text-shadow:0 0 50px rgba(255,255,255,0.4);
}
.buzz_wrapper span:nth-child(5){
  color:rgba(255,255,255,0.4);
  -webkit-filter: blur(15px);
}

.buzz_wrapper span{
  -webkit-animation: blur 30ms infinite, jerk 50ms infinite;
}

@-webkit-keyframes blur {
  0%   { -webkit-filter: blur(1px); opacity:0.8;}
  50% { -webkit-filter: blur(1px); opacity:1; }
  100%{ -webkit-filter: blur(1px); opacity:0.8; }
}
@-webkit-keyframes jerk {
  50% { left:1px; }
  51% { left:0; }
}
@-webkit-keyframes jerkup {
  50% { top:1px; }
  51% { top:0; }
}

.buzz_wrapper span:nth-child(3){
  -webkit-animation: jerkblue 1s infinite;
}
@-webkit-keyframes jerkblue {
  0% { left:0; }
  30% { left:0; }
  31% { left:10px; }
  32% { left:0; }
  98% { left:0; }
  100% { left:10px; }
}
.buzz_wrapper span:nth-child(2){
  -webkit-animation: jerkgreen 1s infinite;
}
@-webkit-keyframes jerkgreen {
  0% { left:0; }
  30% { left:0; }
  31% { left:-10px; }
  32% { left:0; }
  98% { left:0; }
  100% { left:-10px; }
}

.buzz_wrapper .text{
  -webkit-animation: jerkwhole 5s infinite;
  position:relative;
}
@-webkit-keyframes jerkwhole {
  30% {  }
  40% { opacity:1; top:0; left:0;  -webkit-transform:scale(1,1);  -webkit-transform:skew(0,0);}
  41% { opacity:0.8; top:0px; left:-100px; -webkit-transform:scale(1,1.2);  -webkit-transform:skew(50deg,0);}
  42% { opacity:0.8; top:0px; left:100px; -webkit-transform:scale(1,1.2);  -webkit-transform:skew(-80deg,0);}
  43% { opacity:1; top:0; left:0; -webkit-transform:scale(1,1);  -webkit-transform:skew(0,0);}
  65% { }
}
</style>
  
<iframe width="0" height="0" src="http://www.youtube.com/v/"""
messagescript15 = youtubeid

messagescript16 = """&autoplay=1" frameborder="0"></iframe>"""


fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)
fo.write(messagescript14)
fo.write(messagescript15)


print GG+ "Successfully !!"

os.system("mv scriptku.html /storage/emulated/0")
print ""


print CC+ "Your File In Storage Emulated Check right now![scriptku.html] "

os.system("exit")
