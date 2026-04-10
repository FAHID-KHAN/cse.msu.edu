# Plan: Full-Stack Expense Tracker — Code to Deployment

Build a complete **Expense Tracker** (React + Express + PostgreSQL) from zero to deployed on Render — every step an enterprise app goes through. You code everything; each phase explains **what**, **why**, and **what to think about before writing a single line**.

---

## Tech Stack

| Layer | Tech | Why |
|---|---|---|
| Backend | Express.js | Minimal, teaches the middleware pattern clearly |
| Database | PostgreSQL + Prisma ORM | Schema-driven dev, real migrations, enterprise standard |
| Frontend | React (Vite) + React Router | Fast, modern, industry default |
| Auth | JWT + bcryptjs | Teaches token-based auth flow end to end |
| Testing | Jest, Supertest, Vitest, React Testing Library | Backend + frontend coverage |
| Containers | Docker + Docker Compose | Run the full stack with one command |
| CI/CD | GitHub Actions | Automated lint → test → build → deploy |
| Hosting | Render (free tier) | Zero infra overhead, focused on learning code |

---

## Phase 0: Project Setup & Architecture (Day 1)

**Teaches:** Monorepo structure, tooling choices, git discipline.

Create GitHub repo → clone → set up folder structure:
```
expense-tracker/
├── server/       # Express API
├── client/       # React app
├── docker/       # Dockerfiles
├── .github/      # CI workflows
├── .gitignore
└── README.md
```
Init `server/` with npm, scaffold `client/` with Vite. Write `.gitignore`. First commit.

**Think first:** Why separate folders? What happens when 5 devs work on this — who touches what?

---

## Phase 1: Backend Skeleton (Day 2)

**Teaches:** Express middleware pipeline, request lifecycle, centralized error handling, why `app.js` and `server.js` are separate files.

Build: `app.js` (middleware chain: morgan → cors → json → routes → error handler), `server.js` (just `app.listen`), `middleware/errorHandler.js` (4-param catch-all), `config/index.js` (reads env vars), health check endpoint `GET /api/health`.

### Backend folder structure
```
server/
├── src/
│   ├── app.js              # Express app setup (middleware, routes)
│   ├── server.js           # HTTP server startup (listen on port)
│   ├── routes/             # Route definitions
│   │   └── index.js        # Route aggregator
│   ├── controllers/        # Request handlers (business logic)
│   ├── services/           # Data access / business rules
│   ├── middleware/
│   │   └── errorHandler.js # Centralized error handling
│   └── config/
│       └── index.js        # Environment config
├── .env                    # Local env vars (never commit)
├── .env.example            # Template (commit this)
└── package.json
```

**Think first:** Why does the error handler have 4 parameters? Why separate app from server? (Testing.)

---

## Phase 2: Database (Day 3)

**Teaches:** Docker Compose for dev services, schema design, migrations, why ORMs exist, why `Decimal` for money.

Docker Compose for PostgreSQL → Prisma init → design schema (User model + Expense model with category enum: FOOD, TRANSPORT, ENTERTAINMENT, UTILITIES, SHOPPING, HEALTH, OTHER) → first migration → seed data → Prisma client singleton.

### Schema design
- **User:** id, email, password, name, createdAt
- **Expense:** id, amount (Decimal), category (enum), description, date, createdAt, updatedAt
- Relation: User has many Expenses

**Think first:** Why enum for categories, not free text? Why `Decimal` not `Float`? (Try `0.1 + 0.2` in JS.)

---

## Phase 3: REST API — Expenses CRUD (Day 4–5)

**Teaches:** RESTful design, 3-layer pattern (route → controller → service), input validation, HTTP status codes, pagination, IDOR prevention.

Build the 3 layers:
- **Service:** `getAll`, `getById`, `create`, `update`, `remove`, `getSummary` — always filtered by userId
- **Controller:** maps req/res to service calls
- **Validation middleware:** amount > 0, valid enum, ISO date, description ≤ 200 chars
- **Routes:** 6 endpoints:
  - `GET    /api/expenses`        — list with query params (?category=FOOD&page=1&limit=10)
  - `GET    /api/expenses/summary` — aggregated stats
  - `GET    /api/expenses/:id`    — single expense
  - `POST   /api/expenses`        — create (validate body)
  - `PUT    /api/expenses/:id`    — update (validate body)
  - `DELETE /api/expenses/:id`    — delete

