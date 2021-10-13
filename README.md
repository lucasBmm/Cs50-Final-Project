# Tech News

#### Video Demo: https://www.youtube.com/watch?v=mHYZs7Fjr_o

### Technologies used:

* Python

* Flask

* HTML, CSS and Javascript

* Bootstrap

* Jquery

* Sqlite3

  

### Interfaces used:

* VS Code
* SQLiteSTUDIO
* CS50 IDE



#### Why a News Website?

​	My final project is a News Website, and there are some reasons why I choose it:  through the course, I decided that I wanted to become a Web Developer, there some reasons to that, but most importantly, it's because i really enjoyed the Web development part of the course, enjoyed how I can see directly what i was doing, a bit differently than making code with C or Python, it was much more visual, and even other people that don't understand a single line of code can see and appreciate my code.

​	One of my main goals in life right now is get a internship as a developer, and due to some personal research, I found out that most vacancies for internship here in Brazil are for Web development, and that fact made me be even more certain of my choice, so, let's advance to what is most important, the project.

​	I had the idea to make a News Web page due to a Youtube video from a company that was hiring junior developers, and in the video they was analyzing the candidates code, but the back-end was in PHP, and I don't know nothing about PHP, but I really liked the idea, and decided to implement the website in Flask using the knowledge acquired in CS50 and implement it with some personal ideas. That was the Youtube video: https://www.youtube.com/watch?v=Fss8_UR8CPg&t=1127s

​	It was really challenging in the beginning, because there had a lots of things that I don't learned in CS50 videos, but the most valuable thing CS50 teached me was learn how to overcome challenges by myself, so that was I did, a LOT o things I doesn't had any idea in how to solve, but I tried various ideas, and when I run out of ideas I Googled it, Stack Overflow was my best friend by the time haha.

#### Starting the project

​	Now, let's talk about the code itself: In first place I decided what pages my website needed, and it was a homepage, a news page(to display all news in website), write (to add more news), a contact page (it doesn't need to work, because that's not my main goal), a search engine and a page for each news (that's was the biggest challenge for me).

​	Firstly I made the layout page that all other pages would use, secondly a made the homepage, and had the idea of showing the 3 latest news, but I did it only in the end of my project. After that, I made the write news page. In the beginning of the project I was thinking to use other database than Sqlite3, but to some technical problems, I decided to sticky to Sqlite, and used SQliteStudio and CS50 IDE to create and make changes in the database, my database have 5 different values: title, subtitle, content, tag and timestamp (witch is automatically), I made 3 forms and one select option to news tags, I used Javascript to check if all forms was filled, and display a error alert if not, and a success if filled, after that submit all the news components to the database, after that I made the Contact Us page, because it  was only visuals, so was very easy and quick to implement. Now the first challenge to really get my was implement a automatically way to show the news from the database to users, I rewatched David Flask lectures to help me with the logical part of the problem and two Youtube videos really helped me handle the HTML,CSS and visuals. This: https://www.youtube.com/watch?v=XRzAZBPp5iQ and this: https://www.youtube.com/watch?v=EYBJ_y4dvIU&t=661s

​	One thing that i decided to do in the process of the project was make some individual Css files for some pages, because I was having a lot of conflicts in the pages, so that really helped. After that i used a simple if statement in home page to display the latest news, it was a piece of cake to implement after the news page, then I implemented the search engine, and was not that difficult at all, the only thing I had some trouble was how to make the "%variable%" that David teached in SQL classes, but with some Overflow research i found out it was simply  concatenate the "%" with the variable, and done, with was working properly, now the only thing left was my biggest problem: how to implement automatically a page for each news. My main doubt was how to pass a variable from a page to another, I tried some stupid ideas, but none was successful, then I decided to searched in flask documentation for some way to solve this problem, and it was much easier than I thought, i just needed to create a blank page for the news and send the loop index to the url, with that, I would simply display the content of that specific loop in the page, something like allnews"[index][0]" and with that it, I made through all the problems in about 2 weeks.

### Final thanks

​	I'm really happy with my results, even my website not being the best design, all the functionalities work, and that was the real problem to me. I'm very exited to start Cs50 Web as soon I finish this and learn even more about Web Development! Cs50 changed my life and form to see the technology, I can say undoubtedly it was **THE BEST** learning experience I had in my entire life, thanks to all Cs50 staff to give this learning opportunity to all people around the globe, things like this is what truly changes the world, my most absolute thanks!!! **THIS WAS CS50!**  