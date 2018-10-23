# django-social_website
A social website to post images from other sites

</br>
Features:

    -> add a bookmarklet to browser toolbar

    -> fetch and post images from other sites using the bookmarklet

    -> following other users, liking image posts [using Ajax]

    -> user Action Feed, to show activity of other users

    -> Image Feed, for all uploaded images [sorl-thumbnail, infinite scrolling by ajax pagination]

    -> Ranked Images based on views [Using Redis]

</br>
**for bookmarklet to work you need to change the site_url in 2 files with your domain.

      1.\images\static\js\bookmarklet.js
      
      2. \images\templates\bookmarklet_launcher.js
  
**Redis server is needed listening on port 6379, for image views counting.

**A super user is already created, username: admin pw: adminadmin123
