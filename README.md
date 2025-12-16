# SimpleHTML5

A multipage static site template using semantic HTML5 and responsive CSS3 layouts.

## Features

- Semantic HTML5 structure
- Responsive CSS3 design

## Version 1 (root directory)

- What you had last week
- Basic static HTML5 and CSS3 files

To see it in action use "Go Live" & open `index.html` in a web browser.

## Version 2 (v2 directory)

- Improved layout and styling
- Enhanced styling with CSS3 Flexbox and Grid
- Improved accessibility features with switches for dark mode
- Hero area
- Article sections with images and captions

To see it in action use "Go Live" & open `v2/` in a web browser.

You should be able to combine the features from v2 with your code from
last week.

### Task: About Page Issue

- What is wrong with the About page? Fix it.
- What would be a better fix?

## Version 3 (v3-src directory)

- Optional advanced version using Jinja2 templating and Python build script
- Static site generation using Jinja2 templates
- Automated build process with Python script
- Modular template structure for easy maintenance
- Output static files in build directory  

### Usage

1. Ensure you have Python and Jinja2 installed.
2. Run the build script to generate the static site:

   ```bash
   python build-v3.py
   ```  

3. The generated static files will be available in the `build` directory.

### GitHub Pages deploy workflow

This repository includes a GitHub Actions workflow at `.github/workflows/deploy-pages.yml` that can deploy one of three site variants:

- `v1` (root directory)
- `v2` (the `v2/` directory)
- `v3` (build output from `v3-src/` using `build-v3.py`)

Follow these steps to enable deployment via GitHub Actions and choose which variant to publish.

1. In the repository, go to Settings → Pages.
   - Under Source, change from "Deploy from a branch" to "GitHub Actions".
   - By default, the workflow deploys the root directory (v1).
   
2. (Optional) Set the deployment variant using a Repository Variable:
   - To deploy a different variant, go to Settings → Secrets and variables → Actions → Variables.
   - Click "New repository variable" and add:
     - Name: `SITE_TYPE`
     - Value: `v2` to deploy the `v2/` site, or `v3` to build and deploy from `v3-src/`.
     - Leave blank or set to `v1` for the default root directory deployment.

3. Trigger a deployment:
   - Push to the `main` branch, or
   - Run the workflow manually from the Actions tab ("Deploy site to GitHub Pages").

How it works:

- When `SITE_TYPE` is `v3`, the workflow sets up Python, installs Jinja2, runs `python build-v3.py`, and uploads the `build/` directory.
- When `SITE_TYPE` is `v2`, the workflow uploads the `v2/` directory.
- When `SITE_TYPE` is `v1` or blank (default), the workflow uploads the repository root (`./`).

After a successful run, the site will be available at the Pages URL shown in Settings → Pages and in the workflow run summary.

## Tasks for You to Implement

- Choose your own order to implement these features!
- add make sure you are doing them in the correct folder (the base folder  
or v3-src)

## Add another page

Create a new HTML page (e.g., `services.html`) in the appropriate directory.

## Task: Add a YouTube Video Embed

Embed a responsive YouTube video in your webpage.

### Pointers:

1. **HTML Structure**
   - Use a `<figure>` element to contain the video and caption
   - Inside the `<figure>`, add a `<div>` with a class (e.g., `video-container`) to hold the iframe
   - Add an `<iframe>` element with the YouTube embed URL which you can get from the "Share" -> "Embed" option on YouTube
   - Set the `width` and `height` attributes to `100%` for responsiveness   
   - Add a `<figcaption>` for the video description

## Task: Add a diagrams with Mermaid.js

Great for flowcharts, sequence diagrams, and more.

Add the Mermaid.js library to your HTML file by including the following script tag in the `<head>` section: 

```html
<script src="https://unpkg.com/mermaid/dist/mermaid.min.js"></script>
```

Then add the diagram where you like in the main content area:it will work 
best in the art

```html
<figure>
    <div class="mermaid">
        graph TD;
        A-->B;
        B-->C;
    </div>
    <figcaption>Simple Mermaid Diagram</figcaption>
</figure>
```

