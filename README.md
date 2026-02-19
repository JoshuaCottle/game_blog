# The Game Ledger — Game Blog

**Live site:** TBD

**Repository:** https://github.com/JoshuaCottle/game_blog

**Responsibility / Ownership**

- Primary author: Joshua Cottle
- Responsibilities: project structure, Django models/views/forms, templates, styling, and documentation

**Brief**

The Game Ledger is a Django blog platform for video, board, and tabletop games.
Users can register, create posts with images, comment, and like posts. The home
page supports filtering by game type and searching by title.

**External User's Goal**

Browse game-focused posts quickly, filter by type, and engage through comments
and likes.

**Site Owner's Goal**

Provide a clean, reliable blog experience with basic moderation controls and a
simple publishing workflow.

**Contents**

- `blog/` — app (models, views, forms, templates)
- `Game_Blog/` — project settings and URLs
- `templates/` — base and page templates
- `media/` — uploaded post images (local dev)
- `requirements.txt` — dependencies

**UX**

User stories:

- As a visitor, I want to see recent posts with images so I can quickly choose
	what to read.
- As a reader, I want to filter posts by game type so I can focus on my interests.
- As a user, I want to create and edit posts with images so I can share content.
- As a user, I want to comment and like posts to engage with the community.
- As a post author, I want only my own posts editable so my content is protected.

**Design**

- Clean layout using a card-based structure
- Accessible form controls and clear spacing
- Responsive layout for desktop and mobile

**Wireframes**

- Desktop: TBD
- Tablet: TBD
- Mobile: TBD

**Website Features**

- Post list with filter buttons (video, board, tabletop)
- Search by post title
- Image uploads for posts, shown on list and detail pages
- CRUD for posts (author-only edit/delete)
- Comments and likes on post detail pages
- Authentication (register, login, logout)

**Future Features (Ideas)**

- Tagging system for more granular filtering
- Comment edit/delete for comment authors
- Image optimization and thumbnails in production

**Technologies Used**

- Python 3
- Django 4.2
- SQLite (local) / PostgreSQL (production)
- HTML, CSS
- Cloudinary (planned for production media)

**Testing**

- Manual testing: TBD (add table of test cases)
- Unit tests: TBD (models, views, forms)
- Validation: TBD (HTML/CSS, Lighthouse)

**Deployment**

- Heroku (planned)
- Environment variables required:
	- `SECRET_KEY`
	- `DATABASE_URL`
	- `CLOUDINARY_URL` (if using Cloudinary)
	- `DEBUG` (set to `False` in production)

**Local Setup**

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
./.venv/Scripts/python.exe -m pip install -r requirements.txt
```

3. Create `env.py` and set `SECRET_KEY` (and `DATABASE_URL` if using Postgres).
4. Apply migrations:

```bash
./.venv/Scripts/python.exe manage.py migrate
```

5. Run the dev server:

```bash
./.venv/Scripts/python.exe manage.py runserver
```

Visit http://127.0.0.1:8000/

**AI Use**

- Code assistance used for debugging template formatting, refactoring, and
	drafting documentation sections.

**Credits**

- Project Author: Joshua Cottle
- Icons/Images: Author-provided or user-uploaded content
