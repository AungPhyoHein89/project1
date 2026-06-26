# CS50W Project 1: Wiki

An online encyclopedia-like website built using Python, Django, HTML, and CSS. This project is a part of Harvard's CS50's Web Programming with Python and JavaScript course.

## Features Implemented (Version 1)

* **Entry Page:** Users can view the content of a specific encyclopedia entry by navigating to `/wiki/TITLE`. The page renders Markdown content into proper HTML.
* **Index Page:** The homepage lists all current encyclopedia entries. Clicking on any entry name links directly to that entry's page.
* **Search:** Users can search for entries via the sidebar. If the query matches an entry, they are redirected there. If it matches a substring, a list of search results is displayed.
* **Create New Page:** Allows users to create a new encyclopedia entry with a title and Markdown content. It includes validation to prevent overwriting existing titles.
* **Edit Page:** Users can click an "Edit" button on any entry page to modify its Markdown content.
* **Random Page:** Clicking "Random Page" in the sidebar takes the user to a randomly selected encyclopedia entry.

## Technologies Used

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, Bootstrap (or custom layouts)
* **Markup:** Markdown (converted to HTML using the python-markdown package)
* **Version Control:** Git & GitHub

## How to Run the Project Locally

1. Clone or download the repository.
2. Ensure Python and Django are installed.
3. Open your terminal in the project directory (`wiki`) and run the following command to start the development server:

```bash
python manage.py runserver