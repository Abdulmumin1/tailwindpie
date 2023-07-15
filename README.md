# Tailwindpie

Easiest way to setup tailwind in your Python projects.

Just a command away!

### Requirements

Because tailwind depends on node and stuff, you are going  to need to have the following installed

- Nodejs

- npm - comes with node, so no worries.

## Installation

```bash
pip install tailwindpie
```

In your project directory, run

```bash
$ tailwindpie config
```

Lastly, 

In the create tailwind.config.js

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./{folder that contains your html}/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

Ok, one more thing

update the package.json with where you want to store the generated css

```json
"css": "npx tailwindcss -i ./input.css -o .{Folder}/tailwind.css --watch"
```

> **Note**: make sure the folder is created!

In your HTML, add the path to the css

```html
<link
      rel="stylesheet"
      type="text/css"
      href="{{ url_for('static', filename='css/tailwind.css')}}"
/>
```

In this case, we are using it in the base.html file of a Flask project!



## Build css

once you have all this properly setup, you can then build the css.

```bash
$ tailwindpie build
```

This commands will continue to run and track changes in your html and rebuilds the CSS.

### Why?

On the initial build of tailwindCSS, not all the class are created and written into the 'tailwind.css' file. I mean it doesn't even make any sense, There are ten of thousands of classes available in tailwind and this can even extend further.

This is why tailwind tracks changes in your files and only adds to the CSS file, classes that you've used in your project.

> When you are done, you can stop the build command with **Ctrl + C**

# BOOM!!!

Let the magik of tailwind begins
