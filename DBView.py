import sqlite3,webbrowser,os
from rich.console import Console;
from flask import *
console=Console()
def header():
  os.system("cls" if os.name=='nt' else "clear");console.print(""" 
 ██████╗███╗   ███╗███████╗
██╔════╝████╗ ████║██╔════╝
██║     ██╔████╔██║███████╗
██║     ██║╚██╔╝██║╚════██║
╚██████╗██║ ╚═╝ ██║███████║
 ╚═════╝╚═╝     ╚═╝╚══════
 
  By @TweakPY - @vv1ck
 """,style='bold dark_magenta',justify='left')
app=Flask(__name__)
@app.route('/intro')
def intro():
    header();return '''<html lang="en"><head><meta charset="UTF-8"/><title>Welcome</title><link rel="shortcut icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAADzUlEQVR4nO2dy2oUQRSGf1xMCxE1IKgZL6/gG+hSxVeILg3RRFQ07rw8TQQv2Ri3bozJIiouvEBATbxsHEHHhbMqKakBbbqruqq7Lun+PzgwpOvknP5PdVX3nMkEIIQQQgghhBBCCCGkOpMAZgAsAtgAMAIgWmojdY6L6pzluUdjJ4DbAIYJCCMimTz3WwCy0OIfBfAqAQFEIvYSwJGQ4m8lcNIiMdsKUQR5qXHmo7QIL3wvR3cSmGkicbvpS/xJw4Yr7xCuA5hStlByR1R1nCgYH5sq+f4EsNdH8BlD5WVieRZqjBOa8bHR5SvtvI+gdw1BDxb4HKgxTmjGx0aXr1DPCY2zYQhatERM1RgnNONjo8tXKK0a57fDEnSjxjiR8BKky1corRrHtPuPlFhVNuEq40TB+NhUyXdsjWMKSAMLIBKaCLwCwAJEn4WCV0B8IQSXoPhiiDbvAV1HsABxYQEiwwJEhgWIDAsQmaQLsAPAMQCXACwB+AbgM4CTGp8MwDyAVQC/lMnXFwH0KuRZx98l32QLcAbAlxKfDyU+ffURD13TW46BB3+XfF10ccY20CfLB5XMIN7YnpfM5Lr+tvm66uKMbaBNyxOar/iEKe2CB3/bfF11ccY20GkAHwF8VeupyW8td/wRgEPKlnPHnnnwt83XVRdn6gYy+Q1zx6VwYw4XfPSjaX/bfFtXABH5uOt4FkDBAhiIPcMFrwAWoBbchFu+B6zmji+ruxdpj3PHVjz42+bblC7JFGBOEyNvsx78bfNtSpdkCpCp92pM4q1r3oqo42+bb1O6VKZuoH//rEk+9hfRN4i4bviIYl1/23y3VQFOqZPaNLy921NvHa+op9uhej1bcebW9bfNd9sUoK0IFiAuLEBkWIDIJF+A0D3ajD3heD3aPnvC8Xq0GXvCcXu084HjJb8HhO7RrgWO56qLM7aBQvdoh4HjJV8A0zhhmXDd39d0vLJxLABYgCgzUvAKiCuIYAH+h5tww9huNqF7tKuB47nq4oxtoNA92rnA8Vx1ccY2UOgebcaecPwebZ894fg92h57wt1ChNoDyr6yche6y+4STX74CPauJNhxdJcTJZq89RHsQUkw+fOuslSiyT0fwc5p1rur6B7XNHpM+wgov473uyboQ3VJTqC9TKhzLJv50gYA9sSoOg1/NbgMj2SqnUexUajBU8tnG+fvTX7PIiAvvtRkPwKxD8ATFgFj8VfUxAxKT939DDq8JA0AXAmx7OiQO/5ZAPcBvGn5f1UaAnitznXa590OIYQQQgghhBBCCEHr+AMLPCCVpcrSPAAAAABJRU5ErkJggg=="><style id="INLINE_PEN_STYLESHEET_ID">html,body {margin: 0;padding: 0;width: 100%;height: 100%;}#container {display: flex;flex-direction: column;justify-content: center;align-items: center;width: 100%;height: 100%;background-color: #000000;overflow: hidden;}#container netflixintro {display: block;position: relative;width: 300px;height: 300px;overflow: hidden;animation-name: zoom-in;animation-delay: 0.5s;animation-duration: 3.5s;animation-timing-function: ease-in;animation-fill-mode: forwards;background-size: 4000px;background-position: -1950px 0;}#container netflixintro::before {content: "";position: absolute;display: block;background-color: #000000;width: 150%;height: 30%;left: -25%;bottom: -27%;border-radius: 50%;z-index: 5;transform-origin: left center;background-size: 4000px;background-position: -1950px 0;}#container netflixintro[letter=N] {transform-origin: 30% center;}#container netflixintro[letter=N] .helper-1 {width: 19.5%;height: 100%;background-color: rgba(228, 9, 19, 0.5);left: 22.4%;top: 0;transform: rotate(180deg);animation-name: fading-lumieres-box;animation-duration: 2s;animation-delay: 0.6s;animation-fill-mode: forwards;}
#container netflixintro[letter=N] .helper-1 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2.5s;
  animation-fill-mode: forwards;
  animation-delay: 1.2s;
}
#container netflixintro[letter=N] .helper-1 .effect-brush [class*=fur-] {
  bottom: 0;
  height: 40%;
}
#container netflixintro[letter=N] .helper-3 {
  width: 19%;
  height: 150%;
  left: 40.5%;
  top: -25%;
  transform: rotate(-19.5deg);
  box-shadow: 0px 0px 35px -12px rgba(0, 0, 0, 0.4);
  overflow: hidden;
}
#container netflixintro[letter=N] .helper-3 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 0.8s;
}
#container netflixintro[letter=N] .helper-2 {
  width: 19.5%;
  height: 100%;
  left: 57.8%;
  top: 0;
  transform: rotate(180deg);
  overflow: hidden;
}
#container netflixintro[letter=N] .helper-2 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 0.5s;
}
#container netflixintro[letter=E] {
  transform-origin: 30% center;
}
#container netflixintro[letter=E] .helper-1 {
  width: 19.5%;
  height: 100%;
  background-color: rgba(228, 9, 19, 0.5);
  left: 22%;
  top: 0;
  transform: rotate(180deg);
  animation-name: fading-lumieres-box;
  animation-duration: 2s;
  animation-delay: 0.6s;
  animation-fill-mode: forwards;
}
#container netflixintro[letter=E] .helper-1 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2.5s;
  animation-fill-mode: forwards;
  animation-delay: 1.2s;
}
#container netflixintro[letter=E] .helper-1 .effect-brush [class*=fur-] {
  bottom: 0;
  height: 40%;
}
#container netflixintro[letter=E] .helper-2 {
  width: 17.5%;
  height: 50%;
  left: 38%;
  top: -49px;
  transform: rotate(270deg);
  overflow: hidden;
}
#container netflixintro[letter=E] .helper-2 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 0.8s;
}
#container netflixintro[letter=E] .helper-3 {
  width: 17%;
  height: 39%;
  left: 33%;
  top: 29%;
  transform: rotate(-90deg);
  box-shadow: 0px 0px 35px -12px rgba(0, 0, 0, 0.4);
  overflow: hidden;
  animation-name: fading-out;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 1s;
}
#container netflixintro[letter=E] .helper-3 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 0.6s;
}
#container netflixintro[letter=E] .helper-4 {
  width: 17.5%;
  height: 50%;
  left: 38%;
  top: 196px;
  transform: rotate(270deg);
  overflow: hidden;
}
#container netflixintro[letter=E] .helper-4 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 0.4s;
  animation-delay: 0.5s;
}
#container netflixintro[letter=T] {
  transform-origin: center center;
}
#container netflixintro[letter=T] .helper-1 {
  width: 19.5%;
  height: 100%;
  background-color: rgba(228, 9, 19, 0.5);
  left: 38%;
  top: 0;
  transform: rotate(180deg);
  animation-name: fading-lumieres-box;
  animation-duration: 2s;
  animation-delay: 0.6s;
  animation-fill-mode: forwards;
}
#container netflixintro[letter=T] .helper-1 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2.5s;
  animation-fill-mode: forwards;
  animation-delay: 1s;
}
#container netflixintro[letter=T] .helper-1 .effect-brush [class*=fur-] {
  bottom: 0;
  height: 40%;
}
#container netflixintro[letter=T] .helper-2 {
  width: 17.5%;
  height: 54%;
  left: 39%;
  top: -55px;
  transform: rotate(270deg);
  overflow: hidden;
}
#container netflixintro[letter=T] .helper-2 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 0.5s;
}
#container netflixintro[letter=F] {
  transform-origin: 30% center;
}
#container netflixintro[letter=F] .helper-1 {
  width: 19.5%;
  height: 100%;
  background-color: rgba(228, 9, 19, 0.5);
  left: 22%;
  top: 0;
  transform: rotate(180deg);
  animation-name: fading-lumieres-box;
  animation-duration: 2s;
  animation-delay: 0.6s;
  animation-fill-mode: forwards;
}
#container netflixintro[letter=F] .helper-1 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2.5s;
  animation-fill-mode: forwards;
  animation-delay: 1.2s;
}
#container netflixintro[letter=F] .helper-1 .effect-brush [class*=fur-] {
  bottom: 0;
  height: 40%;
}
#container netflixintro[letter=F] .helper-2 {
  width: 17.5%;
  height: 50%;
  left: 38%;
  top: -49px;
  transform: rotate(270deg);
  overflow: hidden;
}
#container netflixintro[letter=F] .helper-2 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 0.7s;
}
#container netflixintro[letter=F] .helper-3 {
  width: 17%;
  height: 39%;
  left: 33%;
  top: 29%;
  transform: rotate(-90deg);
  box-shadow: 0px 0px 35px -12px rgba(0, 0, 0, 0.4);
  overflow: hidden;
  animation-name: fading-out;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 1s;
}
#container netflixintro[letter=F] .helper-3 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 0.5s;
}
#container netflixintro[letter=L] {
  transform-origin: 30% center;
}
#container netflixintro[letter=L] .helper-1 {
  width: 19.5%;
  height: 100%;
  background-color: rgba(228, 9, 19, 0.5);
  left: 22%;
  top: 0;
  transform: rotate(180deg);
  animation-name: fading-lumieres-box;
  animation-duration: 2s;
  animation-delay: 0.6s;
  animation-fill-mode: forwards;
}
#container netflixintro[letter=L] .helper-1 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2.5s;
  animation-fill-mode: forwards;
  animation-delay: 0.8s;
}
#container netflixintro[letter=L] .helper-1 .effect-brush [class*=fur-] {
  bottom: 0;
  height: 40%;
}
#container netflixintro[letter=L] .helper-2 {
  width: 17.5%;
  height: 50%;
  left: 38%;
  top: 196px;
  transform: rotate(270deg);
  overflow: hidden;
}
#container netflixintro[letter=L] .helper-2 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 0.4s;
}
#container netflixintro[letter=I] {
  transform-origin: center center;
}
#container netflixintro[letter=I] .helper-1 {
  width: 19.5%;
  height: 100%;
  background-color: rgba(228, 9, 19, 0.5);
  left: 38%;
  top: 0;
  transform: rotate(180deg);
  animation-name: fading-lumieres-box;
  animation-duration: 2s;
  animation-delay: 0.6s;
  animation-fill-mode: forwards;
}
#container netflixintro[letter=I] .helper-1 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2.5s;
  animation-fill-mode: forwards;
  animation-delay: 1s;
}
#container netflixintro[letter=I] .helper-1 .effect-brush [class*=fur-] {
  bottom: 0;
  height: 40%;
}
#container netflixintro[letter=X] {
  transform-origin: center center;
}
#container netflixintro[letter=X] .helper-1 {
  width: 19%;
  height: 150%;
  left: 40.5%;
  top: -25%;
  transform: rotate(-19.5deg);
  animation-name: fading-lumieres-box;
  animation-duration: 2s;
  animation-delay: 0.6s;
  animation-fill-mode: forwards;
}
#container netflixintro[letter=X] .helper-1 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2.5s;
  animation-fill-mode: forwards;
  animation-delay: 1.2s;
}
#container netflixintro[letter=X] .helper-1 .effect-brush [class*=fur-] {
  bottom: 0;
  height: 40%;
}
#container netflixintro[letter=X] .helper-2 {
  width: 19%;
  height: 150%;
  left: 40.5%;
  top: -25%;
  transform: rotate(19.5deg);
  overflow: hidden;
}
#container netflixintro[letter=X] .helper-2 .effect-brush {
  animation-name: brush-moving;
  animation-duration: 2s;
  animation-fill-mode: forwards;
  animation-delay: 0.5s;
}
#container netflixintro [class*=helper-] {
  position: absolute;
}
#container netflixintro [class*=helper-] .effect-brush {
  position: absolute;
  width: 100%;
  height: 300%;
  top: 0;
  overflow: hidden;
}
#container netflixintro [class*=helper-] .effect-brush::before {
  display: block;
  content: "";
  position: absolute;
  background-color: #e40913;
  width: 100%;
  height: 70%;
  box-shadow: 0px 0px 29px 24px #e40913;
}
#container netflixintro [class*=helper-] .effect-brush [class*=fur-] {
  display: block;
  position: absolute;
  bottom: 10%;
  height: 30%;
}
#container netflixintro [class*=helper-] .effect-brush .fur-1 {
  left: 0%;
  width: 3.8%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 15%, rgba(0, 0, 0, 0) 81%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-2 {
  left: 3.8%;
  width: 2.8%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 10%, rgba(0, 0, 0, 0) 62%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-3 {
  left: 6.6%;
  width: 4.8%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 37%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-4 {
  left: 11.4%;
  width: 4%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 23%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-5 {
  left: 15.4%;
  width: 4%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 15%, rgba(0, 0, 0, 0) 86%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-6 {
  left: 19.4%;
  width: 2.5%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 27%, rgba(0, 0, 0, 0) 89%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-7 {
  left: 21.9%;
  width: 4%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 20%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-8 {
  left: 25.9%;
  width: 2%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 30%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-9 {
  left: 27.9%;
  width: 4%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 35%, rgba(0, 0, 0, 0) 95%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-10 {
  left: 31.9%;
  width: 3.5%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 39%, rgba(0, 0, 0, 0) 95%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-11 {
  left: 35.4%;
  width: 2%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 34%, rgba(0, 0, 0, 0) 95%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-12 {
  left: 37.4%;
  width: 2.6%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 22%, rgba(0, 0, 0, 0) 95%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-13 {
  left: 40%;
  width: 6%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 47%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-14 {
  left: 46%;
  width: 2%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 36%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-15 {
  left: 48%;
  width: 5.5%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 29%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-16 {
  left: 53.5%;
  width: 3%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 39%, rgba(0, 0, 0, 0) 95%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-17 {
  left: 56.5%;
  width: 4.1%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 45%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-18 {
  left: 60.6%;
  width: 2.4%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 34%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-19 {
  left: 63%;
  width: 4%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 47%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-20 {
  left: 67%;
  width: 1.5%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 27%, rgba(0, 0, 0, 0) 95%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-21 {
  left: 68.5%;
  width: 2.8%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 37%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-22 {
  left: 71.3%;
  width: 2.3%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 9%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-23 {
  left: 73.6%;
  width: 2.2%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 28%, rgba(0, 0, 0, 0) 92%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-24 {
  left: 75.8%;
  width: 1%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 37%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-25 {
  left: 76.8%;
  width: 2.1%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 28%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-26 {
  left: 78.9%;
  width: 4.1%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 34%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-27 {
  left: 83%;
  width: 2.5%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 21%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-28 {
  left: 85.5%;
  width: 4.5%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 39%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-29 {
  left: 90%;
  width: 2.8%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 30%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-30 {
  left: 92.8%;
  width: 3.5%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 19%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-brush .fur-31 {
  left: 96.3%;
  width: 3.7%;
  background: linear-gradient(to bottom, #e40913 0%, #e40913 37%, rgba(0, 0, 0, 0) 100%);
}
#container netflixintro [class*=helper-] .effect-lumieres {
  position: absolute;
  width: 100%;
  height: 100%;
  opacity: 0;
  animation-name: showing-lumieres;
  animation-duration: 2s;
  animation-delay: 1.6s;
  animation-fill-mode: forwards;
}
#container netflixintro [class*=helper-] .effect-lumieres [class*=lamp-] {
  position: absolute;
  display: block;
  height: 100%;
  box-shadow: 0px 0px 10px 0px rgba(228, 9, 19, 0.75);
  background: var(--color);
}
#container netflixintro [class*=helper-] .effect-lumieres [class*=lamp-]::before {
  position: absolute;
  content: " ";
  display: block;
  width: 100%;
  height: 100%;
  background: var(--color);
  box-shadow: 0px 0px 10px 0px rgba(228, 9, 19, 0.75);
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-1 {
  --color: #ff0100;
  z: 6;
  left: 0.7%;
  width: 1%;
  animation-delay: 1.88s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-1::before {
  left: 154%;
  animation-delay: 0.9s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-2 {
  --color: #ffde01;
  left: 2.2%;
  width: 1.4%;
  animation-delay: 0.67s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-2::before {
  left: 45%;
  animation-delay: 1.66s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-3 {
  --color: #ff00cc;
  left: 5.8%;
  width: 2.1%;
  animation-delay: 1.83s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-3::before {
  left: 148%;
  animation-delay: 0.97s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-4 {
  --color: #04fd8f;
  left: 10.1%;
  width: 2%;
  animation-delay: 1.69s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-4::before {
  left: 48%;
  animation-delay: 1.68s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-5 {
  --color: #ff0100;
  left: 12.9%;
  width: 1.4%;
  animation-delay: 0.38s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-5::before {
  left: 62%;
  animation-delay: 0.8s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-6 {
  --color: #ff9600;
  left: 15.3%;
  width: 2.8%;
  animation-delay: 0.49s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-6::before {
  left: 17%;
  animation-delay: 0.2s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-7 {
  --color: #0084ff;
  left: 21.2%;
  width: 2.5%;
  animation-delay: 1.97s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-7::before {
  left: 144%;
  animation-delay: 0.43s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-8 {
  --color: #f84006;
  left: 25%;
  width: 2.5%;
  animation-delay: 0.24s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-8::before {
  left: 50%;
  animation-delay: 0.6s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-9 {
  --color: #ffc601;
  left: 30.5%;
  width: 3%;
  animation-delay: 1.63s;
}
#container netflixintro [class*=helper-] .effect-lumieres .lamp-9::before {
  left: 140%;
  animation-delay: 0.66s;
}#container netflixintro [class*=helper-] .effect-lumieres .lamp-10 {--color: #ff4800;left: 36.3%;width: 3%;animation-delay: 1.08s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-10::before {left: 166%;animation-delay: 0.09s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-11 {--color: #fd0100;left: 41%;width: 2.2%;animation-delay: 0.31s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-11::before {left: 149%;animation-delay: 0.67s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-12 {--color: #01ffff;left: 44.2%;width: 2.6%;animation-delay: 1.21s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-12::before {left: 6%;animation-delay: 1.82s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-13 {--color: #ffc601;left: 51.7%;width: 0.5%;animation-delay: 0.66s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-13::before {left: 85%;animation-delay: 1.27s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-14 {--color: #ffc601;left: 52.1%;width: 1.8%;animation-delay: 0.44s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-14::before {left: 103%;animation-delay: 0.47s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-15 {--color: #0078fe;left: 53.8%;width: 2.3%;animation-delay: 0.6s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-15::before {left: 12%;animation-delay: 1.93s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-16 {--color: #0080ff;left: 57.2%;width: 2%;animation-delay: 0.98s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-16::before {left: 130%;animation-delay: 0.65s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-17 {--color: #ffae01;left: 62.3%;width: 2.9%;animation-delay: 0.98s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-17::before {left: 122%;animation-delay: 0.22s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-18 {--color: #ff00bf;left: 65.8%;width: 1.7%;animation-delay: 1.55s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-18::before {left: 38%;animation-delay: 0.8s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-19 {--color: #a601f4;left: 72.8%;width: 0.8%;animation-delay: 0.97s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-19::before {left: 123%;animation-delay: 1.87s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-20 {--color: #f30b34;left: 74.3%;width: 2%;animation-delay: 1.86s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-20::before {left: 71%;animation-delay: 0.77s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-21 {--color: #ff00bf;left: 79.8%;width: 2%;animation-delay: 0.58s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-21::before {left: 99%;animation-delay: 1.26s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-22 {--color: #04fd8f;left: 78.2%;width: 2%;animation-delay: 1.15s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-22::before {left: 68%;animation-delay: 1.48s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-23 {--color: #01ffff;left: 78.5%;width: 2%;animation-delay: 0.39s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-23::before {left: 32%;animation-delay: 0.19s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-24 {--color: #a201ff;left: 85.3%;width: 1.1%;animation-delay: 1.39s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-24::before {left: 187%;animation-delay: 0.11s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-25 {--color: #ec0014;left: 86.9%;width: 1.1%;animation-delay: 0.85s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-25::before {left: 148%;animation-delay: 0.85s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-26 {--color: #0078fe;left: 88.8%;width: 2%;animation-delay: 1.85s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-26::before {left: 184%;animation-delay: 0.99s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-27 {--color: #ff0036;left: 92.4%;width: 2.4%;animation-delay: 1s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-27::before {left: 123%;animation-delay: 0.3s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-28 {--color: #06f98c;left: 96.2%;width: 2.1%;animation-delay: 0.51s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-28::before {left: 192%;animation-delay: 0.26s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-1,#container netflixintro [class*=helper-] .effect-lumieres .lamp-3,#container netflixintro [class*=helper-] .effect-lumieres .lamp-5,#container netflixintro [class*=helper-] .effect-lumieres .lamp-7,#container netflixintro [class*=helper-] .effect-lumieres .lamp-9,#container netflixintro [class*=helper-] .effect-lumieres .lamp-11,#container netflixintro [class*=helper-] .effect-lumieres .lamp-13,#container netflixintro [class*=helper-] .effect-lumieres .lamp-15,#container netflixintro [class*=helper-] .effect-lumieres .lamp-17,#container netflixintro [class*=helper-] .effect-lumieres .lamp-19,#container netflixintro [class*=helper-] .effect-lumieres .lamp-21,#container netflixintro [class*=helper-] .effect-lumieres .lamp-23,#container netflixintro [class*=helper-] .effect-lumieres .lamp-25,#container netflixintro [class*=helper-] .effect-lumieres .lamp-27 {animation-name: lumieres-moving-left;animation-duration: 5s;animation-fill-mode: forwards;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-1::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-3::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-5::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-7::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-9::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-11::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-13::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-15::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-17::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-19::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-21::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-23::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-25::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-27::before {animation-name: lumieres-moving-left;animation-duration: 5.5s;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-2,#container netflixintro [class*=helper-] .effect-lumieres .lamp-4,#container netflixintro [class*=helper-] .effect-lumieres .lamp-6,#container netflixintro [class*=helper-] .effect-lumieres .lamp-8,#container netflixintro [class*=helper-] .effect-lumieres .lamp-10,#container netflixintro [class*=helper-] .effect-lumieres .lamp-12,#container netflixintro [class*=helper-] .effect-lumieres .lamp-14,#container netflixintro [class*=helper-] .effect-lumieres .lamp-16,#container netflixintro [class*=helper-] .effect-lumieres .lamp-18,#container netflixintro [class*=helper-] .effect-lumieres .lamp-20,#container netflixintro [class*=helper-] .effect-lumieres .lamp-22,#container netflixintro [class*=helper-] .effect-lumieres .lamp-24,#container netflixintro [class*=helper-] .effect-lumieres .lamp-26,#container netflixintro [class*=helper-] .effect-lumieres .lamp-28 {animation-name: lumieres-moving-right;animation-duration: 5s;animation-fill-mode: forwards;}#container netflixintro [class*=helper-] .effect-lumieres .lamp-2::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-4::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-6::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-8::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-10::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-12::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-14::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-16::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-18::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-20::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-22::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-24::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-26::before,#container netflixintro [class*=helper-] .effect-lumieres .lamp-28::before {animation-name: lumieres-moving-right;animation-duration: 5.5s;}@keyframes brush-moving {0% {transform: translateY(0);}100% {transform: translateY(-100%);}}@keyframes fading-out {0% {opacity: 1;}100% {opacity: 0;}}@keyframes lumieres-moving-right {0% {transform: translate(0);}40% {transform: translate(-10px) scaleX(1);}50% {transform: translate(-60px);}100% {transform: translate(-120px) scaleX(3);}}@keyframes lumieres-moving-left {0% {transform: translate(0);}40% {transform: translate(10px) scaleX(1);}50% {transform: translate(60px);}100% {transform: translate(120px) scaleX(3);}}@keyframes zoom-in {0% {transform: scale(1);}100% {transform: scale(15);}}@keyframes showing-lumieres {0% {opacity: 0;}100% {opacity: 1;}}@keyframes fading-lumieres-box {0% {background-color: rgba(228, 9, 19, 0.5);}100% {background-color: rgba(228, 9, 19, 0);}}</style></head><body><div id="container"><netflixintro letter="T"><div class="helper-1"><div class="effect-brush"><span class="fur-31"></span><span class="fur-30"></span><span class="fur-29"></span><span class="fur-28"></span><span class="fur-27"></span><span class="fur-26"></span><span class="fur-25"></span><span class="fur-24"></span><span class="fur-23"></span><span class="fur-22"></span><span class="fur-21"></span><span class="fur-20"></span><span class="fur-19"></span><span class="fur-18"></span><span class="fur-17"></span><span class="fur-16"></span><span class="fur-15"></span><span class="fur-14"></span><span class="fur-13"></span><span class="fur-12"></span><span class="fur-11"></span><span class="fur-10"></span><span class="fur-9"></span><span class="fur-8"></span><span class="fur-7"></span><span class="fur-6"></span><span class="fur-5"></span><span class="fur-4"></span><span class="fur-3"></span><span class="fur-2"></span><span class="fur-1"></span></div><div class="effect-lumieres"><span class="lamp-1"></span><span class="lamp-2"></span><span class="lamp-3"></span><span class="lamp-4"></span><span class="lamp-5"></span><span class="lamp-6"></span><span class="lamp-7"></span><span class="lamp-8"></span><span class="lamp-9"></span><span class="lamp-10"></span><span class="lamp-11"></span><span class="lamp-12"></span><span class="lamp-13"></span><span class="lamp-14"></span><span class="lamp-15"></span><span class="lamp-16"></span><span class="lamp-17"></span><span class="lamp-18"></span><span class="lamp-19"></span><span class="lamp-20"></span><span class="lamp-21"></span><span class="lamp-22"></span><span class="lamp-23"></span><span class="lamp-24"></span><span class="lamp-25"></span><span class="lamp-26"></span><span class="lamp-27"></span><span class="lamp-28"></span></div></div><div class="helper-2"><div class="effect-brush"><span class="fur-31"></span><span class="fur-30"></span><span class="fur-29"></span><span class="fur-28"></span><span class="fur-27"></span><span class="fur-26"></span><span class="fur-25"></span><span class="fur-24"></span><span class="fur-23"></span><span class="fur-22"></span><span class="fur-21"></span><span class="fur-20"></span><span class="fur-19"></span><span class="fur-18"></span><span class="fur-17"></span><span class="fur-16"></span><span class="fur-15"></span><span class="fur-14"></span><span class="fur-13"></span><span class="fur-12"></span><span class="fur-11"></span><span class="fur-10"></span><span class="fur-9"></span><span class="fur-8"></span><span class="fur-7"></span><span class="fur-6"></span><span class="fur-5"></span><span class="fur-4"></span><span class="fur-3"></span><span class="fur-2"></span><span class="fur-1"></span></div></div><div class="helper-3"><div class="effect-brush"><span class="fur-31"></span><span class="fur-30"></span><span class="fur-29"></span><span class="fur-28"></span><span class="fur-27"></span><span class="fur-26"></span><span class="fur-25"></span><span class="fur-24"></span><span class="fur-23"></span><span class="fur-22"></span><span class="fur-21"></span><span class="fur-20"></span><span class="fur-19"></span><span class="fur-18"></span><span class="fur-17"></span><span class="fur-16"></span><span class="fur-15"></span><span class="fur-14"></span><span class="fur-13"></span><span class="fur-12"></span><span class="fur-11"></span><span class="fur-10"></span><span class="fur-9"></span><span class="fur-8"></span><span class="fur-7"></span><span class="fur-6"></span><span class="fur-5"></span><span class="fur-4"></span><span class="fur-3"></span><span class="fur-2"></span><span class="fur-1"></span></div></div><div class="helper-4"><div class="effect-brush"><span class="fur-31"></span><span class="fur-30"></span><span class="fur-29"></span><span class="fur-28"></span><span class="fur-27"></span><span class="fur-26"></span><span class="fur-25"></span><span class="fur-24"></span><span class="fur-23"></span><span class="fur-22"></span><span class="fur-21"></span><span class="fur-20"></span><span class="fur-19"></span><span class="fur-18"></span><span class="fur-17"></span><span class="fur-16"></span><span class="fur-15"></span><span class="fur-14"></span><span class="fur-13"></span><span class="fur-12"></span><span class="fur-11"></span><span class="fur-10"></span><span class="fur-9"></span><span class="fur-8"></span><span class="fur-7"></span><span class="fur-6"></span><span class="fur-5"></span><span class="fur-4"></span><span class="fur-3"></span><span class="fur-2"></span><span class="fur-1"></span></div></div></netflixintro></div><script>let sleep = ms => {return new Promise(resolve => setTimeout(resolve, ms));};sleep(5200).then(() => { window.location.replace ("/"); });</script></body></html>'''
@app.route('/')
def index():header();conn=sqlite3.connect('customers.db');conn.row_factory=sqlite3.Row;customer=conn.execute('SELECT * FROM customer').fetchall();conn.close();return render_template_string('''<!DOCTYPE html><html><head><meta charset="UTF-8" /><title>DataBase Report</title><link rel="shortcut icon" type="image/x-icon" href="data:image/png;base64,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"><style>body{font-family:Arial, sans-serif;background-color: #111;}.grid{border-collapse:collapse;font-family:Arial, sans-serif;font-size:12px;color:rgb(233, 240, 240);border-top:1px solid #2e9bce;border-left:1px solid #2e9bce;}.cell{background-color:#222426;text-align:left;padding-top:7px;padding-left:4px;padding-right:4px;padding-bottom:7px;border-bottom-width:1px;border-bottom-color:#2e9bce;border-bottom-style:solid;border-right-width:1px;border-right-color:#2e9bce;border-right-style:solid;}.totalCell{background-color:#222426;font-weight:700;text-align:left;padding-top:7px;padding-left:4px;padding-right:4px;padding-bottom:7px;border-bottom-width:1px;border-bottom-color:#2e9bce;border-bottom-style:solid;border-right-width:1px;border-right-color:#2e9bce;border-right-style:solid;}.rowHeaderCell{background-color:#222426;padding-top:7px;padding-left:4px;padding-right:4px;padding-bottom:7px;border-bottom-width:1px;border-bottom-color:#2e9bce;border-bottom-style:solid;border-right-width:1px;border-right-color:#2e9bce;border-right-style:solid;}.columnHeaderCell{background-color:#191D1F;padding-top:7px;padding-left:4px;padding-right:4px;padding-bottom:7px;border-bottom-width:1px;border-bottom-color:#2e9bce;border-bottom-style:solid;border-right-width:1px;border-right-color:#2e9bce;border-right-style:solid;}.title{color: rgb(233, 240, 240);padding-top:7px;padding-left:420px;;padding-bottom:10px;}</style><h1 class="title">DataBase Report<img style="width: 50px;" src="data:image/png;base64,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"></h1></head><body><div class='title'></div><table class='grid'><tr><td class='columnHeaderCell' style='width:149px;'>ID</td><td class='columnHeaderCell' style='width:100px;'>Name</td><td class='columnHeaderCell' style='width:100px;'>username</td><td class='columnHeaderCell' style='width:125px;'>Phone Number</td><td class='columnHeaderCell' style='width:125px;'>Email</td><td class='columnHeaderCell' style='width:125px;'>Address</td><td class='columnHeaderCell' style='width:125px;'>Product Name</td><td class='columnHeaderCell' style='width:125px;'>Product Price</td><td class='columnHeaderCell' style='width:125px;'>Purchase Date</td></tr>{% for view in customer %}<div class="view"><tr><td class='rowHeaderCell' style='width:149px;'>{{ view['ID'] }}</td><td class='cell' style='width:100px;'>{{ view['Name'] }}</td><td class='cell' style='width:100px;'>{{ view['username'] }}</td><td class='cell' style='width:125px;'>{{ view['Phone_Number'] }}</td><td class='cell' style='width:125px;'>{{ view['Email'] }}</td><td class='cell' style='width:125px;'>{{ view['Address'] }}</td><td class='cell' style='width:125px;'>{{ view['Product_Name'] }}</td><td class='cell' style='width:125px;'>{{ view['Product_Price'] }}</td><td class='cell' style='width:125px;'>{{ view['Date_of_Purchase'] }}</td></tr></div>{% endfor %}</table></body></html>''',customer=customer)
header();webbrowser.open("http://127.0.0.1:5079/intro");app.run(port=5079)