**Think first:** Why does `getById` need `userId`? (IDOR attack.) Why validate server-side even if the frontend validates?

---

## Phase 4: Frontend Setup (Day 6)

**Teaches:** React project structure, API layer separation, env variables, component hierarchy.

### Frontend folder structure
```
client/
├── src/
│   ├── api/
│   │   └── expenses.js     # All API calls (fetch wrapper)
│   ├── components/
│   │   ├── Layout.jsx       # Shared layout (nav, footer)
│   │   ├── ExpenseList.jsx
│   │   ├── ExpenseForm.jsx
│   │   ├── ExpenseCard.jsx
│   │   ├── Dashboard.jsx
│   │   ├── CategoryFilter.jsx
│   │   └── ProtectedRoute.jsx
│   ├── pages/
│   │   ├── HomePage.jsx
│   │   ├── ExpensesPage.jsx
│   │   ├── DashboardPage.jsx
│   │   ├── LoginPage.jsx
│   │   └── SignupPage.jsx
│   ├── context/
│   │   └── AuthContext.jsx
│   ├── hooks/
│   │   └── useExpenses.js   # Custom hook for expense data
│   ├── App.jsx              # Routes + Layout
│   ├── main.jsx             # Entry point
│   └── index.css
├── .env                     # VITE_API_URL=http://localhost:3000
└── .env.example
```

Create the API service layer in one file — all fetch calls go through here. Set up React Router with 5 routes. Build `Layout.jsx` with nav.

**Think first:** Why a single `api/expenses.js` file? What happens if the backend URL changes?

---

## Phase 5: Frontend UI (Day 7–8)

**Teaches:** Component composition, controlled forms, custom hooks, lifting state.

Build bottom-up:
1. `ExpenseCard` (dumb, receives props)
2. `ExpenseList` (maps cards)
3. `ExpenseForm` (controlled inputs, works for create AND edit)
4. `CategoryFilter`
5. `ExpensesPage` (smart, manages state)
6. Extract `useExpenses` custom hook
7. `Dashboard` with summary stats

Plain CSS only — no frameworks.

**Think first:** Why a custom hook? What would the page component look like without it?

---

## Phase 6: Authentication (Day 9–10)

**Teaches:** JWT flow, password hashing, auth middleware, protected routes, security basics.

### Backend
- `authService`: signup hashes password (bcrypt, 10 salt rounds), login compares hash, both return JWT
- `authController` + routes: `POST /auth/signup`, `POST /auth/login`, `GET /auth/me`
- Auth middleware: reads `Bearer` token → verifies → attaches `req.userId` → 401 if invalid
- Protect all expense routes with auth middleware

### Frontend
- `AuthContext`: stores token in localStorage, provides `login()`, `signup()`, `logout()`, `user`, `isAuthenticated`
- `LoginPage` + `SignupPage`: forms that call AuthContext
- `ProtectedRoute`: wraps routes, redirects to `/login` if unauthenticated
- API layer attaches `Authorization` header to all requests

**Think first:** Why hash passwords? What if the DB leaks? Why does the JWT secret NEVER go in code?

---

## Phase 7: Testing (Day 11–12)

**Teaches:** Testing pyramid, what to test, mocking, test isolation.

### Backend (Jest + Supertest)
- Unit tests for `expenseService`: valid create, reject negative amount, user can't see others' expenses, summary calculation
- Integration tests for API routes: 201 on create, 400 on invalid, 401 without token, 404 for other user's expense

### Frontend (Vitest + React Testing Library)
- `ExpenseCard` renders amount, category, date correctly
- `ExpenseForm` calls onSubmit with form data
- `ExpenseForm` shows validation errors for empty fields
- `ExpenseList` shows "No expenses" when array is empty

**Think first:** Why test that users can't see each other's data? What real-world bug does this catch?

---

## Phase 8: Docker (Day 13)

**Teaches:** Containers, multi-stage builds, Docker networking, non-root users.

- `docker/server.Dockerfile` — 2-stage: install deps + generate Prisma → slim runtime, non-root user
- `docker/client.Dockerfile` — 2-stage: Vite build → serve with Nginx
- `docker/nginx.conf` — serve static files + proxy `/api` to backend
- Update `docker-compose.yml` for full stack: postgres + server + client
- Add `Makefile` shortcuts: `make dev`, `make build`, `make down`

**Think first:** Why multi-stage? Why non-root? Why does Nginx proxy `/api` to the backend?