You can use any Mermaid syntax to create different types of diagrams.
Visit [https://mermaid.js.org/](https://mermaid.js.org) and use the Free version to design your diagrams.

## Task: Add a simple map

Embed an OpenStreetMap map into your webpage.

### Pointers:

- Open [https://www.openstreetmap.org](https://www.openstreetmap.org/)
![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*pLggZxtqH99TVK-E8blPIQ.png)

- Search for a place you want
- Right-click and click on “show address”
![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*_d3Cs3oKXdXfDJmy27DmUA.png)

- On the right side click on the share
![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*j3yQ5mNu2B68ACZ87oO1xg.jpeg)

- Click on HTML and copy the iframe code and paste it into your HTML document
![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*4FPsepkyxnjj5yPxhWu5CA.jpeg)

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*874SQpS95CwRJVA7Syz7uA.jpeg)

## Task: Hero Image with Text Overlay

Create a hero section with a full-width background image and centered text overlay.

### Pointers:

     You already have a hero section in `index.html` with the class `hero`.
     1. Pick a high-quality image and add it to the `assets/images/` directory.
     2. In your CSS file, set the `.hero` class to use the image as a background:
        - Use `background-image: url('path/to/your/image.jpg');`
        - Set `background-size: cover;` and `background-position: center;`   
        - Set a fixed height for the hero section (e.g., `height: 400px;`)
        3. Center the text overlay using flexbox:
        - `display: flex; justify-content: center; align-items: 
        
## Task: Mobile Menu Toggle

Add a hamburger menu button that shows/hides a navigation menu on smaller screens.

### Pointers

1. **HTML Structure**
   - Add a `<button>` element with id `menu-button` in your header
   - Add an id `nav-menu` to your existing `<nav>` element
   - Use the `aria-label` and `aria-expanded` attributes for accessibility

2. **CSS Styling**
   - Hide the button by default with `display: none`
   - Use a media query `@media (max-width: 768px)` to show it on mobile
   - Position the menu absolutely when it appears on mobile
   - Add a `.active` CSS class that shows/hides the menu (use `max-height` or `display` to toggle visibility)
   - Add a smooth `transition` for the menu opening/closing animation

3. **JavaScript Event Listeners**
   - Listen for clicks on the menu button and toggle the `.active` class on the nav menu
   - Update the `aria-expanded` attribute when the menu opens/closes
   - Add a click listener to all nav links so the menu closes when a user navigates
   - Bonus: Close the menu if the user clicks outside of it (use `event.target` and `.contains()`)

4. **Testing**
   - Test on desktop (button should be hidden)
   - Test on mobile/tablet (button should appear)
   - Test that clicking the button toggles the menu
   - Test that clicking a nav link closes the menu

#### Hints

- Use `document.getElementById()` and `document.querySelectorAll()` to select elements
- Use `classList.toggle()` and `classList.remove()` to manage the `.active` class
- Use `addEventListener('click', ...)` to handle user interactions

## Task: Add a relevant widget

A widget is html/css/javascript that you can drop into you page fairly easily
to do a task or add information.

I comes with other peoples images and styles so be careful to check it works
well with your own design.

### Weather widget

Embed a simple weather widget using a third-party service like WeatherWidget.io.

- [https://www.forecast.co.uk/widget/](https://www.forecast.co.uk/widget/)
- [https://weatherwidget.io/](https://weatherwidget.io/)
- [https://www.theweather.com/widget/](https://www.theweather.com/widget/)
- [https://meteo.uk/widget/](https://meteo.uk/widget/)

### Christmas Widgets

- [https://www.geeksforgeeks.org/html/decorating-your-website-for-christmas-and-new-year-html-css-code-snippets/](https://www.geeksforgeeks.org/html/decorating-your-website-for-christmas-and-new-year-html-css-code-snippets/)
- [https://www.perssondennis.com/articles/33-christmas-animations-to-easily-add-to-your-website](https://www.perssondennis.com/articles/33-christmas-animations-to-easily-add-to-your-website)

### History timeline widget

- [https://timeline.knightlab.com/](https://timeline.knightlab.com/)

## Advanced Task : APIs

*Application Programming Interfaces* (APIs) allow you to fetch data from other
services and display it on your own site.

They usually require some JavaScript to make the request and handle the
response. And often require you to sign up for an API key.

### Task: Add weather into your own html using a weather API

Fetch weather data from a public API (like OpenWeatherMap) and display it on your webpage.

- [https://www.geeksforgeeks.org/javascript/weather-app-using-vanilla-javascript/](https://www.geeksforgeeks.org/javascript/weather-app-using-vanilla-javascript/)
- [https://medium.com/@ravipatel.it/a-comprehensive-guide-to-fetching-weather-data-using-javascript-fetch-api-13133d0bc2e6](https://medium.com/@ravipatel.it/a-comprehensive-guide-to-fetching-weather-data-using-javascript-fetch-api-13133d0bc2e6)
- [https://javascript.plainenglish.io/build-a-real-time-weather-app-with-javascript-and-openweathermap-api-bcf8111df1fe](https://javascript.plainenglish.io/build-a-real-time-weather-app-with-javascript-and-openweathermap-api-bcf8111df1fe)

### Christmas APIs

- [https://christmascountdown.live/api#/joke](https://christmascountdown.live/api#/joke)
- [https://github.com/christmas-countdown/christmas.js](https://github.com/christmas-countdown/christmas.js)
