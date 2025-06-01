# 🐾 Paw Fact

![PawFact Demo Image](https://i.postimg.cc/yxGyjyLB/Screenshot-2025-06-01-at-3-38-19-AM.png)

Paw Fact is a fun, browser-based app that fetches random cat facts from an external API. Built with Flask, it lets users click a button to fetch a new cat fact instantly. It displays a random cat fact in your browser.

It was originally created for an MLH hackathon, and while the early version was built in a short time frame, I’ve since expanded on it. It’s currently functional, with room for improvement.

- Pulls live data from a [cat facts API](https://catfact.ninja/)
  
- Lets users click a button to load a new fact
  
- Built with Flask (Python) + simple HTML/JS frontend
  
- Uses Jinja templating to dynamically render HTML pages

---

## 🌱 Building Paw Fact

Paw Fact is currently not deployed online, but you can easily build and run it locally on your machine. To get started, clone the repository, install Flask, and run the app using Python.

### Clone the repository

```bash
git clone https://github.com/hagerbahar-cs/paw-fact.git
cd paw-fact
```

Install Flask (if you don't have it)
```
pip install Flask
```

Run the app
Use the latest version of Python, or at least version 3.12:
```
python3.12 PawFact.py
```
This will start a Flask server, and you can open your browser to see Paw Fact in action!


## 🌱 Future Improvements

While Paw Fact is fully functional and fun to use, here are some planned enhancements to make it even better:

   - Improve responsiveness for mobile devices, ensuring the layout and UI don’t break on smaller screens.

   - Add more sound effects and allow users to toggle sounds on/off for a richer experience.

   - Expand fact categories to include other animals like dogs, birds, and more.

   - Build a custom backend API to manage and serve facts instead of relying on an external API.

   - Enhance accessibility by improving keyboard navigation and screen reader support.

## 🛠️ Technologies Used

 - Python 3.12+
 - Flask
 - Jinja templating
 - JavaScript
 - HTML/CSS