---

## Phase 9: CI/CD Pipeline (Day 14)

**Teaches:** Automated quality gates, pipeline stages, fail-fast principle, parallel jobs.

GitHub Actions workflow `.github/workflows/ci.yml`:
1. **lint** — ESLint on both projects (fastest, runs first)
2. **test-backend** — PostgreSQL service container, Prisma migrations, Jest *(depends on lint)*
3. **test-frontend** — Vitest *(parallel with test-backend)*
4. **build** — build Docker images *(depends on both test jobs)*
5. **deploy** — deploy to Render *(main branch only, depends on build)*

**Think first:** Why lint before tests? Why parallel test jobs? Why deploy only from main?

---

## Phase 10: Deploy to Render (Day 15)

**Teaches:** Production environment, env management, production DB, HTTPS, SPA routing.

1. Create Render PostgreSQL (free tier)
2. Deploy backend as Web Service — build: `npm install && npx prisma migrate deploy && npx prisma generate`, start: `node src/server.js`
3. Deploy frontend as Static Site — build: `npm install && npm run build`, publish: `dist`, rewrite: `/* → /index.html`
4. Set all env vars (DATABASE_URL, JWT_SECRET, NODE_ENV, VITE_API_URL, CLIENT_URL)
5. Update CORS for production frontend URL
6. Test live: signup → login → add expenses → dashboard
7. Write README: live link, architecture diagram, setup instructions, screenshots

**Think first:** Why `migrate deploy` not `migrate dev` in production? Why the rewrite rule for React Router?

---

## Verification Checklist

| Phase | How to verify |
|---|---|
| 0 | Repo exists on GitHub with clean structure |
| 1 | `curl localhost:3000/api/health` → `{"status":"ok"}` |
| 2 | `npx prisma studio` shows tables with seed data |
| 3 | All 6 endpoints work via curl/Postman |
| 4 | React loads at `localhost:5173`, nav works |
| 5 | Full CRUD in UI works, dashboard shows stats |
| 6 | Signup → login → only own expenses visible → 401 without token |
| 7 | `npm test` green in both server/ and client/ |
| 8 | `docker compose up --build` → full app at `localhost` |
| 9 | GitHub Actions pipeline runs green on push |
| 10 | Live URL: signup → expenses → dashboard → works |

---

## Final Project Structure

```
expense-tracker/
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Makefile
├── docker/
│   ├── server.Dockerfile
│   ├── client.Dockerfile
│   └── nginx.conf
├── server/
│   ├── src/
│   │   ├── app.js
│   │   ├── server.js
│   │   ├── config/index.js
│   │   ├── lib/prisma.js
│   │   ├── routes/index.js, expenses.js, auth.js
│   │   ├── controllers/expenseController.js, authController.js
│   │   ├── services/expenseService.js, authService.js
│   │   └── middleware/errorHandler.js, auth.js, validate.js
│   ├── prisma/schema.prisma, seed.js
│   ├── tests/setup.js, expense.test.js, auth.test.js
│   ├── .env.example
│   └── package.json
├── client/
│   ├── src/
│   │   ├── api/expenses.js
│   │   ├── components/*.jsx
│   │   ├── pages/*.jsx
│   │   ├── context/AuthContext.jsx
│   │   ├── hooks/useExpenses.js
│   │   ├── App.jsx, main.jsx, index.css
│   ├── .env.example
│   └── package.json
├── .gitignore
└── README.md
```

---

## Architecture Decisions

| Decision | Reasoning |
|---|---|
| **Prisma** over raw SQL | Teaches schema-driven dev and migrations. Raw SQL is a separate skill to learn later. |
| **Plain CSS** over Tailwind/MUI | Forces understanding of styling fundamentals. No framework magic. |
| **localStorage** for JWT | Simpler for learning. HttpOnly cookies are safer (noted as learning point). |
| **No state management library** | Context + hooks is sufficient at this scale. Redux/Zustand adds complexity without teaching core patterns. |
| **Render** over AWS/Azure | Free tier, zero infra overhead. Focus on code, not cloud console navigation. |

---

## What to Add Next (After Completing All 10 Phases)

- Rate limiting on auth endpoints
- File upload for receipt images
- Email notifications (welcome email, weekly summary)
- WebSocket for real-time dashboard updates
- Admin panel
- Pagination with cursor-based approach
- HttpOnly cookie auth (replace localStorage)
- Monitoring with health dashboards
